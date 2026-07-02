"""
Plantilla para el componente "container" — un <div> reutilizable como
panel/zona visual con fondo y borde propios.

RUP Fase: Construccion — Iteracion 5 (UI/UX)
Basado en el patron Html-div ya verificado en el forense, el mismo que
usa builder_tool.py internamente para el fondo de pagina — aqui se expone
como un tipo de componente publico que Gemini puede colocar varias veces
por pagina, para agrupar controles.

IMPORTANTE — orden de capas: en CSS con position:absolute, el orden de
aparicion en el HTML determina que queda encima. Los "container" deben
generarse ANTES (mas arriba en el array "elements" del JSON) que los
controles que van dentro de ellos, para quedar detras visualmente. Esto
se exige como regla en system_prompt.md, no se resuelve en Python.
"""

_DEVICES_VISITED_HTML = '[&quot;TST-1080 (Landscape)&quot;]'
_DEVICES_VISITED_TOML = '[\\\"TST-1080 (Landscape)\\\"]'


def build_container_html(element_id: str, element: dict) -> str:
    label = element.get("label", "") or "Container"

    return (
        f'<div '
        f'id="{element_id}" '
        f'componentname="{label}" '
        f'ccid_componenttype="Html-div" '
        f'devicesvisited="{_DEVICES_VISITED_HTML}">'
        f'</div>'
    )


def build_container_css(element_id: str, element: dict) -> str:
    x = element["x"]
    y = element["y"]
    w = element["w"]
    h = element["h"]

    # Fondo: gradiente tiene prioridad sobre color sólido
    gradient = element.get("background_gradient")
    bg_solid = element.get("panel_background_color") or "transparent"
    bg_value = gradient if gradient else bg_solid

    border_color  = element.get("border_color")  or "#2A2F3A"
    border_width  = element.get("border_width")
    if border_width is None:
        border_width = 1
    border_radius = element.get("border_radius")
    if border_radius is None:
        border_radius = 12

    box_shadow = element.get("box_shadow")
    opacity    = element.get("opacity")

    shadow_line  = f"    box-shadow: {box_shadow};\n" if box_shadow else ""
    opacity_line = f"    opacity: {opacity};\n"        if opacity    else ""

    return (
        f"  #{element_id} {{\n"
        f"    display: block;\n"
        f"    position: absolute;\n"
        f"    left: {x}px;\n"
        f"    top: {y}px;\n"
        f"    width: {w}px;\n"
        f"    height: {h}px;\n"
        f"    background: {bg_value};\n"
        f"    border: {border_width}px solid {border_color};\n"
        f"    border-radius: {border_radius}px;\n"
        f"    box-sizing: border-box;\n"
        f"{shadow_line}"
        f"{opacity_line}"
        f"  }}"
    )


def build_container_page_attributes(element_id: str, element: dict) -> str:
    label = element.get("label", "") or "Container"

    return (
        '[[Elements]]\n'
        'Type = "html-div"\n'
        'Editable = true\n'
        '\n'
        '[Elements.Attributes]\n'
        f'componentName = "{label}"\n'
        f'id = "{element_id}"\n'
        'ccid_ComponentType = "Html-div"\n'
        f'devicesVisited = "{_DEVICES_VISITED_TOML}"'
    )
