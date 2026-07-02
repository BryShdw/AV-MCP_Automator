"""
Plantilla para el componente <ch5-video-switcher> — HTML, CSS y PageAttributes.

RUP Fase: Construccion — Iteracion 4
Fuente: archivo .cuig de prueba con todos los componentes de Crestron Construct.

Componente compuesto: contiene N <ch5-video-switcher-source> y M
<ch5-video-switcher-screen>. A diferencia de Dpad/Keypad/Tab Button, sus
sub-elementos SI llevan id, pero son predecibles ('Source1', 'Screen1' —
no hex aleatorio), asi que generarlos de forma independiente en html/css/
page_attributes es seguro: ambas funciones calculan el mismo string.

Uso tipico en Pro AV: matrices de conmutacion (elegir que fuente va a que
pantalla) en salas de control o auditorios con multiples displays.
"""

_DEVICES_VISITED_HTML = '[&quot;TST-1080 (Landscape)&quot;]'
_DEVICES_VISITED_TOML = '[\\\"TST-1080 (Landscape)\\\"]'

_DEFAULT_SOURCE_COUNT = 5
_DEFAULT_SCREEN_COUNT = 2


def build_video_switcher_html(element_id: str, element: dict) -> str:
    label = element.get("label", "") or "Video Switcher"
    n_sources = element.get("source_count") or _DEFAULT_SOURCE_COUNT
    n_screens = element.get("screen_count") or _DEFAULT_SCREEN_COUNT

    sources_html = "".join(
        f'<ch5-video-switcher-source ccid_imageicontype="iconclass" '
        f'id="Source{i}" componentname="Source {i}" componentnumber="{i}">'
        f'</ch5-video-switcher-source>'
        for i in range(1, n_sources + 1)
    )
    screens_html = "".join(
        f'<ch5-video-switcher-screen id="Screen{i}" '
        f'componentname="Screen {i}" componentnumber="{i}" '
        f'alignlabel="center"></ch5-video-switcher-screen>'
        for i in range(1, n_screens + 1)
    )

    return (
        f'<ch5-video-switcher numberofsources="{n_sources}" '
        f'numberofsourcelistdivisions="1" numberofscreens="{n_screens}" '
        f'displayscreenlabel="true" numberofscreencolumns="0" indexid="idx" '
        f'scrollbar="true" screenaspectratio="stretch" '
        f'sourcelistposition="top" ccid_linksendreceive="True" '
        f'sourceiconclass="fas fa-video" ccid_imageicontype="iconclass" '
        f'endless="false" id="{element_id}" componentname="{label}" '
        f'ccid_activefont="\'Roboto\'" assetid="0" '
        f'ccid_componenttype="Video Switcher" '
        f'devicesvisited="{_DEVICES_VISITED_HTML}">'
        + sources_html + screens_html +
        f'</ch5-video-switcher>'
    )


def build_video_switcher_css(element_id: str, element: dict) -> str:
    x = element["x"]
    y = element["y"]
    w = element["w"]

    return (
        f"  #{element_id} {{\n"
        f"    width: {w}px;\n"
        f"    height: auto;\n"
        f"    display: block;\n"
        f"    left: {x}px;\n"
        f"    top: {y}px;\n"
        f"    position: absolute;\n"
        f"    --ch5-video-switcher--width: {w}px;\n"
        f"  }}\n"
        f"  #{element_id} .ch5-video-switcher :not(i):not(svg) "
        f"{{ font-family: 'Roboto'; }}\n"
        f"  #{element_id} .ch5-video-switcher--source-list "
        f".source-container {{ width: 68px; }}"
    )


def build_video_switcher_page_attributes(element_id: str, element: dict) -> str:
    label = element.get("label", "") or "Video Switcher"
    n_sources = element.get("source_count") or _DEFAULT_SOURCE_COUNT
    n_screens = element.get("screen_count") or _DEFAULT_SCREEN_COUNT

    sources_toml = "".join(
        '[[Elements.Components]]\n'
        'Type = "Ch5 Video Switcher Source"\n'
        '\n'
        '[Elements.Components.Attributes]\n'
        'ccid_imageIconType = "iconclass"\n'
        f'id = "Source{i}"\n'
        f'componentName = "Source {i}"\n'
        f'componentNumber = "{i}"\n'
        for i in range(1, n_sources + 1)
    )
    screens_toml = "".join(
        '[[Elements.Components]]\n'
        'Type = "Ch5 Video Switcher Screen"\n'
        '\n'
        '[Elements.Components.Attributes]\n'
        f'id = "Screen{i}"\n'
        f'componentName = "Screen {i}"\n'
        f'componentNumber = "{i}"\n'
        'alignlabel = "center"\n'
        for i in range(1, n_screens + 1)
    )

    return (
        '[[Elements]]\n'
        'Type = "Ch5 Video Switcher"\n'
        'Editable = true\n'
        '\n'
        + sources_toml + screens_toml +
        '\n[Elements.Attributes]\n'
        f'numberofsources = "{n_sources}"\n'
        'numberofsourcelistdivisions = "1"\n'
        f'numberofscreens = "{n_screens}"\n'
        'displayscreenlabel = "true"\n'
        'numberofscreencolumns = "0"\n'
        'indexId = "idx"\n'
        'scrollbar = "true"\n'
        'screenaspectratio = "stretch"\n'
        'sourcelistposition = "top"\n'
        'ccid_linkSendReceive = "True"\n'
        'sourceiconclass = "fas fa-video"\n'
        'ccid_imageIconType = "iconclass"\n'
        'endless = "false"\n'
        f'id = "{element_id}"\n'
        f'componentName = "{label}"\n'
        'ccid_ActiveFont = "\'Roboto\'"\n'
        'assetid = "0"\n'
        'ccid_ComponentType = "Video Switcher"\n'
        f'devicesVisited = "{_DEVICES_VISITED_TOML}"'
    )
