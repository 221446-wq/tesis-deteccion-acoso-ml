# Etapa 4: Implementación del prototipo (OE4)

CRISP-DM: despliegue (solo en un equipo local).

- `backend/`: API REST con FastAPI que carga el modelo validado y devuelve la predicción, su probabilidad y las palabras más influyentes según SHAP.
- `frontend/`: interfaz en React donde el revisor pega un relato y ve el resultado.

El prototipo no guarda los relatos ni los envía a servicios externos. Muestra siempre un aviso de que el resultado es un apoyo a la revisión humana y no una decisión.

Ejecución del servidor: `uvicorn app:app --host 127.0.0.1 --port 8000` desde `backend/`.
