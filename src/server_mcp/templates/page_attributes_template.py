"""
Plantilla para el bloque {PageAttributes} del archivo .cuig.

RUP Fase: Construccion — Iteracion 3 (Semana 6)
Fuente: docs/01_Inception/05_analisis_forense_cuig.md — Bloque 4

Genera la seccion [Attributes] de la pagina y delega cada [[Elements]]
al metodo build_*_page_attributes() de la plantilla correspondiente.
"""
import uuid

from .button_template import build_button_page_attributes
from .slider_template import build_slider_page_attributes
from .video_template import build_video_page_attributes
from .text_template import build_text_page_attributes
from .toggle_template import build_toggle_page_attributes
from .gauge_template import build_gauge_page_attributes
from .dpad_template import build_dpad_page_attributes
from .keypad_template import build_keypad_page_attributes
from .image_template import build_image_page_attributes
from .tab_button_template import build_tab_button_page_attributes
from .video_switcher_template import build_video_switcher_page_attributes
from .container_template import build_container_page_attributes
from .header_template import build_header_page_attributes


# ─── DISPATCHER: tipo de componente → funcion de PageAttributes ───────────────

_PAGE_ATTR_BUILDERS = {
    "ch5-button": build_button_page_attributes,
    "ch5-slider": build_slider_page_attributes,
    "ch5-video":  build_video_page_attributes,
    "ch5-text":   build_text_page_attributes,
    "ch5-toggle": build_toggle_page_attributes,
    "ch5-gauge":  build_gauge_page_attributes,
    "ch5-dpad":   build_dpad_page_attributes,
    "ch5-keypad": build_keypad_page_attributes,
    "ch5-image":  build_image_page_attributes,
    "ch5-tab-button":     build_tab_button_page_attributes,
    "ch5-video-switcher": build_video_switcher_page_attributes,
    "container": build_container_page_attributes,
    "ch5-header": build_header_page_attributes,
}


def _build_bg_div_page_attrs(div_id: str) -> str:
    """Entrada en {PageAttributes} para el div de fondo."""
    return (
        f"[[Elements]]\n"
        f"Type = \"html-div\"\n\n"
        f"[Elements.Attributes]\n"
        f"componentName = \"Background\"\n"
        f"id = \"{div_id}\"\n"
        f"ccid_ComponentType = \"Html-div\"\n"
        f"devicesVisited = \"[\\\"TST-1080 (Landscape)\\\"]\"\n"
    )


def build_page_attributes_block(
    page_name: str,
    bg_div_id: str,
    elements_with_ids: list[tuple[str, dict]],
) -> str:
    """
    Genera el bloque {PageAttributes} completo de un archivo .cuig.

    Incluye:
    - [Attributes]: metadatos de la pagina (Name, PageMode, Id, etc.)
    - [[Elements]]: uno por cada componente, con su bloque TOML especifico

    Args:
        page_name:         Nombre de la pagina (ej. "Proyector")
        bg_div_id:         ID del div de fondo
        elements_with_ids: Lista de tuplas (element_id, element_dict).
                           element_dict debe tener al menos 'type'.

    Returns:
        String con el bloque {PageAttributes} completo
    """
    # UUID completo para el page_id (Regla 6 del forense)
    page_id = str(uuid.uuid4())

    # Seccion [Attributes] de la pagina
    lines = [
        "{PageAttributes}",
        "[Attributes]",
        f'Name = "{page_name}"',
        'PageMode = "absolute"',
        f'Id = "{page_id}"',
        'StartPage = "False"',
        'PreloadPage = "False"',
        'CachePage = "False"',
        'VisibilityJoin = "0"',
        'DisplayBackgroundColor = "False"',
        "",  # linea en blanco entre [Attributes] y [[Elements]]
    ]

    # PRIMERO: el div de fondo
    lines.append(_build_bg_div_page_attrs(bg_div_id))

    # LUEGO: Generar [[Elements]] por cada componente
    for element_id, element in elements_with_ids:
        component_type = element["type"]
        builder_fn = _PAGE_ATTR_BUILDERS.get(component_type)

        if builder_fn is None:
            raise ValueError(
                f"Tipo de componente no soportado en PageAttributes: '{component_type}'. "
                f"Tipos validos: {list(_PAGE_ATTR_BUILDERS.keys())}"
            )

        element_block = builder_fn(element_id, element)
        lines.append(element_block)
        lines.append("")  # linea en blanco entre elementos

    return "\n".join(lines).rstrip()
