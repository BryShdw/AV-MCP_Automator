"""
Plantilla para el componente <ch5-button> — HTML, CSS y PageAttributes.

RUP Fase: Construccion — Iteracion 3 (Semana 6)
Fuente: docs/01_Inception/05_analisis_forense_cuig.md — Seccion 4: ch5-button

Replica EXACTAMENTE los atributos detectados en el analisis forense del
proyecto "Exercise 1" de Crestron Construct.
"""

# devicesvisited — valor hardcoded del forense (HTML-encoded quotes)
_DEVICES_VISITED_HTML = '[&quot;TST-1080 (Landscape)&quot;]'

# devicesVisited — valor para PageAttributes (escaped quotes)
_DEVICES_VISITED_TOML = '[\\\"TST-1080 (Landscape)\\\"]'


def build_button_html(element_id: str, element: dict) -> str:
    label = element.get("label", "")
    color = element.get("color", "default")
    shape = element.get("shape") or "rounded-rectangle"

    return (
        f'<ch5-button '
        f'id="{element_id}" '
        f'componentname="{label}" '
        f'labelinnerhtml="{label}" '
        f'ccid_label="{label}" '
        f'type="{color}" '
        f'shape="{shape}" '
        f'orientation="horizontal" size="regular" '
        f'halignlabel="center" valignlabel="middle" '
        f'checkboxshow="false" checkboxposition="left" disabled="false" '
        f'clearlabel="false" iconposition="first" '
        f'ccid_imageicontype="iconclass" ccid_linksendreceive="True" '
        f'ccid_syncproperties="syncEnabled" ccid_lastsizeselected="regular" '
        f'customvstheme="custom" affectedbypreviewstate="True" '
        f'ccid_activefont="\'Roboto\'" '
        f'assetid="0" pageflip="0" '
        f'ccid_componenttype="Button" '
        f'devicesvisited="{_DEVICES_VISITED_HTML}">'
        f'</ch5-button>'
    )


def build_button_css(element_id: str, element: dict) -> str:
    x = element["x"]
    y = element["y"]
    w = element["w"]
    h = element["h"]
    text_color = element.get("text_color")
    box_shadow = element.get("box_shadow")

    # Para botones circulares: forzar border-radius aunque el shape lo controle
    # el web component internamente; el CSS lo refuerza para sombras/glow.
    shape = element.get("shape") or "rounded-rectangle"
    br_line = "    border-radius: 50%;\n" if shape == "circle" else ""

    color_line    = f"    color: {text_color};\n"   if text_color else ""
    shadow_line   = f"    box-shadow: {box_shadow};\n" if box_shadow else ""

    return (
        f"  #{element_id} {{\n"
        f"    display: block;\n"
        f"    left: {x}px;\n"
        f"    top: {y}px;\n"
        f"    position: absolute;\n"
        f"    width: {w}px;\n"
        f"    height: {h}px;\n"
        f"{br_line}"
        f"{color_line}"
        f"{shadow_line}"
        f"  }}"
    )


def build_button_page_attributes(element_id: str, element: dict) -> str:
    """
    Genera el bloque [[Elements]] TOML para un ch5-button en {PageAttributes}.

    Incluye [[Elements.Components]] textnode y [Elements.Attributes] completo.
    """
    label = element.get("label", "Button")
    color = element.get("color", "default")
    shape = element.get("shape") or "rounded-rectangle"

    return (
        '[[Elements]]\n'
        'Type = "Ch5 Button"\n'
        'Editable = true\n'
        '\n'
        '[[Elements.Components]]\n'
        'Type = "textnode"\n'
        'Content = "\\n              "\n'
        '\n'
        '[Elements.Attributes]\n'
        f'id = "{element_id}"\n'
        'componentName = "Button"\n'
        f'labelinnerhtml = "{label}"\n'
        f'type = "{color}"\n'
        'orientation = "horizontal"\n'
        f'shape = "{shape}"\n'
        'size = "regular"\n'
        'halignlabel = "center"\n'
        'valignlabel = "middle"\n'
        'ccid_linkSendReceive = "True"\n'
        'ccid_ComponentType = "Button"\n'
        'ccid_syncProperties = "syncEnabled"\n'
        'ccid_lastSizeSelected = "regular"\n'
        'ccid_ActiveFont = "\'Roboto\'"\n'
        f'ccid_Label = "{label}"\n'
        'customVsTheme = "custom"\n'
        f'devicesVisited = "{_DEVICES_VISITED_TOML}"'
    )
