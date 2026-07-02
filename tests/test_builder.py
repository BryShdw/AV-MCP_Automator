"""
Tests del Builder_Tool — CP-01 al CP-04
RUP: Construcción IT-4 | Va al informe: ✅ Sí
"""
import pytest
import os
import re
from pathlib import Path
from src.server_mcp.tools.builder_tool import build_cuig_file


@pytest.fixture
def layout_simple():
    return {
        "page_name": "Test_Boton",
        "canvas_width": 1280,
        "canvas_height": 800,
        "elements": [
            {"type": "ch5-button", "label": "ON", "x": 100, "y": 100,
             "w": 120, "h": 50, "color": "success"}
        ]
    }

@pytest.fixture
def layout_completo():
    return {
        "page_name": "Test_Completo",
        "canvas_width": 1920,
        "canvas_height": 1080,
        "elements": [
            {"type": "ch5-button", "label": "Encender", "x": 100, "y": 200,
             "w": 120, "h": 50, "color": "success"},
            {"type": "ch5-button", "label": "Apagar",   "x": 240, "y": 200,
             "w": 120, "h": 50, "color": "danger"},
            {"type": "ch5-slider", "label": "Volumen",  "x": 100, "y": 300,
             "w": 300, "h": 30},
        ]
    }


def test_CP01_genera_archivo_cuig(layout_simple, tmp_path):
    """CP-01: El Builder_Tool genera un archivo .cuig en disco."""
    ruta = build_cuig_file(layout_simple, output_dir=tmp_path)
    assert Path(ruta).exists(), "El archivo .cuig no fue creado en disco"
    assert ruta.endswith(".cuig"), "El archivo generado no tiene extensión .cuig"


def test_CP02_cuig_tiene_cuatro_bloques(layout_simple, tmp_path):
    """CP-02: El .cuig generado contiene los 4 bloques requeridos por Crestron."""
    ruta = build_cuig_file(layout_simple, output_dir=tmp_path)
    contenido = Path(ruta).read_text(encoding="utf-8")
    assert "{FileMetadata}" in contenido, "Falta bloque {FileMetadata}"
    assert "{Html}"         in contenido, "Falta bloque {Html}"
    assert "{Css}"          in contenido, "Falta bloque {Css}"
    assert "{PageAttributes}" in contenido, "Falta bloque {PageAttributes}"


def test_CP03_ids_unicos_consistentes(layout_completo, tmp_path):
    """CP-03: Cada ID de elemento aparece exactamente en {Html}, {Css} y {PageAttributes}."""
    ruta = build_cuig_file(layout_completo, output_dir=tmp_path)
    contenido = Path(ruta).read_text(encoding="utf-8")

    # Extraer todos los IDs del bloque {Html} (atributo id="XXXX")
    ids_html = set(re.findall(r'\bid="([a-z0-9]{4,6})"', contenido))
    assert len(ids_html) >= len(layout_completo["elements"]), \
        "Hay menos IDs en {Html} que elementos en el layout"

    for element_id in ids_html:
        # El mismo ID debe aparecer en el bloque {Css} como selector CSS
        assert f"#{element_id}" in contenido, \
            f"ID '{element_id}' no tiene regla CSS en {{Css}}"
        # Y también en {PageAttributes} como campo id =
        assert f'id = "{element_id}"' in contenido or \
               f"id = '{element_id}'" in contenido, \
            f"ID '{element_id}' no aparece en {{PageAttributes}}"


def test_CP04_coordenadas_mapeadas_a_css(layout_simple, tmp_path):
    """CP-04: Las coordenadas x,y,w,h del JSON se mapean a left,top,width,height en px."""
    el = layout_simple["elements"][0]
    ruta = build_cuig_file(layout_simple, output_dir=tmp_path)
    contenido = Path(ruta).read_text(encoding="utf-8")

    assert f"left: {el['x']}px"   in contenido, "Coordenada x no mapeada a left"
    assert f"top: {el['y']}px"    in contenido, "Coordenada y no mapeada a top"
    assert f"width: {el['w']}px"  in contenido, "Coordenada w no mapeada a width"
    assert f"height: {el['h']}px" in contenido, "Coordenada h no mapeada a height"


def test_CP05_background_color_aplicado(layout_simple, tmp_path):
    """CP-05: El background_color del tema se aplica al canvas en el bloque {Css}."""
    color_test = "#1A3560"
    ruta = build_cuig_file(layout_simple, output_dir=tmp_path,
                           background_color=color_test)
    contenido = Path(ruta).read_text(encoding="utf-8")
    assert color_test in contenido, \
        f"El color de fondo '{color_test}' no aparece en el .cuig generado"


def test_CP06_doble_media_query(layout_simple, tmp_path):
    """CP-06: El CSS contiene el doble bloque @media requerido por Crestron."""
    ruta = build_cuig_file(layout_simple, output_dir=tmp_path)
    contenido = Path(ruta).read_text(encoding="utf-8")
    assert contenido.count("@media") >= 2, \
        "El .cuig debe tener al menos 2 bloques @media (universal + landscape)"


def test_CP07_labels_no_son_placeholder(layout_completo, tmp_path):
    """CP-07: Ningún componente debe tener 'label' como texto hardcodeado."""
    ruta = build_cuig_file(layout_completo, output_dir=tmp_path)
    contenido = Path(ruta).read_text(encoding="utf-8")
    assert 'labelinnerhtml="label"' not in contenido, \
        "Se detectó label hardcodeado 'label' en el .cuig"
    # Verificar que los labels reales sí están
    for el in layout_completo["elements"]:
        if el.get("label"):
            assert el["label"] in contenido, \
                f"El label '{el['label']}' no aparece en el .cuig"


def test_CP08_div_base_fondo_presente(layout_simple, tmp_path):
    """CP-08: El .cuig tiene un html-div de fondo con el background_color del tema."""
    color = "#1A3560"
    ruta = build_cuig_file(layout_simple, output_dir=tmp_path, background_color=color)
    contenido = Path(ruta).read_text(encoding="utf-8")
    assert color in contenido, \
        f"El background_color '{color}' no aparece en el .cuig"
    assert "Html-div" in contenido or "html-div" in contenido, \
        "Falta el elemento html-div de fondo en el .cuig"
    # El div debe aparecer ANTES del primer ch5-button en el Html
    pos_div    = contenido.lower().find("html-div")
    pos_button = contenido.lower().find("ch5-button")
    assert pos_div < pos_button, \
        "El div de fondo debe aparecer ANTES del primer ch5-button en {Html}"


def test_CP09_button_text_ccid_label_no_hardcodeado():
    """CP-09: ccid_label usa el valor real, no 'label' hardcodeado."""
    from src.server_mcp.templates.button_template import build_button_page_attributes
    from src.server_mcp.templates.text_template import build_text_page_attributes

    el = {"type": "ch5-button", "label": "Encender", "x": 0, "y": 0, "w": 1, "h": 1}
    btn_attrs = build_button_page_attributes("id1", el)
    assert 'ccid_label = "Encender"' in btn_attrs
    assert 'ccid_label = "label"' not in btn_attrs


    el2 = {"type": "ch5-text", "label": "Titulo", "x": 0, "y": 0, "w": 1, "h": 1}
    txt_attrs = build_text_page_attributes("id2", el2)
    assert 'ccid_label = "Titulo"' in txt_attrs
    assert 'ccid_label = "label"' not in txt_attrs


def test_CP10_toggle_sin_atributo_label():
    """CP-10: ch5-toggle no tiene el atributo irreal label=\"..."."""
    from src.server_mcp.templates.toggle_template import build_toggle_html
    el = {"type": "ch5-toggle", "label": "Mute", "x": 0, "y": 0, "w": 1, "h": 1}
    html = build_toggle_html("id1", el)
    
    assert ' label="' not in html, "Se encontro el atributo label= en el toggle"


def test_CP11_nuevos_componentes_generan_tag_esperado(tmp_path):
    """CP-11: Los 6 componentes nuevos generan el tag HTML correcto sin error."""
    types_and_tags = [
        ("ch5-gauge", "<ch5-segmented-gauge"),
        ("ch5-dpad", "<ch5-dpad"),
        ("ch5-keypad", "<ch5-keypad"),
        ("ch5-image", "<ch5-image"),
        ("ch5-tab-button", "<ch5-tab-button"),
        ("ch5-video-switcher", "<ch5-video-switcher"),
    ]
    
    for ctype, tag in types_and_tags:
        layout = {
            "page_name": f"Test_{ctype}",
            "canvas_width": 1280,
            "canvas_height": 800,
            "elements": [
                {"type": ctype, "label": "Test", "x": 10, "y": 10, "w": 100, "h": 100}
            ]
        }
        ruta = build_cuig_file(layout, output_dir=tmp_path)
        contenido = Path(ruta).read_text(encoding="utf-8")
        assert tag in contenido, f"Falta el tag {tag} para el componente {ctype}"


def test_CP12_dpad_tiene_5_sub_botones(tmp_path):
    """CP-12: Un ch5-dpad genera exactamente 5 sub-botones."""
    layout = {
        "page_name": "Test_Dpad",
        "canvas_width": 1280,
        "canvas_height": 800,
        "elements": [
            {"type": "ch5-dpad", "label": "PTZ", "x": 10, "y": 10, "w": 100, "h": 100}
        ]
    }
    ruta = build_cuig_file(layout, output_dir=tmp_path)
    contenido = Path(ruta).read_text(encoding="utf-8")
    
    # Contamos ocurrencias de <ch5-dpad-button
    matches = len(re.findall(r"<ch5-dpad-button", contenido))
    assert matches == 5, f"Se esperaban 5 ch5-dpad-button, se encontraron {matches}"


def test_CP13_keypad_tiene_13_sub_botones(tmp_path):
    """CP-13: Un ch5-keypad genera exactamente 13 sub-botones."""
    layout = {
        "page_name": "Test_Keypad",
        "canvas_width": 1280,
        "canvas_height": 800,
        "elements": [
            {"type": "ch5-keypad", "label": "Dialer", "x": 10, "y": 10, "w": 200, "h": 300}
        ]
    }
    ruta = build_cuig_file(layout, output_dir=tmp_path)
    contenido = Path(ruta).read_text(encoding="utf-8")
    
    # Contamos ocurrencias de <ch5-keypad-button
    matches = len(re.findall(r"<ch5-keypad-button", contenido))
    assert matches == 13, f"Se esperaban 13 ch5-keypad-button, se encontraron {matches}"


def test_CP14_video_switcher_sub_elementos(tmp_path):
    """CP-14: ch5-video-switcher respeta source_count e ids predecibles."""
    layout = {
        "page_name": "Test_Switcher",
        "canvas_width": 1280,
        "canvas_height": 800,
        "elements": [
            {
                "type": "ch5-video-switcher", 
                "label": "Matrix", 
                "x": 10, "y": 10, "w": 400, "h": 300,
                "source_count": 3,
                "screen_count": 1
            }
        ]
    }
    ruta = build_cuig_file(layout, output_dir=tmp_path)
    contenido = Path(ruta).read_text(encoding="utf-8")
    
    # Contamos fuentes
    sources = re.findall(r"<ch5-video-switcher-source", contenido)
    assert len(sources) == 3, f"Se esperaban 3 sources, se encontraron {len(sources)}"
    
    # Verificamos ids
    assert 'id="Source1"' in contenido
    assert 'id="Source2"' in contenido
    assert 'id="Source3"' in contenido
    
    # Verificamos que no haya un cuarto
    assert 'id="Source4"' not in contenido


def test_CP15_ids_unicos_entre_paginas(layout_simple, tmp_path):
    """CP-15: Generar dos páginas distintas en el mismo directorio no produce IDs repetidos."""
    # Generar página A
    layout_A = dict(layout_simple)
    layout_A["page_name"] = "Pagina_A"
    ruta_A = build_cuig_file(layout_A, output_dir=tmp_path)
    
    # Generar página B
    layout_B = dict(layout_simple)
    layout_B["page_name"] = "Pagina_B"
    ruta_B = build_cuig_file(layout_B, output_dir=tmp_path)
    
    contenido_A = Path(ruta_A).read_text(encoding="utf-8")
    contenido_B = Path(ruta_B).read_text(encoding="utf-8")
    
    ids_A = set(re.findall(r'id="(i[0-9a-f]{4,})"', contenido_A))
    ids_B = set(re.findall(r'id="(i[0-9a-f]{4,})"', contenido_B))
    
    interseccion = ids_A.intersection(ids_B)
    assert len(interseccion) == 0, f"Se encontraron IDs repetidos entre paginas: {interseccion}"


def test_CP16_regeneracion_misma_pagina(layout_simple, tmp_path):
    """CP-16: Regenerar la misma página no rompe el escaneo de IDs."""
    # Generar página 1ra vez
    ruta_1 = build_cuig_file(layout_simple, output_dir=tmp_path)
    
    # Generar página 2da vez (sobreescribir)
    ruta_2 = build_cuig_file(layout_simple, output_dir=tmp_path)
    
    assert Path(ruta_2).exists()
    assert ruta_1 == ruta_2


def test_CP17_casing_consistente_labelInnerHTML(tmp_path):
    """CP-17: El HTML usa labelinnerhtml (minúsculas) consistentemente para resolver bug de parseo."""
    layout = {
        "page_name": "Test_Casing",
        "canvas_width": 1280,
        "canvas_height": 800,
        "elements": [
            {"type": "ch5-button", "label": "Encender Proyector", "x": 10, "y": 10, "w": 100, "h": 100},
            {"type": "ch5-text", "label": "Encender Proyector", "x": 10, "y": 150, "w": 100, "h": 100}
        ]
    }
    ruta = build_cuig_file(layout, output_dir=tmp_path)
    contenido = Path(ruta).read_text(encoding="utf-8")
    
    assert 'labelinnerhtml="Encender Proyector"' in contenido, "ch5-button debe usar labelinnerhtml en minúsculas"
    assert 'labelinnerhtml="Encender Proyector"' in contenido, "ch5-text debe usar labelinnerhtml (minúsculas)"


def test_CP18_no_duplicacion_atributos():
    """CP-18: labelInnerHTML y ccid_label aparecen exactamente una vez en el tag HTML."""
    from src.server_mcp.templates.button_template import build_button_html
    
    el = {"type": "ch5-button", "label": "Test Label", "x": 0, "y": 0, "w": 1, "h": 1}
    html = build_button_html("id1", el)
    
    label_inner_html_count = len(re.findall(r'labelInnerHTML=', html, flags=re.IGNORECASE))
    ccid_label_count = len(re.findall(r'ccid_label=', html, flags=re.IGNORECASE))
    
    assert label_inner_html_count == 1, f"labelInnerHTML aparece {label_inner_html_count} veces, se esperaba 1"
    assert ccid_label_count == 1, f"ccid_label aparece {ccid_label_count} veces, se esperaba 1"


def test_CP19_container_css_custom_values():
    """CP-19: build_container_css() aplica valores custom de borde."""
    from src.server_mcp.templates.container_template import build_container_css
    el = {
        "x": 10, "y": 10, "w": 100, "h": 100,
        "border_color": "#FF0000",
        "border_width": 3,
        "border_radius": 20
    }
    css = build_container_css("id1", el)
    assert "border: 3px solid #FF0000;" in css
    assert "border-radius: 20px;" in css


def test_CP20_container_css_default_values():
    """CP-20: build_container_css() usa defaults seguros."""
    from src.server_mcp.templates.container_template import build_container_css
    el = {"x": 10, "y": 10, "w": 100, "h": 100}
    css = build_container_css("id1", el)
    assert "background: transparent;" in css
    assert "border: 1px solid #2A2F3A;" in css
    assert "border-radius: 12px;" in css


def test_CP21_button_text_color():
    """CP-21: ch5-button aplica text_color opcionalmente en CSS."""
    from src.server_mcp.templates.button_template import build_button_css
    el_with_color = {"x": 10, "y": 10, "w": 100, "h": 100, "text_color": "#00FF00"}
    css1 = build_button_css("id1", el_with_color)
    assert "color: #00FF00;" in css1
    
    el_no_color = {"x": 10, "y": 10, "w": 100, "h": 100}
    css2 = build_button_css("id2", el_no_color)
    assert "color:" not in css2


def test_CP22_container_ordering_in_html(tmp_path):
    """CP-22: El layout con un container antes que botones preserva el orden HTML."""
    layout = {
        "page_name": "Test_Container_Order",
        "canvas_width": 1280,
        "canvas_height": 800,
        "elements": [
            {"type": "container", "label": "Panel", "x": 10, "y": 10, "w": 500, "h": 500},
            {"type": "ch5-button", "label": "B1", "x": 20, "y": 20, "w": 100, "h": 100},
            {"type": "ch5-button", "label": "B2", "x": 140, "y": 20, "w": 100, "h": 100}
        ]
    }
    ruta = build_cuig_file(layout, output_dir=tmp_path)
    contenido = Path(ruta).read_text(encoding="utf-8")
    
    # Extraer bloque Html
    html_start = contenido.find("{Html}")
    html_end = contenido.find("{Css}")
    bloque_html = contenido[html_start:html_end]
    
    # Check that container div appears before ch5-buttons
    pos_panel = bloque_html.find('componentname="Panel"')
    pos_b1 = bloque_html.find('componentname="B1"')
    pos_b2 = bloque_html.find('componentname="B2"')
    
    assert pos_panel != -1 and pos_b1 != -1 and pos_b2 != -1
    assert pos_panel < pos_b1
    assert pos_b1 < pos_b2


def test_CP23_button_shape_circle(tmp_path):
    layout = {
        "page_name": "TestShape",
        "canvas_width": 1280,
        "canvas_height": 800,
        "elements": [
            {
                "type": "ch5-button",
                "label": "Circle",
                "x": 0, "y": 0, "w": 100, "h": 100,
                "shape": "circle"
            }
        ]
    }
    ruta = build_cuig_file(layout, output_dir=str(tmp_path))
    cuig_str = Path(ruta).read_text(encoding='utf-8')
    
    html_block = cuig_str.split("{Html}")[1].split("{Css}")[0]
    
    assert 'shape="circle"' in html_block
    assert 'shape="rounded-rectangle"' not in html_block


def test_CP24_button_box_shadow(tmp_path):
    layout = {
        "page_name": "TestShadow",
        "canvas_width": 1280,
        "canvas_height": 800,
        "elements": [
            {
                "type": "ch5-button",
                "label": "Btn",
                "x": 0, "y": 0, "w": 100, "h": 100,
                "box_shadow": "0 4px 12px rgba(0,0,0,0.5)"
            }
        ]
    }
    ruta = build_cuig_file(layout, output_dir=str(tmp_path))
    cuig_str = Path(ruta).read_text(encoding='utf-8')
    css_block = cuig_str.split("{Css}")[1].split("{PageAttributes}")[0]
    
    assert "box-shadow: 0 4px 12px rgba(0,0,0,0.5);" in css_block


def test_CP25_text_typography_custom(tmp_path):
    layout = {
        "page_name": "TestTextTypo",
        "canvas_width": 1280,
        "canvas_height": 800,
        "elements": [
            {
                "type": "ch5-text",
                "label": "Big Text",
                "x": 0, "y": 0, "w": 400, "h": 100,
                "font_size": 96,
                "font_weight": "700",
                "letter_spacing": 4
            }
        ]
    }
    ruta = build_cuig_file(layout, output_dir=str(tmp_path))
    cuig_str = Path(ruta).read_text(encoding='utf-8')
    css_block = cuig_str.split("{Css}")[1].split("{PageAttributes}")[0]
    
    assert "font-size: 96px;" in css_block
    assert "font-weight: 700;" in css_block
    assert "letter-spacing: 4px;" in css_block


def test_CP26_text_typography_default(tmp_path):
    layout = {
        "page_name": "TestTextTypoDef",
        "canvas_width": 1280,
        "canvas_height": 800,
        "elements": [
            {
                "type": "ch5-text",
                "label": "Def Text",
                "x": 0, "y": 0, "w": 400, "h": 100
            }
        ]
    }
    ruta = build_cuig_file(layout, output_dir=str(tmp_path))
    cuig_str = Path(ruta).read_text(encoding='utf-8')
    css_block = cuig_str.split("{Css}")[1].split("{PageAttributes}")[0]
    
    assert "font-size:" not in css_block
    assert "font-weight:" not in css_block
    assert "letter-spacing:" not in css_block


def test_CP27_container_background_gradient(tmp_path):
    layout = {
        "page_name": "TestGrad",
        "canvas_width": 1280,
        "canvas_height": 800,
        "elements": [
            {
                "type": "container",
                "label": "Grad",
                "x": 0, "y": 0, "w": 100, "h": 100,
                "background_gradient": "linear-gradient(135deg, #000 0%, #111 100%)",
                "panel_background_color": "#FF0000"
            }
        ]
    }
    ruta = build_cuig_file(layout, output_dir=str(tmp_path))
    cuig_str = Path(ruta).read_text(encoding='utf-8')
    css_block = cuig_str.split("{Css}")[1].split("{PageAttributes}")[0]
    
    assert "background: linear-gradient(135deg, #000 0%, #111 100%);" in css_block
    assert "background-color: #FF0000" not in css_block


def test_CP28_container_shadow_opacity(tmp_path):
    layout = {
        "page_name": "TestOp",
        "canvas_width": 1280,
        "canvas_height": 800,
        "elements": [
            {
                "type": "container",
                "label": "Cont",
                "x": 0, "y": 0, "w": 100, "h": 100,
                "box_shadow": "0 2px 5px #000",
                "opacity": 0.9
            }
        ]
    }
    ruta = build_cuig_file(layout, output_dir=str(tmp_path))
    cuig_str = Path(ruta).read_text(encoding='utf-8')
    css_block = cuig_str.split("{Css}")[1].split("{PageAttributes}")[0]
    
    assert "box-shadow: 0 2px 5px #000;" in css_block
    assert "opacity: 0.9;" in css_block


def test_CP29_layout_ordering(tmp_path):
    layout = {
        "page_name": "TestOrder",
        "canvas_width": 1280,
        "canvas_height": 800,
        "elements": [
            {"type": "container", "label": "C1", "x": 0, "y": 0, "w": 10, "h": 10},
            {"type": "container", "label": "C2", "x": 0, "y": 0, "w": 10, "h": 10},
            {"type": "container", "label": "C3", "x": 0, "y": 0, "w": 10, "h": 10}, # accent bar
            {"type": "ch5-text", "label": "T1", "x": 0, "y": 0, "w": 10, "h": 10},
            {"type": "ch5-text", "label": "T2", "x": 0, "y": 0, "w": 10, "h": 10},
            {"type": "ch5-button", "label": "B1", "x": 0, "y": 0, "w": 10, "h": 10},
            {"type": "ch5-button", "label": "B2", "x": 0, "y": 0, "w": 10, "h": 10},
            {"type": "ch5-button", "label": "B3", "x": 0, "y": 0, "w": 10, "h": 10},
            {"type": "ch5-button", "label": "B4", "x": 0, "y": 0, "w": 10, "h": 10}
        ]
    }
    ruta = build_cuig_file(layout, output_dir=str(tmp_path))
    cuig_str = Path(ruta).read_text(encoding='utf-8')
    html_block = cuig_str.split("{Html}")[1].split("{Css}")[0]
    
    idx_c2 = html_block.find('componentname="C2"')
    idx_b1 = html_block.find('componentname="B1"')
    
    assert idx_c2 != -1
    assert idx_b1 != -1
    assert idx_c2 < idx_b1
