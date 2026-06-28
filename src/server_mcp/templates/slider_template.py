"""
Plantilla para el componente <ch5-slider> en el bloque {Html} del .cuig.
RUP Fase: Construcción — Iteración 3 (Semana 6)
"""


def build_slider_html(element_id: str, element: dict) -> str:
    """Genera el fragmento HTML de un <ch5-slider>."""
    label = element.get("label", "Control")
    join = element.get("join_analog", 0)

    # TODO (Semana 6): Ajustar con atributos ccid_* reales del análisis forense
    return f"""<ch5-slider
    id="{element_id}"
    label="{label}"
    receivestatefeedback="a{join}"
    sendeventonchange="a{join}"
    ccid_syncproperties=""
    devicesvisited="">
</ch5-slider>"""


def build_slider_css(element_id: str, element: dict) -> str:
    """Genera la regla CSS absoluta para posicionar el slider."""
    return (
        f"#{element_id} {{"
        f" position:absolute;"
        f" left:{element['x']}px;"
        f" top:{element['y']}px;"
        f" width:{element['w']}px;"
        f" height:{element['h']}px;"
        f" }}"
    )
