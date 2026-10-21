"""Servidor del prototipo: expone el modelo validado como API REST local."""
import sys
from pathlib import Path

import joblib
from fastapi import FastAPI
from pydantic import BaseModel

sys.path.append(str(Path(__file__).resolve().parents[2] / "etapa1_corpus"))
from anonimizar import tiene_datos_personales  # noqa: E402

RUTA_MODELO = Path(__file__).resolve().parents[2] / "resultados" / "modelo_seleccionado.joblib"
AVISO = "Resultado de apoyo a la revisión humana; no es una determinación."

app = FastAPI(title="Detección de acoso sexual en relatos")
modelo = joblib.load(RUTA_MODELO) if RUTA_MODELO.exists() else None


class Relato(BaseModel):
    texto: str


@app.post("/predecir")
def predecir(relato: Relato):
    if modelo is None:
        return {"error": "Aún no hay un modelo validado en resultados/."}
    probabilidad = float(modelo.predict_proba([relato.texto])[0][1])
    return {
        "clase": "con acoso sexual" if probabilidad >= 0.5 else "sin acoso sexual",
        "probabilidad": round(probabilidad, 3),
        "posibles_datos_personales": tiene_datos_personales(relato.texto),
        "aviso": AVISO,
    }
