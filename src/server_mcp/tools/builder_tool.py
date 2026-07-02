"""
Builder_Tool — Compilador de archivos .cuig

Toma el JSON validado por Pydantic (LayoutSchema) y ensambla un archivo .cuig
nativo de Crestron Construct con los 4 bloques obligatorios:
  {FileMetadata} + {Html} + {Css} + {PageAttributes}

RUP Fase: Construccion — Iteracion 3 (Semana 7)
Fuente: docs/01_Inception/05_analisis_forense_cuig.md

Reglas criticas del forense:
  - IDs unicos: "i" + uuid4().hex[:4]
  - Canvas ID propio por pagina
  - Doble bloque @media identico en CSS
  - PageAttributes en formato TOML con [[Elements]]
  - devicesvisited siempre: '[&quot;TST-1080 (Landscape)&quot;]'
"""
import uuid
from pathlib import Path
import re

# Templates
from ..templates.metadata_template import build_metadata_block
from ..templates.button_template import (
    build_button_html, build_button_css,
)
from ..templates.slider_template import (
    build_slider_html, build_slider_css,
)
from ..templates.video_template import (
    build_video_html, build_video_css,
)
from ..templates.text_template import (
    build_text_html, build_text_css,
)
from ..templates.toggle_template import (
    build_toggle_html, build_toggle_css,
)
from ..templates.gauge_template import build_gauge_html, build_gauge_css
from ..templates.dpad_template import build_dpad_html, build_dpad_css
from ..templates.keypad_template import build_keypad_html, build_keypad_css
from ..templates.image_template import build_image_html, build_image_css
from ..templates.tab_button_template import (
    build_tab_button_html, build_tab_button_css,
)
from ..templates.video_switcher_template import (
    build_video_switcher_html, build_video_switcher_css,
)
from ..templates.container_template import build_container_html, build_container_css
from ..templates.page_attributes_template import build_page_attributes_block
from ..templates.header_template import build_header_html, build_header_css


# ─── DISPATCHERS ──────────────────────────────────────────────────────────────

_HTML_BUILDERS = {
    "ch5-button": build_button_html,
    "ch5-slider": build_slider_html,
    "ch5-video":  build_video_html,
    "ch5-text":   build_text_html,
    "ch5-toggle": build_toggle_html,
    "ch5-gauge":  build_gauge_html,
    "ch5-dpad":   build_dpad_html,
    "ch5-keypad": build_keypad_html,
    "ch5-image":  build_image_html,
    "ch5-tab-button":     build_tab_button_html,
    "ch5-video-switcher": build_video_switcher_html,
    "container": build_container_html,
    "ch5-header": build_header_html,
}

_CSS_BUILDERS = {
    "ch5-button": build_button_css,
    "ch5-slider": build_slider_css,
    "ch5-video":  build_video_css,
    "ch5-text":   build_text_css,
    "ch5-toggle": build_toggle_css,
    "ch5-gauge":  build_gauge_css,
    "ch5-dpad":   build_dpad_css,
    "ch5-keypad": build_keypad_css,
    "ch5-image":  build_image_css,
    "ch5-tab-button":     build_tab_button_css,
    "ch5-video-switcher": build_video_switcher_css,
    "container": build_container_css,
    "ch5-header": build_header_css,
}


# ─── FUNCIONES AUXILIARES ─────────────────────────────────────────────────────

def _generate_cuig_id() -> str:
    """
    Genera un ID unico en el formato de Crestron: "i" + 4 hex chars.
    Ejemplos reales del forense: i1l4, iw5g, iec5, i2e3i, ih6z
    """
    return "i" + uuid.uuid4().hex[:4]

def _scan_existing_ids(target_dir: Path) -> set[str]:
    """
    Escanea todos los archivos .cuig ya presentes en target_dir y devuelve
    el set de IDs ya usados en el proyecto.

    Esto es necesario porque Crestron Construct indexa los componentes a
    nivel de PROYECTO completo, no por pagina individual — dos elementos
    con el mismo id en dos paginas .cuig distintas pueden confundirse al
    sincronizar el proyecto en el editor. _generate_cuig_id() por si solo
    solo evita colisiones dentro de una sola llamada a build_cuig_file(),
    asi que este escaneo previo es el que garantiza unicidad real.
    """
    existing_ids: set[str] = set()
    id_pattern = re.compile(r'id="(i[0-9a-f]{4,})"')

    if not target_dir.exists():
        return existing_ids

    for cuig_file in target_dir.glob("*.cuig"):
        try:
            content = cuig_file.read_text(encoding="utf-8")
        except OSError:
            continue
        existing_ids.update(id_pattern.findall(content))

    return existing_ids


def _build_bg_div_html(div_id: str, element: dict) -> str:
    """Genera el html-div de fondo que establece el color del tema."""
    return (
        f'<div '
        f'id="{div_id}" '
        f'componentname="Background" '
        f'ccid_componenttype="Html-div" '
        f'devicesvisited="[&quot;TST-1080 (Landscape)&quot;]">'
        f'</div>'
    )

def _build_bg_div_css(div_id: str, element: dict) -> str:
    """CSS del div de fondo — ocupa todo el canvas con el color del tema."""
    bg_color = element.get("background_color", "#0D1117")
    w = element["w"]
    h = element["h"]
    return (
        f"  #{div_id} {{\n"
        f"    display: block;\n"
        f"    background-color: {bg_color};\n"
        f"    left: 0px;\n"
        f"    top: 0px;\n"
        f"    position: absolute;\n"
        f"    width: {w}px;\n"
        f"    height: {h}px;\n"
        f"  }}"
    )



def _build_html_block(
    bg_div_id: str,
    bg_div_element: dict,
    elements_with_ids: list[tuple[str, dict]]
) -> str:
    """
    Ensambla el bloque {Html} completo con todos los componentes.

    Cada componente HTML esta separado por '\\n              ' (salto + 14 espacios)
    como se observo en el forense.
    """
    html_fragments = []

    # PRIMERO: el div de fondo
    html_fragments.append(_build_bg_div_html(bg_div_id, bg_div_element))

    # LUEGO: el resto de componentes
    for element_id, element in elements_with_ids:
        component_type = element["type"]
        builder_fn = _HTML_BUILDERS.get(component_type)

        if builder_fn is None:
            raise ValueError(
                f"Tipo de componente no soportado en Html: '{component_type}'. "
                f"Tipos validos: {list(_HTML_BUILDERS.keys())}"
            )

        html_fragments.append(builder_fn(element_id, element))

    # Separador entre componentes: salto de linea + 14 espacios (patron del forense)
    separator = "\n              "
    inner_html = separator.join(html_fragments)

    return f"{{Html}}\n              {inner_html}"


def _build_css_block(
    canvas_id: str,
    bg_div_id: str,
    bg_div_element: dict,
    elements_with_ids: list[tuple[str, dict]],
    background_color: str = "#0D1117",
) -> str:
    """
    Ensambla el bloque {Css} completo con el doble @media obligatorio.

    Segun el forense (Regla 5):
    - Primer @media: max-width:99999px (universal)
    - Segundo @media: landscape especifico
    - Ambos contienen LAS MISMAS reglas CSS

    El canvas tiene su propia regla con background-color del tema seleccionado.
    """
    css_rules_list = []

    # Regla del canvas (fondo de pagina — color del tema elegido por el usuario)
    css_rules_list.append(f"  #{canvas_id} {{ background-color: {background_color}; }}")

    # PRIMERO: CSS del div de fondo
    css_rules_list.append(_build_bg_div_css(bg_div_id, bg_div_element))

    # LUEGO: Reglas de cada componente
    for element_id, element in elements_with_ids:
        component_type = element["type"]
        builder_fn = _CSS_BUILDERS.get(component_type)

        if builder_fn is None:
            raise ValueError(
                f"Tipo de componente no soportado en Css: '{component_type}'. "
                f"Tipos validos: {list(_CSS_BUILDERS.keys())}"
            )

        css_rules_list.append(builder_fn(element_id, element))

    css_rules = "\n".join(css_rules_list)

    # Doble bloque @media (Regla 5 del forense)
    return (
        "{Css}\n"
        f"@media (max-width: 99999px){{\n"
        f"{css_rules}\n"
        f"}}\n"
        f"@media (orientation: landscape) and (max-width: 1281px) and "
        f"(max-height: 801px), (orientation: landscape) and "
        f"(max-width: 1279px){{\n"
        f"{css_rules}\n"
        f"}}"
    )


# ─── FUNCION PRINCIPAL ────────────────────────────────────────────────────────

def build_cuig_file(
    layout_json: dict,
    output_dir: str | Path,
    background_color: str = "#0D1117",
) -> str:
    """
    Ensambla un archivo .cuig valido para Crestron Construct a partir del JSON
    validado por Pydantic (LayoutSchema).

    Proceso:
      1. Genera canvas_id + element_id por componente
      2. Ensambla {FileMetadata} con versiones hardcodeadas
      3. Ensambla {Html} con los componentes CH5
      4. Ensambla {Css} con doble @media, posicionamiento absoluto y color de fondo del tema
      5. Ensambla {PageAttributes} con formato TOML de Crestron
      6. Concatena los 4 bloques y escribe el .cuig en disco

    Args:
        layout_json: Dict validado con page_name, canvas_width, canvas_height, elements
        output_dir:  Ruta a Solutions/MiProyecto/MiProyecto/ (carpeta interna
                     donde Crestron Construct espera los archivos .cuig).
        background_color: Color hex del fondo de pagina del tema seleccionado.

    Returns:
        Ruta absoluta del archivo .cuig generado en disco
    """
    page_name = layout_json["page_name"]
    elements = layout_json["elements"]

    # Resolver directorio de salida
    target_dir = Path(output_dir)
    target_dir.mkdir(parents=True, exist_ok=True)

    # ─── 1. Generar IDs ──────────────────────────────────────────────────
    # Se escanean los IDs de TODAS las paginas ya existentes en el proyecto
    # antes de generar ninguno nuevo, para garantizar unicidad real a nivel
    # de proyecto (ver _scan_existing_ids para el porque).
    used_ids: set[str] = _scan_existing_ids(target_dir)

    def _next_id() -> str:
        new_id = _generate_cuig_id()
        while new_id in used_ids:
            new_id = _generate_cuig_id()
        used_ids.add(new_id)
        return new_id

    canvas_id = _next_id()

    # ID del div base de fondo (primera capa — establece el background_color)
    bg_div_id = _next_id()

    # Dimensiones del canvas para el div base
    canvas_w = layout_json.get("canvas_width", 1280)
    canvas_h = layout_json.get("canvas_height", 800)

    # Elemento div base (se insertará PRIMERO en Html, Css y PageAttributes)
    bg_div_element = {
        "type":           "html-div",
        "label":          "",
        "x":              0,
        "y":              0,
        "w":              canvas_w,
        "h":              canvas_h,
        "background_color": background_color,
    }

    # Lista de tuplas (element_id, element_dict) para pasar a todos los builders
    elements_with_ids: list[tuple[str, dict]] = []

    for el in elements:
        # Convertir Pydantic model a dict si es necesario
        el_dict = el if isinstance(el, dict) else el.model_dump()

        elements_with_ids.append((_next_id(), el_dict))

    # ─── 2. Ensamblar {FileMetadata} ─────────────────────────────────────
    metadata_block = build_metadata_block()

    # ─── 3. Ensamblar {Html} ─────────────────────────────────────────────
    html_block = _build_html_block(bg_div_id, bg_div_element, elements_with_ids)

    # ─── 4. Ensamblar {Css} ──────────────────────────────────────────────
    css_block = _build_css_block(
        canvas_id, bg_div_id, bg_div_element, elements_with_ids, background_color=background_color,
    )

    # ─── 5. Ensamblar {PageAttributes} ───────────────────────────────────
    page_attrs_block = build_page_attributes_block(
        page_name, bg_div_id, elements_with_ids
    )

    # ─── 6. Concatenar y escribir ────────────────────────────────────────
    cuig_content = (
        f"{metadata_block}\n"
        f"{html_block}\n"
        f"{css_block}\n"
        f"{page_attrs_block}\n"
    )

    # Nombre del archivo: page_name.cuig
    filename = f"{page_name}.cuig"
    filepath = target_dir / filename

    filepath.write_text(cuig_content, encoding="utf-8")

    return str(filepath.resolve())
