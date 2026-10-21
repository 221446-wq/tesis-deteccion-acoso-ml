"""Línea base léxica: marca como acoso todo relato que contiene un término de la lista.

La lista se define antes del entrenamiento y no se ajusta con los datos.
"""
import re
import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin


class LineaBaseLexica(BaseEstimator, ClassifierMixin):
    def __init__(self, terminos=()):
        self.terminos = terminos

    def fit(self, X, y=None):
        self.classes_ = np.array([0, 1])
        patron = r"\b(" + "|".join(re.escape(t) for t in self.terminos) + r")\b"
        self._regex = re.compile(patron, re.IGNORECASE)
        return self

    def predict(self, X):
        return np.array([1 if self._regex.search(texto) else 0 for texto in X])
