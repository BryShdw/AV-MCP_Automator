def build_header_html(element_id: str, element: dict) -> str:
    label = element.get("label", "")

    return (
        f'<h1 '
        f'headingtype="h1" '
        f'data-mytext="myText" '
        f'componentname="{label}" '
        f'id="{element_id}" '
        f'ccid_componenttype="Html-header" '
        f'ccid_activefont="\'Roboto\'" '
        f'devicesvisited="[&quot;TST-1080 (Landscape)&quot;]">'
        f'{label}'
        f'</h1>'
    )


def build_header_css(element_id: str, element: dict) -> str:
    x = element["x"]
    y = element["y"]
    w = element["w"]
    h = element["h"]
    text_color = element.get("text_color", "#FFFFFF")
    font_size = element.get("font_size", 32)

    return (
        f"  #{element_id} {{\n"
        f"    overflow: hidden;\n"
        f"    font-weight: 400;\n"
        f"    font-size: {font_size}px;\n"
        f"    min-width: 1em;\n"
        f"    min-height: 1.5em;\n"
        f"    font-family: 'Roboto';\n"
        f"    display: block;\n"
        f"    color: {text_color};\n"
        f"    background-color: transparent;\n"
        f"    margin: 0;\n"
        f"    left: {x}px;\n"
        f"    top: {y}px;\n"
        f"    position: absolute;\n"
        f"    font-style: normal;\n"
        f"  }}"
    )


def build_header_page_attributes(element_id: str, element: dict) -> str:
    label = element.get("label", "")
    return (
        '[[Elements]]\n'
        'Type = "html-header"\n'
        'Editable = true\n'
        '\n'
        '[[Elements.Components]]\n'
        'Type = "textnode"\n'
        f'Content = "{label}"\n'
        '\n'
        '[Elements.Attributes]\n'
        'headingType = "h1"\n'
        'data-mytext = "myText"\n'
        f'componentName = "{label}"\n'
        f'id = "{element_id}"\n'
        'ccid_ComponentType = "Html-header"\n'
        f'ccid_ActiveFont = "\'Roboto\'"\n'
        f'devicesVisited = "[\\\"TST-1080 (Landscape)\\\"]"'
    )
