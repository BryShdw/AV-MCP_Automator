"""
Plantilla para el componente <ch5-dpad> — HTML, CSS y PageAttributes.

RUP Fase: Construccion — Iteracion 4
Fuente: archivo .cuig de prueba con todos los componentes de Crestron Construct.

El Dpad es un componente compuesto: SIEMPRE tiene 5 sub-botones fijos
(Up, Down, Left, Right, Center). Sus sub-elementos no llevan id propio —
se identifican por su atributo 'key', que es deterministico. Ver nota de
diseño al inicio de este prompt sobre por que se evitan ids aleatorios
en sub-elementos compuestos.

Uso tipico en Pro AV: control PTZ de camara, navegacion de menus on-screen.
"""

_DEVICES_VISITED_HTML = '[&quot;TST-1080 (Landscape)&quot;]'
_DEVICES_VISITED_TOML = '[\\\"TST-1080 (Landscape)\\\"]'

# (componentname, key, iconclass o None para el boton central)
_DPAD_BUTTONS = [
    ("Up",     "up",     "fas fa-caret-up"),
    ("Down",   "down",   "fas fa-caret-down"),
    ("Left",   "left",   "fas fa-caret-left"),
    ("Right",  "right",  "fas fa-caret-right"),
    ("Center", "center", None),
]


def build_dpad_html(element_id: str, element: dict) -> str:
    label = element.get("label", "") or "Dpad"

    sub_html = []
    for name, key, icon in _DPAD_BUTTONS:
        if icon:
            sub_html.append(
                f'<ch5-dpad-button componentname="{name}" key="{key}" '
                f'iconclass="{icon}" ccid_imageicontype="iconclass">'
                f'</ch5-dpad-button>'
            )
        else:
            sub_html.append(
                f'<ch5-dpad-button componentname="{name}" key="{key}" '
                f'ccid_imageicontype="iconclass" '
                f'ccid_activefont="\'Roboto\'"></ch5-dpad-button>'
            )

    return (
        f'<ch5-dpad shape="plus" type="default" hidecenterbutton="false" '
        f'disablecenterbutton="false" customvstheme="custom" '
        f'id="{element_id}" componentname="{label}" '
        f'ccid_linksendreceive="True" ccid_componenttype="Dpad" '
        f'devicesvisited="{_DEVICES_VISITED_HTML}" '
        f'ccid_customsizeset size="custom">'
        + "".join(sub_html) +
        f'</ch5-dpad>'
    )


def build_dpad_css(element_id: str, element: dict) -> str:
    x = element["x"]
    y = element["y"]
    w = element["w"]
    h = element["h"]
    side = min(w, h)

    return (
        f"  #{element_id} {{\n"
        f"    display: block;\n"
        f"    left: {x}px;\n"
        f"    top: {y}px;\n"
        f"    position: absolute;\n"
        f"    width: {w}px;\n"
        f"    height: {h}px;\n"
        f"    --ch5-dpad--regular-size: {side}px;\n"
        f"  }}\n"
        f"  #{element_id} span:not(.dpad-btn-icon) {{ font-family: 'Roboto'; }}"
    )


def build_dpad_page_attributes(element_id: str, element: dict) -> str:
    label = element.get("label", "") or "Dpad"

    sub_blocks = []
    for name, key, icon in _DPAD_BUTTONS:
        if icon:
            sub_blocks.append(
                '[[Elements.Components]]\n'
                'Type = "Ch5 Dpad Button"\n'
                '\n'
                '[Elements.Components.Attributes]\n'
                f'componentName = "{name}"\n'
                f'key = "{key}"\n'
                f'iconclass = "{icon}"\n'
                'pressed = "false"\n'
                'ccid_imageIconType = "iconclass"\n'
            )
        else:
            sub_blocks.append(
                '[[Elements.Components]]\n'
                'Type = "Ch5 Dpad Button"\n'
                '\n'
                '[Elements.Components.Attributes]\n'
                f'componentName = "{name}"\n'
                f'key = "{key}"\n'
                'pressed = "false"\n'
                'ccid_imageIconType = "iconclass"\n'
                'ccid_ActiveFont = "\'Roboto\'"\n'
            )

    return (
        '[[Elements]]\n'
        'Type = "Ch5 Dpad"\n'
        'Editable = true\n'
        '\n'
        '[[Elements.Components]]\n'
        'Type = "textnode"\n'
        'Content = "\\n              "\n'
        + "".join(sub_blocks) +
        '\n[Elements.Attributes]\n'
        'shape = "plus"\n'
        'type = "default"\n'
        'useContractForCustomStyle = "false"\n'
        'useContractForCustomClass = "false"\n'
        'useContractForEnable = "false"\n'
        'useContractForShow = "false"\n'
        'hidecenterbutton = "false"\n'
        'disablecenterbutton = "false"\n'
        'customvstheme = "custom"\n'
        f'id = "{element_id}"\n'
        f'componentName = "{label}"\n'
        'disabled = "false"\n'
        'ccid_linkSendReceive = "True"\n'
        'ccid_ComponentType = "Dpad"\n'
        f'devicesVisited = "{_DEVICES_VISITED_TOML}"\n'
        'ccid_customSizeSet = "true"\n'
        'size = "custom"'
    )
