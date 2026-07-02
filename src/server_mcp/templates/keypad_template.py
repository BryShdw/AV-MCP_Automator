"""
Plantilla para el componente <ch5-keypad> — HTML, CSS y PageAttributes.

RUP Fase: Construccion — Iteracion 4
Fuente: archivo .cuig de prueba con todos los componentes de Crestron Construct.

13 sub-botones fijos: digitos 0-9, asterisco, numeral y un boton extra
(icono de telefono, oculto por defecto via showextrabutton="false").
Ninguno lleva id propio: 'key' ya es identificador unico y deterministico.

Uso tipico en Pro AV: marcado de extensiones telefonicas, ingreso de PIN.
"""

_DEVICES_VISITED_HTML = '[&quot;TST-1080 (Landscape)&quot;]'
_DEVICES_VISITED_TOML = '[\\\"TST-1080 (Landscape)\\\"]'

# (key, labelmajor, labelminor) — mapeo estandar de teclado telefonico
_KEYPAD_DIGITS = [
    ("button1", "1", ""),
    ("button2", "2", "ABC"),
    ("button3", "3", "DEF"),
    ("button4", "4", "GHI"),
    ("button5", "5", "JKL"),
    ("button6", "6", "MNO"),
    ("button7", "7", "PQRS"),
    ("button8", "8", "TUV"),
    ("button9", "9", "WXYZ"),
    ("button0", "0", "+"),
]


def build_keypad_html(element_id: str, element: dict) -> str:
    label = element.get("label", "") or "Keypad"

    sub_html = [
        f'<ch5-keypad-button pressed="false" key="{key}" '
        f'labelmajor="{major}" labelminor="{minor}" '
        f'componentname="{key}"></ch5-keypad-button>'
        for key, major, minor in _KEYPAD_DIGITS
    ]
    sub_html.append(
        '<ch5-keypad-button pressed="false" key="buttonstar" '
        'labelmajor="*" componentname="buttonstar" labelminor="">'
        '</ch5-keypad-button>'
    )
    sub_html.append(
        '<ch5-keypad-button pressed="false" key="buttonhash" '
        'labelmajor="#" componentname="buttonhash" labelminor="">'
        '</ch5-keypad-button>'
    )
    sub_html.append(
        '<ch5-keypad-button pressed="false" key="buttonextra" '
        'iconclass="fas fa-phone" componentname="buttonextra" '
        'labelmajor="" labelminor=""></ch5-keypad-button>'
    )

    return (
        f'<ch5-keypad shape="rounded-rectangle" type="default" indexid="idx" '
        f'usecontractforcustomstyle="false" usecontractforcustomclass="false" '
        f'usecontractforenable="false" usecontractforshow="false" '
        f'affectedbypreviewstate="True" '
        f'usecontractforhideasteriskbutton="false" '
        f'usecontractforhidepoundbutton="false" textorientation="top" '
        f'disabled="false" showextrabutton="false" customvstheme="custom" '
        f'hideasteriskbutton="false" hidepoundbutton="false" '
        f'id="{element_id}" componentname="{label}" '
        f'ccid_activefont="\'Roboto\'" ccid_linksendreceive="True" '
        f'ccid_componenttype="Keypad" devicesvisited="{_DEVICES_VISITED_HTML}" '
        f'ccid_customsizeset size="custom">'
        + "".join(sub_html) +
        f'</ch5-keypad>'
    )


def build_keypad_css(element_id: str, element: dict) -> str:
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
        f"    --ch5-keypad--regular-container-width: {w}px;\n"
        f"  }}\n"
        f"  #{element_id} span:not(.has-icon, .has-icon span) "
        f"{{ font-family: 'Roboto'; }}"
    )


def build_keypad_page_attributes(element_id: str, element: dict) -> str:
    label = element.get("label", "") or "Keypad"

    sub_blocks = [
        '[[Elements.Components]]\n'
        'Type = "Ch5 Keypad Button"\n'
        'Editable = true\n'
        '\n'
        '[Elements.Components.Attributes]\n'
        'pressed = "false"\n'
        f'key = "{key}"\n'
        f'labelmajor = "{major}"\n'
        f'labelminor = "{minor}"\n'
        f'componentName = "{key}"\n'
        for key, major, minor in _KEYPAD_DIGITS
    ]
    sub_blocks.append(
        '[[Elements.Components]]\n'
        'Type = "Ch5 Keypad Button"\n'
        'Editable = true\n'
        '\n'
        '[Elements.Components.Attributes]\n'
        'pressed = "false"\n'
        'key = "buttonstar"\n'
        'labelmajor = "*"\n'
        'componentName = "buttonstar"\n'
        'labelminor = ""\n'
    )
    sub_blocks.append(
        '[[Elements.Components]]\n'
        'Type = "Ch5 Keypad Button"\n'
        'Editable = true\n'
        '\n'
        '[Elements.Components.Attributes]\n'
        'pressed = "false"\n'
        'key = "buttonhash"\n'
        'labelmajor = "#"\n'
        'componentName = "buttonhash"\n'
        'labelminor = ""\n'
    )
    sub_blocks.append(
        '[[Elements.Components]]\n'
        'Type = "Ch5 Keypad Button"\n'
        'Editable = true\n'
        '\n'
        '[Elements.Components.Attributes]\n'
        'pressed = "false"\n'
        'key = "buttonextra"\n'
        'iconclass = "fas fa-phone"\n'
        'componentName = "buttonextra"\n'
        'labelmajor = ""\n'
        'labelminor = ""\n'
    )

    return (
        '[[Elements]]\n'
        'Type = "Ch5 Keypad"\n'
        'Editable = true\n'
        '\n'
        '[[Elements.Components]]\n'
        'Type = "textnode"\n'
        'Content = "\\n              "\n'
        + "".join(sub_blocks) +
        '\n[Elements.Attributes]\n'
        'shape = "rounded-rectangle"\n'
        'type = "default"\n'
        'indexid = "idx"\n'
        'useContractForCustomStyle = "false"\n'
        'useContractForCustomClass = "false"\n'
        'useContractForEnable = "false"\n'
        'useContractForShow = "false"\n'
        'affectedByPreviewState = "True"\n'
        'useContractForHideAsteriskButton = "false"\n'
        'useContractForHidePoundButton = "false"\n'
        'textorientation = "top"\n'
        'disabled = "false"\n'
        'showextrabutton = "false"\n'
        'customvstheme = "custom"\n'
        'hideasteriskbutton = "false"\n'
        'hidepoundbutton = "false"\n'
        f'id = "{element_id}"\n'
        f'componentName = "{label}"\n'
        'ccid_ActiveFont = "\'Roboto\'"\n'
        'ccid_linkSendReceive = "True"\n'
        'ccid_ComponentType = "Keypad"\n'
        f'devicesVisited = "{_DEVICES_VISITED_TOML}"\n'
        'ccid_customSizeSet = "true"\n'
        'size = "custom"'
    )
