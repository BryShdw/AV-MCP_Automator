"""
Plantilla para el componente <ch5-segmented-gauge> — HTML, CSS y PageAttributes.

RUP Fase: Construccion — Iteracion 4
Fuente: archivo .cuig de prueba con todos los componentes de Crestron Construct.

Uso tipico en Pro AV: medidor de nivel (volumen, señal, etc).
"""

_DEVICES_VISITED_HTML = '[&quot;TST-1080 (Landscape)&quot;]'
_DEVICES_VISITED_TOML = '[\\\"TST-1080 (Landscape)\\\"]'


def build_gauge_html(element_id: str, element: dict) -> str:
    label = element.get("label", "") or "Segmented Gauge"

    return (
        f'<ch5-segmented-gauge '
        f'primarystategraphic="green" secondarystategraphic="yellow" '
        f'tertiarystategraphic="red" orientation="horizontal" '
        f'touchsettable="true" value="0" minvalue="0" maxvalue="65535" '
        f'gaugeledstyle="rectangle" numberofsegments="20" '
        f'id="{element_id}" componentname="{label}" '
        f'ccid_linksendreceive="True" ccid_componenttype="Segmented Gauge" '
        f'devicesvisited="{_DEVICES_VISITED_HTML}">'
        f'</ch5-segmented-gauge>'
    )


def build_gauge_css(element_id: str, element: dict) -> str:
    w = element["w"]
    h = element["h"]
    x = element["x"]
    y = element["y"]

    return (
        f"  #{element_id} {{\n"
        f"    display: default;\n"
        f"    left: {x}px;\n"
        f"    top: {y}px;\n"
        f"    position: absolute;\n"
        f"    width: {w}px;\n"
        f"    height: {h}px;\n"
        f"  }}\n"
        f"  #{element_id} .ch5-segmented-gauge {{ display: flex; }}"
    )


def build_gauge_page_attributes(element_id: str, element: dict) -> str:
    label = element.get("label", "") or "Segmented Gauge"

    return (
        '[[Elements]]\n'
        'Type = "Ch5 Segmented Gauge"\n'
        'Editable = true\n'
        '\n'
        '[[Elements.Components]]\n'
        'Type = "textnode"\n'
        'Content = "\\n              "\n'
        '\n'
        '[Elements.Attributes]\n'
        'primarystategraphic = "green"\n'
        'secondarystategraphic = "yellow"\n'
        'tertiarystategraphic = "red"\n'
        'orientation = "horizontal"\n'
        'touchsettable = "true"\n'
        'value = "0"\n'
        'minvalue = "0"\n'
        'maxvalue = "65535"\n'
        'gaugeledstyle = "rectangle"\n'
        'numberofsegments = "20"\n'
        f'id = "{element_id}"\n'
        f'componentName = "{label}"\n'
        'ccid_linkSendReceive = "True"\n'
        'ccid_ComponentType = "Segmented Gauge"\n'
        f'devicesVisited = "{_DEVICES_VISITED_TOML}"'
    )
