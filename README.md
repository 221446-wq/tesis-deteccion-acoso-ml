# Desarrollo de un modelo de aprendizaje automático para la detección de acoso sexual en relatos de estudiantes de la UNSAAC

Repositorio del plan de tesis de **Pamela Diaz Misme** (ORCID [0009-0006-8710-4858](https://orcid.org/0009-0006-8710-4858)).
Escuela Profesional de Ingeniería Informática y de Sistemas, Universidad Nacional de San Antonio Abad del Cusco.
Asesor: Dr. Rony Villafuerte Serna.

## De qué trata

En la UNSAAC, casi ninguna experiencia de hostigamiento sexual llega a denunciarse. Este proyecto propone un modelo que, a partir de un relato escrito por un estudiante, indique si describe o no una situación de acoso sexual. El modelo se compara con una línea base léxica (búsqueda de palabras clave) y se integra en un prototipo de apoyo a la revisión humana.

## Metodología

El desarrollo sigue **CRISP-DM**, organizado en cuatro etapas, una por cada objetivo específico. Cada etapa tiene su propia carpeta en este repositorio.

| Carpeta | Objetivo específico | Etapas de CRISP-DM | Producto |
|---|---|---|---|
| `etapa1_corpus/` | OE1: construir el corpus anonimizado y anotado | Comprensión del problema y de los datos, preparación | Corpus anotado, kappa de Cohen, hoja de datos |
| `etapa2_modelo/` | OE2: entrenar y seleccionar el modelo | Preparación de los datos y modelado | Modelo seleccionado y registro de experimentos |
| `etapa3_validacion/` | OE3: validar el modelo frente a la línea base | Evaluación | Métricas, prueba de McNemar y análisis de errores |
| `etapa4_prototipo/` | OE4: implementar el prototipo | Despliegue | Prototipo (FastAPI + React) y ficha del modelo |

**Diseño:** experimental computacional factorial con medidas repetidas. Se comparan 13 configuraciones (regresión logística, SVM lineal y Naïve Bayes con TF-IDF; BETO; con y sin tratamiento del desbalance) y dos líneas base, todas sobre los mismos relatos de prueba.

**Evaluación:** macro F1, precisión, exhaustividad, kappa de Cohen, prueba de McNemar con ajuste de Holm e intervalos de confianza por *bootstrap*. Partición 80/20 por participante y validación cruzada agrupada de cinco pliegues, para evitar la fuga de información.

## Estructura

```
├── docs/
│   ├── plan-tesis/          Plan de tesis (PDF y fuente LaTeX)
│   └── presentacion/        Presentación del plan
├── datos/                   Vacía a propósito: los relatos NO se publican
├── etapa1_corpus/           Anonimización y acuerdo entre anotadores
├── etapa2_modelo/           Líneas base y configuraciones de los modelos
├── etapa3_validacion/       Métricas y pruebas estadísticas
├── etapa4_prototipo/        Servidor (FastAPI) e interfaz (React)
├── resultados/              Métricas y registros de experimentos
└── requirements.txt         Dependencias del entorno de pruebas
```

## Estado

Plan de tesis en revisión. El código de las etapas es la base inicial; se completará durante la ejecución, después de la aprobación ética.

## Privacidad

Los relatos son información sensible. **Ningún relato, real o anonimizado, se sube a este repositorio.** La carpeta `datos/` solo contiene su descripción, y el archivo `.gitignore` impide subir su contenido. Todo el procesamiento se hace en un equipo local.

## Entorno

Python 3.11, scikit-learn 1.5, imbalanced-learn 0.12, PyTorch 2.4, Transformers 4.44, SHAP 0.46, FastAPI 0.115 y React 18. Ver `requirements.txt`.
