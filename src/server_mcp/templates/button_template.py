"""
Plantilla para el componente <ch5-button> en el bloque {Html} del .cuig.
RUP Fase: Construcción — Iteración 3 (Semana 6)

IMPORTANTE: Los valores de ccid_* y atributos internos deben ajustarse
con los valores reales detectados en el análisis forense (Semana 1).
"""


def build_button_html(element_id: str, element: dict) -> str:
    """
    Genera el fragmento HTML de un <ch5-button> para el bloque {Html}.

    Args:
        element_id: ID único generado por el Builder_Tool (ej. "i1l4")
        element:    Dict con label, color, join_digital (opcional)

    Returns:
        String HTML del componente <ch5-button>
    """
    label = element.get("label", "Botón")
    color = element.get("color", "default")
    join = element.get("join_digital", 0)

    # TODO (Semana 6): Reemplazar atributos ccid_* con valores reales del forense
    return f"""<ch5-button
    id="{element_id}"
    label="{label}"
    type="{color}"
    sendeventonclick="d{join}"
    ccid_syncproperties=""
    devicesvisited="">
</ch5-button>"""


def build_button_css(element_id: str, element: dict) -> str:
    """Genera la regla CSS absoluta para posicionar el botón en el canvas."""
    return (
        f"#{element_id} {{"
        f" position:absolute;"
        f" left:{element['x']}px;"
        f" top:{element['y']}px;"
        f" width:{element['w']}px;"
        f" height:{element['h']}px;"
        f" }}"
    )
