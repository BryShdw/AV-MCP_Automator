"""
Plantilla para el componente <ch5-image> — HTML, CSS y PageAttributes.

RUP Fase: Construccion — Iteracion 4
Fuente: archivo .cuig de prueba con todos los componentes de Crestron Construct.

Componente simple, sin sub-elementos. No renderiza texto — 'label' solo
se usa como nombre interno (componentname) para identificarlo en el arbol
de Crestron Construct. El asset/imagen real se asigna manualmente en
Construct (assetid="0" es el placeholder por defecto).

Uso tipico en Pro AV: logo de la sala/empresa, iconografia personalizada.
"""

_DEVICES_VISITED_HTML = '[&quot;TST-1080 (Landscape)&quot;]'
_DEVICES_VISITED_TOML = '[\\\"TST-1080 (Landscape)\\\"]'


def build_image_html(element_id: str, element: dict) -> str:
    label = element.get("label", "") or "Image"

    return (
        f'<ch5-image numberofmodes="0" customvstheme="custom" '
        f'refreshrate="0" allowpositiondatatobesent="false" '
        f'allowvaluesonmove="false" assetid="0" '
        f'id="{element_id}" componentname="{label}" '
        f'ccid_linksendreceive="True" ccid_componenttype="Image" '
        f'devicesvisited="{_DEVICES_VISITED_HTML}">'
        f'</ch5-image>'
    )


def build_image_css(element_id: str, element: dict) -> str:
    x = element["x"]
    y = element["y"]
    w = element["w"]
    h = element["h"]

    return (
        f"  #{element_id} {{\n"
        f"    width: {w}px;\n"
        f"    height: {h}px;\n"
        f"    overflow: hidden;\n"
        f"    display: block;\n"
        f"    left: {x}px;\n"
        f"    top: {y}px;\n"
        f"    position: absolute;\n"
        f"  }}"
    )


def build_image_page_attributes(element_id: str, element: dict) -> str:
    label = element.get("label", "") or "Image"

    return (
        '[[Elements]]\n'
        'Type = "Ch5 Image"\n'
        'Editable = true\n'
        '\n'
        '[[Elements.Components]]\n'
        'Type = "textnode"\n'
        'Content = "\\n              "\n'
        '\n'
        '[Elements.Attributes]\n'
        'numberofmodes = "0"\n'
        'customvstheme = "custom"\n'
        'refreshrate = "0"\n'
        'allowpositiondatatobesent = "false"\n'
        'allowvaluesonmove = "false"\n'
        'assetid = "0"\n'
        f'id = "{element_id}"\n'
        f'componentName = "{label}"\n'
        'ccid_linkSendReceive = "True"\n'
        'ccid_ComponentType = "Image"\n'
        f'devicesVisited = "{_DEVICES_VISITED_TOML}"'
    )
