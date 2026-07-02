"""
Plantilla para el componente <ch5-slider> — HTML, CSS y PageAttributes.

RUP Fase: Construccion — Iteracion 3 (Semana 6)
Fuente: docs/01_Inception/05_analisis_forense_cuig.md — Seccion 4: ch5-slider

Replica EXACTAMENTE los atributos detectados en el analisis forense.
El slider tiene CSS adicional para .noUi-touch-area y font-family.
"""

# devicesvisited — valor hardcoded del forense
_DEVICES_VISITED_HTML = '[&quot;TST-1080 (Landscape)&quot;]'
_DEVICES_VISITED_TOML = '[\\\"TST-1080 (Landscape)\\\"]'


def build_slider_html(element_id: str, element: dict) -> str:
    """
    Genera el fragmento HTML de un <ch5-slider> para el bloque {Html}.

    Args:
        element_id: ID unico generado (ej. "i2e3i")
        element:    Dict con label (del JSON de la IA)

    Returns:
        String HTML del componente <ch5-slider>
    """
    label = element.get("label", "")
    join  = element.get("join_analog", 0)

    return (
        f'<ch5-slider '
        f'id="{element_id}" '
        f'componentname="{label}" '
        f'nohandle="false" size="regular" orientation="horizontal" '
        f'tapsettable="false" handleshape="rounded-rectangle" handlesize="regular" '
        f'tooltipshowtype="off" tooltipdisplaytype="%" '
        f'value="50" slidertype="fader" customvstheme="custom" '
        f'min="0" max="100" step="1" '
        f'ccid_linksendreceive="True" ccid_componenttype="Slider" '
        f'devicesvisited="{_DEVICES_VISITED_HTML}">'
        f'</ch5-slider>'
    )


def build_slider_css(element_id: str, element: dict) -> str:
    """
    Genera las reglas CSS para posicionar el slider.

    El slider tiene 3 reglas CSS segun el forense:
    1. Posicion absoluta base
    2. .noUi-touch-area padding
    3. Font-family Roboto
    """
    x = element["x"]
    y = element["y"]
    w = element["w"]
    h = element["h"]

    return (
        f"  #{element_id} {{\n"
        f"    display: block;\n"
        f"    left: {x}px;\n"
        f"    top: {y}px;\n"
        f"    position: absolute;\n"
        f"    width: {w}px;\n"
        f"    height: {h}px;\n"
        f"  }}\n"
        f"  #{element_id} .noUi-touch-area {{ slidertouchareapadding_padding: 0px; }}\n"
        f"  #{element_id} .ch5-slider :not(i):not(svg) {{ font-family: Roboto; }}"
    )


def build_slider_page_attributes(element_id: str, element: dict) -> str:
    """
    Genera el bloque [[Elements]] TOML para un ch5-slider en {PageAttributes}.

    Incluye atributos especificos del slider (min, max, step, value, etc.)
    detectados en el analisis forense.
    """
    return (
        '[[Elements]]\n'
        'Type = "Ch5 Slider"\n'
        'Editable = true\n'
        '\n'
        '[[Elements.Components]]\n'
        'Type = "textnode"\n'
        'Content = "\\n              "\n'
        '\n'
        '[Elements.Attributes]\n'
        'nohandle = "false"\n'
        'size = "regular"\n'
        'orientation = "horizontal"\n'
        'value = "50"\n'
        'min = "0"\n'
        'max = "100"\n'
        'step = "1"\n'
        f'id = "{element_id}"\n'
        'componentName = "Slider"\n'
        'ccid_linkSendReceive = "True"\n'
        'ccid_ComponentType = "Slider"\n'
        f'devicesVisited = "{_DEVICES_VISITED_TOML}"'
    )
