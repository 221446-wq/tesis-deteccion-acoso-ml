"""Primer filtro automático de anonimización.

Reemplaza correos, teléfonos y códigos de estudiante por marcadores.
No sustituye la revisión manual: nombres propios, cursos o lugares
se revisan a mano antes de usar el relato.
"""
import re

PATRONES = [
    (re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"), "[CORREO]"),
    (re.compile(r"(?:\+?51[\s-]?)?9\d{2}[\s-]?\d{3}[\s-]?\d{3}"), "[TELEFONO]"),
    (re.compile(r"\b\d{6}\b"), "[CODIGO]"),
]


def anonimizar(texto: str) -> str:
    """Devuelve el texto con los datos detectados reemplazados por marcadores."""
    for patron, marcador in PATRONES:
        texto = patron.sub(marcador, texto)
    return texto


def tiene_datos_personales(texto: str) -> bool:
    """Indica si el texto contiene algún dato que el filtro detecta."""
    return any(patron.search(texto) for patron, _ in PATRONES)


if __name__ == "__main__":
    ejemplo = "Me escribió al 987 654 321 y a mi correo ana@gmail.com, código 201234."
    print(anonimizar(ejemplo))
