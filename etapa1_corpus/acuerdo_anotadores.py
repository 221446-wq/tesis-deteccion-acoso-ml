"""Acuerdo entre anotadores: kappa de Cohen con intervalo de confianza por bootstrap."""
import numpy as np
from sklearn.metrics import cohen_kappa_score


def kappa_con_ic(anotador_a, anotador_b, b=2000, semilla=42):
    """Devuelve el kappa de Cohen y su IC 95 % por remuestreo de relatos."""
    a, c = np.asarray(anotador_a), np.asarray(anotador_b)
    kappa = cohen_kappa_score(a, c)
    rng = np.random.default_rng(semilla)
    valores = []
    for _ in range(b):
        idx = rng.integers(0, len(a), len(a))
        if len(set(a[idx])) > 1 or len(set(c[idx])) > 1:
            valores.append(cohen_kappa_score(a[idx], c[idx]))
    return kappa, np.percentile(valores, [2.5, 97.5])


def acuerdo_porcentual(anotador_a, anotador_b):
    a, c = np.asarray(anotador_a), np.asarray(anotador_b)
    return float((a == c).mean())
