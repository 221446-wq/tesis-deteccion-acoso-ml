"""Configuraciones del diseño experimental con representación TF-IDF.

BETO se entrena aparte con Transformers (ver el plan, Etapa 2).
"""
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline
from sklearn.dummy import DummyClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedGroupKFold, cross_val_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC

SEMILLA = 42


def _tfidf():
    return TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True, min_df=2)


def configuraciones():
    """Devuelve un diccionario {nombre: pipeline} con las líneas base y las 9 configuraciones TF-IDF."""
    clasificadores = {
        "RL": lambda peso: LogisticRegression(max_iter=1000, class_weight=peso, random_state=SEMILLA),
        "SVM": lambda peso: LinearSVC(class_weight=peso, random_state=SEMILLA),
        # Naïve Bayes no admite pesos por clase: la ponderación se aplica usando
        # probabilidades a priori uniformes (fit_prior=False) en lugar de las del corpus
        "NB": lambda peso: MultinomialNB(fit_prior=(peso is None)),
    }
    confs = {"base_mayoritaria": Pipeline([("tfidf", _tfidf()), ("clf", DummyClassifier(strategy="most_frequent"))])}
    for nombre, crear in clasificadores.items():
        confs[f"{nombre}_sin_tratamiento"] = Pipeline([("tfidf", _tfidf()), ("clf", crear(None))])
        confs[f"{nombre}_ponderacion"] = Pipeline([("tfidf", _tfidf()), ("clf", crear("balanced"))])
        confs[f"{nombre}_smote"] = Pipeline([("tfidf", _tfidf()), ("smote", SMOTE(random_state=SEMILLA)), ("clf", crear(None))])
    return confs


def evaluar(confs, textos, etiquetas, participantes, pliegues=5):
    """Validación cruzada agrupada por participante. Devuelve {nombre: (media, desviación)} del macro F1."""
    cv = StratifiedGroupKFold(n_splits=pliegues, shuffle=True, random_state=SEMILLA)
    resultados = {}
    for nombre, pipe in confs.items():
        puntajes = cross_val_score(pipe, textos, etiquetas, groups=participantes, cv=cv, scoring="f1_macro")
        resultados[nombre] = (puntajes.mean(), puntajes.std())
    return resultados
