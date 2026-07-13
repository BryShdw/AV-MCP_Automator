"""
Plantilla para el componente <ch5-toggle> — HTML, CSS y PageAttributes.

RUP Fase: Construccion — Iteracion 3 (Semana 6)
Fuente: docs/01_Inception/05_analisis_forense_cuig.md — Seccion 4: ch5-toggle

Toggle es un boton on/off estilo switch, distinto al ch5-button.
"""

# devicesvisited — valor hardcoded del forense
_DEVICES_VISITED_HTML = '[&quot;TST-1080 (Landscape)&quot;]'
_DEVICES_VISITED_TOML = '[\\\"TST-1080 (Landscape)\\\"]'


def build_toggle_html(element_id: str, element: dict) -> str:
    """
    Genera el fragmento HTML de un <ch5-toggle> para el bloque {Html}.

    Args:
        element_id: ID unico generado (ej. "ihlc")
        element:    Dict del JSON de la IA

    Returns:
        String HTML del componente <ch5-toggle>
    """
    return (
        f'<ch5-toggle '
        f'id="{element_id}" '
        f'componentname="Toggle" '
        f'ccid_label="" '
        f'handleshape="circle" orientation="horizontal" size="regular" '
        f'value="false" customvstheme="custom" '
        f'ccid_activefont="\'Roboto\'" '
        f'ccid_linksendreceive="True" ccid_componenttype="Toggle" '
        f'devicesvisited="{_DEVICES_VISITED_HTML}">'
        f'</ch5-toggle>'
    )


def build_toggle_css(element_id: str, element: dict) -> str:
    """
    Genera las reglas CSS para posicionar el toggle.
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
        f"  }}"
    )


def build_toggle_page_attributes(element_id: str, element: dict) -> str:
    """
    Genera el bloque [[Elements]] TOML para un ch5-toggle en {PageAttributes}.
    """
    return (
        '[[Elements]]\n'
        'Type = "Ch5 Toggle"\n'
        'Editable = true\n'
        '\n'
        '[[Elements.Components]]\n'
        'Type = "textnode"\n'
        'Content = "\\n              "\n'
        '\n'
        '[Elements.Attributes]\n'
        'handleShape = "circle"\n'
        'orientation = "horizontal"\n'
        'size = "regular"\n'
        'value = "false"\n'
        'customVsTheme = "custom"\n'
        f'id = "{element_id}"\n'
        'componentName = "Toggle"\n'
        'ccid_ActiveFont = "\'Roboto\'"\n'
        'ccid_Label = ""\n'
        'ccid_linkSendReceive = "True"\n'
        'ccid_ComponentType = "Toggle"\n'
        f'devicesVisited = "{_DEVICES_VISITED_TOML}"'
    )
