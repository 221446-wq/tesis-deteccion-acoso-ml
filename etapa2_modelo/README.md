# Etapa 2: Entrenamiento y selección del modelo (OE2)

CRISP-DM: preparación de los datos y modelado.

1. Partición 80/20 por participante (los relatos de prueba no se tocan hasta la Etapa 3).
2. Línea base léxica (`linea_base_lexica.py`) y línea base mayoritaria.
3. 13 configuraciones (`configuraciones.py`): regresión logística, SVM lineal y Naïve Bayes con TF-IDF, cada uno sin tratamiento, con ponderación de clases y con SMOTE; BETO sin tratamiento y con ponderación.
4. Validación cruzada agrupada de 5 pliegues; se elige la configuración con mayor macro F1.

El vectorizador y SMOTE están dentro del pipeline, así que se ajustan solo con los datos de entrenamiento de cada pliegue (sin fuga de información).
