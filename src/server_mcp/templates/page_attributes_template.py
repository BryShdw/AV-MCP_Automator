"""
Plantilla para el bloque {PageAttributes} del archivo .cuig.
RUP Fase: Construcción — Iteración 3 (Semana 6)

El formato TOML/INI exacto debe determinarse en el análisis forense (Semana 1).
"""


def build_page_attributes_block(elements_with_ids: list[dict]) -> str:
    """
    Genera el bloque {PageAttributes} que indexa todos los componentes de la página.

    Args:
        elements_with_ids: Lista de dicts con 'id', 'type' y propiedades del elemento

    Returns:
        String con el bloque {PageAttributes} completo
    """
    # TODO (Semana 6): Completar con el formato exacto del análisis forense
    lines = ["{PageAttributes}"]
    for el in elements_with_ids:
        lines.append(f"[{el['id']}]")
        lines.append(f"type={el['type']}")
        lines.append(f"label={el.get('label', '')}")
    lines.append("{/PageAttributes}")
    return "\n".join(lines)
