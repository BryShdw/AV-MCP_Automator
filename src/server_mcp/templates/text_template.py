"""
Plantilla para el componente <ch5-text> — HTML, CSS y PageAttributes.

RUP Fase: Construccion — Iteracion 3 (Semana 6)
Fuente: docs/01_Inception/05_analisis_forense_cuig.md — Seccion 4: ch5-text

Nota: En Crestron, el componentName de ch5-text es "Formatted-Text" (no "Text").
"""

# devicesvisited — valor hardcoded del forense
_DEVICES_VISITED_HTML = '[&quot;TST-1080 (Landscape)&quot;]'
_DEVICES_VISITED_TOML = '[\\\"TST-1080 (Landscape)\\\"]'


def build_text_html(element_id: str, element: dict) -> str:
    """
    Genera el fragmento HTML de un <ch5-text> para el bloque {Html}.

    Args:
        element_id: ID unico generado (ej. "iwiy")
        element:    Dict con label (del JSON de la IA)

    Returns:
        String HTML del componente <ch5-text>
    """
    label = element.get("label", "")

    return (
        f'<ch5-text '
        f'id="{element_id}" '
        f'componentname="{label}" '
        f'clearlabel="false" labelmodeadvncomponent="simple" '
        f'horizontalalignment="center" verticalalignment="middle" '
        f'multilinesupport="false" truncatetext="false" '
        f'ccid_label="{label}" '
        f'labelinnerhtml="{label}" '
        f'ccid_activefont="\'Roboto\'" '
        f'ccid_linksendreceive="True" ccid_componenttype="Formatted-Text" '
        f'ccid_themecssset="true" '
        f'devicesvisited="{_DEVICES_VISITED_HTML}">'
        f'</ch5-text>'
    )


def build_text_css(element_id: str, element: dict) -> str:
    x = element["x"]
    y = element["y"]
    w = element["w"]
    h = element["h"]
    text_color    = element.get("text_color")
    font_size     = element.get("font_size")
    font_weight   = element.get("font_weight")
    letter_spacing = element.get("letter_spacing")

    color_line   = f"    color: {text_color};\n"                if text_color    else ""
    fs_line      = f"    font-size: {font_size}px;\n"           if font_size     else ""
    fw_line      = f"    font-weight: {font_weight};\n"         if font_weight   else ""
    ls_line      = f"    letter-spacing: {letter_spacing}px;\n" if letter_spacing is not None else ""

    return (
        f"  #{element_id} {{\n"
        f"    display: block;\n"
        f"    left: {x}px;\n"
        f"    top: {y}px;\n"
        f"    position: absolute;\n"
        f"    width: {w}px;\n"
        f"    height: {h}px;\n"
        f"{color_line}"
        f"{fs_line}"
        f"{fw_line}"
        f"{ls_line}"
        f"  }}\n"
        f"  #{element_id} :not(i):not(svg) {{ font-family: 'Roboto'; }}"
    )


def build_text_page_attributes(element_id: str, element: dict) -> str:
    """
    Genera el bloque [[Elements]] TOML para un ch5-text en {PageAttributes}.
    """
    label = element.get("label", "label")

    return (
        '[[Elements]]\n'
        'Type = "Ch5 Text"\n'
        'Editable = true\n'
        '\n'
        '[[Elements.Components]]\n'
        'Type = "textnode"\n'
        'Content = "\\n              "\n'
        '\n'
        '[Elements.Attributes]\n'
        'clearlabel = "false"\n'
        'labelmodeadvncomponent = "simple"\n'
        'horizontalalignment = "center"\n'
        'verticalalignment = "middle"\n'
        'multilinesupport = "false"\n'
        'truncatetext = "false"\n'
        f'id = "{element_id}"\n'
        'componentName = "Formatted-Text"\n'
        f'labelinnerhtml = "{label}"\n'
        'ccid_ActiveFont = "\'Roboto\'"\n'
        f'ccid_Label = "{label}"\n'
        'ccid_linkSendReceive = "True"\n'
        'ccid_ComponentType = "Formatted-Text"\n'
        'ccid_themeCssSet = "true"\n'
        f'devicesVisited = "{_DEVICES_VISITED_TOML}"'
    )
