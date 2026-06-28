"""
Plantilla para el componente <ch5-video> en el bloque {Html} del .cuig.
RUP Fase: Construcción — Iteración 3 (Semana 6)
"""


def build_video_html(element_id: str, element: dict) -> str:
    """Genera el fragmento HTML de un <ch5-video>."""
    # TODO (Semana 6): Completar con atributos reales del análisis forense
    return f"""<ch5-video
    id="{element_id}"
    ccid_syncproperties=""
    devicesvisited="">
</ch5-video>"""


def build_video_css(element_id: str, element: dict) -> str:
    """Genera la regla CSS absoluta para posicionar el video."""
    return (
        f"#{element_id} {{"
        f" position:absolute;"
        f" left:{element['x']}px;"
        f" top:{element['y']}px;"
        f" width:{element['w']}px;"
        f" height:{element['h']}px;"
        f" }}"
    )
