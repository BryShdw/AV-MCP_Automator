"""
Plantilla para el componente <ch5-video> — HTML, CSS y PageAttributes.

RUP Fase: Construccion — Iteracion 3 (Semana 6)
Fuente: docs/01_Inception/05_analisis_forense_cuig.md — Seccion 4: ch5-video

El video usa height:auto y tiene una regla CSS extra para .ch5-video.
"""

# devicesvisited — valor hardcoded del forense
_DEVICES_VISITED_HTML = '[&quot;TST-1080 (Landscape)&quot;]'
_DEVICES_VISITED_TOML = '[\\\"TST-1080 (Landscape)\\\"]'


def build_video_html(element_id: str, element: dict) -> str:
    """
    Genera el fragmento HTML de un <ch5-video> para el bloque {Html}.

    Args:
        element_id: ID unico generado (ej. "ih6z")
        element:    Dict del JSON de la IA

    Returns:
        String HTML del componente <ch5-video>
    """
    label = element.get("label", "")

    return (
        f'<ch5-video '
        f'id="{element_id}" '
        f'componentname="{label}" '
        f'aspectratio="16:9" sourcetype="Network" snapshotrefreshrate="5" '
        f'size="regular" '
        f'ccid_linksendreceive="True" ccid_componenttype="Video" '
        f'devicesvisited="{_DEVICES_VISITED_HTML}">'
        f'</ch5-video>'
    )


def build_video_css(element_id: str, element: dict) -> str:
    """
    Genera las reglas CSS para posicionar el video.

    Segun el forense, el video usa height:auto (no el h del JSON)
    y tiene una regla extra para .ch5-video { display:block; }.
    """
    x = element["x"]
    y = element["y"]
    w = element["w"]

    return (
        f"  #{element_id} {{\n"
        f"    display: block;\n"
        f"    left: {x}px;\n"
        f"    top: {y}px;\n"
        f"    position: absolute;\n"
        f"    width: {w}px;\n"
        f"    height: auto;\n"
        f"  }}\n"
        f"  #{element_id} .ch5-video {{ display: block; }}"
    )


def build_video_page_attributes(element_id: str, element: dict) -> str:
    """
    Genera el bloque [[Elements]] TOML para un ch5-video en {PageAttributes}.
    """
    return (
        '[[Elements]]\n'
        'Type = "Ch5 Video"\n'
        'Editable = true\n'
        '\n'
        '[[Elements.Components]]\n'
        'Type = "textnode"\n'
        'Content = "\\n              "\n'
        '\n'
        '[Elements.Attributes]\n'
        'aspectRatio = "16:9"\n'
        'sourceType = "Network"\n'
        'snapshotRefreshRate = "5"\n'
        'size = "regular"\n'
        f'id = "{element_id}"\n'
        'componentName = "Video"\n'
        'ccid_linkSendReceive = "True"\n'
        'ccid_ComponentType = "Video"\n'
        f'devicesVisited = "{_DEVICES_VISITED_TOML}"'
    )
