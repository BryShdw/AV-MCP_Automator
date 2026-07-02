"""
Test manual del Builder_Tool — Genera un .cuig de ejemplo y lo imprime en consola.

Ejecucion: python tests/manual_test_builder.py

Genera una pagina "Proyector" con:
  - Boton "Encender" (success)
  - Boton "Apagar" (danger)
  - Slider "Volumen"
  - Texto "Estado del Proyector"

El .cuig se escribe en tests/output/ para inspeccion visual.
"""
import sys
import os

# Fix encoding para Windows
if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Agregar src/ al path para imports relativos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from pathlib import Path

# Importar directamente las funciones (sin imports relativos del paquete)
# Para el test manual, importamos las templates y el builder de forma directa

# --- Reimportar sin relative imports para el script standalone ---
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src", "server_mcp"))

from templates.metadata_template import build_metadata_block
from templates.button_template import build_button_html, build_button_css, build_button_page_attributes
from templates.slider_template import build_slider_html, build_slider_css, build_slider_page_attributes
from templates.video_template import build_video_html, build_video_css, build_video_page_attributes
from templates.text_template import build_text_html, build_text_css, build_text_page_attributes
from templates.toggle_template import build_toggle_html, build_toggle_css, build_toggle_page_attributes
from templates.page_attributes_template import (
    build_page_attributes_block,
    _PAGE_ATTR_BUILDERS,
)

import uuid


# ─── CONFIGURACION DEL TEST ──────────────────────────────────────────────────

TEST_OUTPUT_DIR = Path(__file__).parent / "output"

TEST_LAYOUT = {
    "page_name": "Proyector",
    "canvas_width": 1280,
    "canvas_height": 800,
    "elements": [
        {
            "type": "ch5-button",
            "label": "Encender",
            "x": 100, "y": 200, "w": 160, "h": 60,
            "color": "success",
        },
        {
            "type": "ch5-button",
            "label": "Apagar",
            "x": 280, "y": 200, "w": 160, "h": 60,
            "color": "danger",
        },
        {
            "type": "ch5-slider",
            "label": "Volumen",
            "x": 100, "y": 320, "w": 400, "h": 40,
        },
        {
            "type": "ch5-text",
            "label": "Estado del Proyector",
            "x": 100, "y": 100, "w": 300, "h": 40,
        },
    ],
}


# ─── DISPATCHERS (replicados del builder_tool para el test standalone) ────────

_HTML_BUILDERS = {
    "ch5-button": build_button_html,
    "ch5-slider": build_slider_html,
    "ch5-video":  build_video_html,
    "ch5-text":   build_text_html,
    "ch5-toggle": build_toggle_html,
}

_CSS_BUILDERS = {
    "ch5-button": build_button_css,
    "ch5-slider": build_slider_css,
    "ch5-video":  build_video_css,
    "ch5-text":   build_text_css,
    "ch5-toggle": build_toggle_css,
}


def _generate_cuig_id() -> str:
    """Genera ID en formato Crestron: 'i' + 4 hex chars."""
    return "i" + uuid.uuid4().hex[:4]


def run_manual_test():
    """Ejecuta el test manual del Builder_Tool."""
    print("=" * 70)
    print("  AV-MCP Automator — Test Manual del Builder_Tool")
    print("  Generando archivo .cuig de ejemplo...")
    print("=" * 70)
    print()

    page_name = TEST_LAYOUT["page_name"]
    elements = TEST_LAYOUT["elements"]

    # 1. Generar IDs
    canvas_id = _generate_cuig_id()
    elements_with_ids = []
    used_ids = {canvas_id}

    for el in elements:
        new_id = _generate_cuig_id()
        while new_id in used_ids:
            new_id = _generate_cuig_id()
        used_ids.add(new_id)
        elements_with_ids.append((new_id, el))

    print(f"Canvas ID: {canvas_id}")
    for eid, el in elements_with_ids:
        print(f"  [{eid}] {el['type']} -> \"{el.get('label', '')}\"")
    print()

    # 2. FileMetadata
    metadata_block = build_metadata_block()

    # 3. Html
    html_fragments = []
    for element_id, element in elements_with_ids:
        builder_fn = _HTML_BUILDERS[element["type"]]
        html_fragments.append(builder_fn(element_id, element))

    separator = "\n              "
    html_block = f"{{Html}}\n              {separator.join(html_fragments)}"

    # 4. Css (doble @media)
    css_rules_list = [f"  #{canvas_id} {{ background-color: #ffffff; }}"]
    for element_id, element in elements_with_ids:
        builder_fn = _CSS_BUILDERS[element["type"]]
        css_rules_list.append(builder_fn(element_id, element))

    css_rules = "\n".join(css_rules_list)
    css_block = (
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

    # 5. PageAttributes
    page_attrs_block = build_page_attributes_block(page_name, elements_with_ids)

    # 6. Concatenar
    cuig_content = (
        f"{metadata_block}\n"
        f"{html_block}\n"
        f"{css_block}\n"
        f"{page_attrs_block}\n"
    )

    # 7. Escribir archivo
    TEST_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    filepath = TEST_OUTPUT_DIR / f"{page_name}.cuig"
    filepath.write_text(cuig_content, encoding="utf-8")

    print(f"Archivo generado: {filepath.resolve()}")
    print(f"Tamanio: {filepath.stat().st_size} bytes")
    print()

    # 8. Imprimir contenido para verificacion visual
    print("=" * 70)
    print("  CONTENIDO DEL ARCHIVO .cuig GENERADO")
    print("=" * 70)
    print()
    print(cuig_content)
    print()
    print("=" * 70)

    # 9. Validaciones basicas
    print()
    print("  VALIDACIONES")
    print("-" * 70)
    checks = [
        ("{FileMetadata}", "{FileMetadata}" in cuig_content),
        ("{Html}", "{Html}" in cuig_content),
        ("{Css}", "{Css}" in cuig_content),
        ("{PageAttributes}", "{PageAttributes}" in cuig_content),
        ("Schema = \"1.0.0.0\"", 'Schema = "1.0.0.0"' in cuig_content),
        ("Doble @media", cuig_content.count("@media") == 2),
        ("IDs consistentes (Html+Css+PageAttrs)", all(
            eid in cuig_content
            for eid, _ in elements_with_ids
            # Verificar que cada ID aparece al menos 3 veces (Html, Css, PageAttributes)
        )),
        ("Canvas ID en CSS", canvas_id in cuig_content),
        ("devicesvisited presente", "TST-1080" in cuig_content),
        ('PageMode = "absolute"', 'PageMode = "absolute"' in cuig_content),
    ]

    all_passed = True
    for name, passed in checks:
        status = "[OK]" if passed else "[FAIL]"
        print(f"  {status} {name}")
        if not passed:
            all_passed = False

    # Verificar que cada ID aparece al menos 3 veces
    for eid, el in elements_with_ids:
        count = cuig_content.count(eid)
        ok = count >= 3
        status = "[OK]" if ok else "[FAIL]"
        print(f"  {status} ID '{eid}' aparece {count} veces (min 3: Html+Css+PageAttrs)")
        if not ok:
            all_passed = False

    print("-" * 70)
    if all_passed:
        print("  TODAS LAS VALIDACIONES PASARON")
    else:
        print("  ALGUNAS VALIDACIONES FALLARON")
    print("=" * 70)


if __name__ == "__main__":
    run_manual_test()
