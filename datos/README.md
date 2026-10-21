# Datos

Esta carpeta está vacía a propósito. Los relatos de los estudiantes son información sensible y no se publican, ni siquiera anonimizados.

Estructura que se usará en el equipo local (excluida de Git):

- `crudos/`: relatos tal como llegan del formulario, cifrados.
- `anonimizados/`: relatos sin datos personales, con marcadores como `[PERSONA]` o `[CURSO]`.
- `anotados/`: relatos anonimizados con su etiqueta final (`con acoso sexual` / `sin acoso sexual`) y el identificador del participante.

Formato previsto de `anotados/corpus.csv`:

| columna | descripción |
|---|---|
| `id_relato` | identificador del relato |
| `id_participante` | identificador anónimo del participante (para la partición por participante) |
| `texto` | relato anonimizado |
| `etiqueta` | 1 = con acoso sexual, 0 = sin acoso sexual |
