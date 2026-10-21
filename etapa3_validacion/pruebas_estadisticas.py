"""Métricas y pruebas estadísticas para comparar modelos sobre los mismos relatos de prueba."""
import numpy as np
from scipy.stats import chi2
from sklearn.metrics import f1_score


def mcnemar(y_real, pred_a, pred_b):
    """Prueba de McNemar con corrección de continuidad. Devuelve (estadístico, valor p)."""
    acierto_a = np.asarray(pred_a) == np.asarray(y_real)
    acierto_b = np.asarray(pred_b) == np.asarray(y_real)
    n01 = int(np.sum(~acierto_a & acierto_b))   # A falla, B acierta
    n10 = int(np.sum(acierto_a & ~acierto_b))   # A acierta, B falla
    if n01 + n10 == 0:
        return 0.0, 1.0
    estadistico = (abs(n01 - n10) - 1) ** 2 / (n01 + n10)
    return estadistico, float(chi2.sf(estadistico, df=1))


def bootstrap_por_participante(y_real, pred, participantes, metrica=None, b=2000, semilla=42):
    """IC 95 % de una métrica remuestreando participantes (no relatos sueltos)."""
    metrica = metrica or (lambda y, p: f1_score(y, p, average="macro"))
    y_real, pred, participantes = map(np.asarray, (y_real, pred, participantes))
    ids = np.unique(participantes)
    rng = np.random.default_rng(semilla)
    valores = []
    for _ in range(b):
        elegidos = rng.choice(ids, size=len(ids), replace=True)
        idx = np.concatenate([np.where(participantes == i)[0] for i in elegidos])
        valores.append(metrica(y_real[idx], pred[idx]))
    return metrica(y_real, pred), np.percentile(valores, [2.5, 97.5])


def holm(valores_p, alfa=0.05):
    """Ajuste de Holm: devuelve una lista de booleanos (True = se rechaza H0)."""
    orden = np.argsort(valores_p)
    m = len(valores_p)
    rechazar = [False] * m
    for k, i in enumerate(orden):
        if valores_p[i] <= alfa / (m - k):
            rechazar[i] = True
        else:
            break
    return rechazar
