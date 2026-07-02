"""
Plantilla para el componente <ch5-tab-button> — HTML, CSS y PageAttributes.

RUP Fase: Construccion — Iteracion 4
Fuente: archivo .cuig de prueba con todos los componentes de Crestron Construct.

Componente compuesto: el padre <ch5-tab-button> contiene N
<ch5-tab-button-individual-button>. El forense NO muestra ningun atributo de
texto/label en los sub-botones individuales (ni labelinnerhtml ni
equivalente) — solo 'componentname' y 'componentnumber'. Por eso el texto
visible de cada pestaña probablemente requiera configuracion manual del
ingeniero AV en Construct. Esta plantilla nombra cada sub-boton de forma
descriptiva en 'componentname' (usando los items provistos o un nombre
generico) para que sea facil identificarlos en el arbol del editor, pero
NO promete que el texto se vea automaticamente en el touch panel.

Uso tipico en Pro AV: navegacion tipo pestañas dentro de una misma pagina
(ej. alternar entre "Audio" / "Video" / "Iluminacion").
"""

_DEVICES_VISITED_HTML = '[&quot;TST-1080 (Landscape)&quot;]'
_DEVICES_VISITED_TOML = '[\\\"TST-1080 (Landscape)\\\"]'

_DEFAULT_TAB_COUNT = 3


def _resolve_tab_names(element: dict) -> list[str]:
    """Usa element['tab_items'] si vino del JSON de Gemini; si no, genera
    nombres genericos segun element['tab_count'] (default 3)."""
    items = element.get("tab_items")
    if items:
        return list(items)
    count = element.get("tab_count") or _DEFAULT_TAB_COUNT
    return [f"Individual Button {i}" for i in range(1, count + 1)]


def build_tab_button_html(element_id: str, element: dict) -> str:
    label = element.get("label", "") or "Tab Button"
    names = _resolve_tab_names(element)

    sub_html = "".join(
        f'<ch5-tab-button-individual-button ccid_imageicontype="iconclass" '
        f'componentname="{name}" componentnumber="{i}">'
        f'</ch5-tab-button-individual-button>'
        for i, name in enumerate(names, start=1)
    )

    return (
        f'<ch5-tab-button numberofitems="{len(names)}" '
        f'usecontractforcustomstyle="false" usecontractforcustomclass="false" '
        f'orientation="horizontal" previewstate="buttonnormal" indexid="idx" '
        f'buttonhalignlabel="center" buttonvalignlabel="middle" '
        f'buttoniconposition="first" buttonshape="rounded-rectangle" '
        f'buttontype="default" pd-receivestateenable="" '
        f'pd-receivestateshow="" affectedbypreviewstate="True" '
        f'customvstheme="custom" id="{element_id}" componentname="{label}" '
        f'ccid_activefont="\'Roboto\'" ccid_label="" '
        f'ccid_linksendreceive="True" assetid="0" '
        f'ccid_imageicontype="iconclass" ccid_componenttype="Tab Button" '
        f'devicesvisited="{_DEVICES_VISITED_HTML}">'
        + sub_html +
        f'</ch5-tab-button>'
    )


def build_tab_button_css(element_id: str, element: dict) -> str:
    x = element["x"]
    y = element["y"]
    w = element["w"]
    h = element["h"]

    return (
        f"  #{element_id} .ch5-tab-button :not(i):not(svg) "
        f"{{ font-family: 'Roboto'; }}\n"
        f"  #{element_id} {{\n"
        f"    width: {w}px;\n"
        f"    height: {h}px;\n"
        f"    display: block;\n"
        f"    left: {x}px;\n"
        f"    top: {y}px;\n"
        f"    position: absolute;\n"
        f"    --ch5-tab-button--button-container-width: {w}px;\n"
        f"    --ch5-tab-button--button-container-height: {h}px;\n"
        f"  }}"
    )


def build_tab_button_page_attributes(element_id: str, element: dict) -> str:
    label = element.get("label", "") or "Tab Button"
    names = _resolve_tab_names(element)

    sub_blocks = "".join(
        '[[Elements.Components]]\n'
        'Type = "Ch5 Tab Button Individual Button"\n'
        '\n'
        '[Elements.Components.Attributes]\n'
        'ccid_imageIconType = "iconclass"\n'
        f'componentName = "{name}"\n'
        f'componentNumber = "{i}"\n'
        for i, name in enumerate(names, start=1)
    )

    return (
        '[[Elements]]\n'
        'Type = "Ch5 Tab Button"\n'
        'Editable = true\n'
        '\n'
        + sub_blocks +
        '\n[Elements.Attributes]\n'
        f'numberofitems = "{len(names)}"\n'
        'useContractForCustomStyle = "false"\n'
        'useContractForCustomClass = "false"\n'
        'orientation = "horizontal"\n'
        'previewstate = "buttonnormal"\n'
        'indexid = "idx"\n'
        'buttonhalignlabel = "center"\n'
        'buttonvalignlabel = "middle"\n'
        'buttoniconposition = "first"\n'
        'buttonshape = "rounded-rectangle"\n'
        'buttontype = "default"\n'
        'pd-receivestateenable = ""\n'
        'pd-receivestateshow = ""\n'
        'affectedByPreviewState = "True"\n'
        'customvstheme = "custom"\n'
        f'id = "{element_id}"\n'
        f'componentName = "{label}"\n'
        'ccid_ActiveFont = "\'Roboto\'"\n'
        'ccid_Label = ""\n'
        'ccid_linkSendReceive = "True"\n'
        'assetid = "0"\n'
        'ccid_imageIconType = "iconclass"\n'
        'ccid_ComponentType = "Tab Button"\n'
        f'devicesVisited = "{_DEVICES_VISITED_TOML}"'
    )
