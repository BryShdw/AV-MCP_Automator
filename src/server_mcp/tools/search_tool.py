"""
Search_Tool — Recuperacion semantica desde LanceDB.

Dado una lista de tipos de componentes CH5, busca en la tabla 'ch5_components'
(indexada por ingest.py) y retorna los esquemas encontrados formateados como
string para insertar en el prompt de Gemini.

Si LanceDB no tiene resultados para un tipo, se usa el esquema base del
SEED_SCHEMA como fallback para que Gemini siempre tenga contexto minimo.

RUP Fase: Construccion — Iteracion 3 (Semana 9)
"""
import os
import json
import logging
import lancedb
from pathlib import Path
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()

logger = logging.getLogger(__name__)

# ─── CONFIGURACION ────────────────────────────────────────────────────────────

LANCEDB_PATH = os.getenv("LANCEDB_PATH", "src/data_layer/lancedb_store")
TABLE_NAME = os.getenv("LANCEDB_TABLE_NAME", "ch5_components")
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# ─── SEED SCHEMAS (fallback local) ───────────────────────────────────────────
# Duplicados de ingest.py para evitar importar pyarrow/numpy en cada llamada.
# Si se actualiza ingest.py, actualizar tambien aqui.

_SEED_SCHEMAS: dict[str, dict] = {
    "ch5-button": {
        "component_type": "ch5-button",
        "description": (
            "Botón de acción táctil para control AV. Usado para "
            "encender/apagar dispositivos, cambiar fuentes o ejecutar macros."
        ),
        "content": (
            "Componente ch5-button: Botón de acción táctil para control AV profesional. "
            "Tipos disponibles: default, info, text, danger, warning, success, primary, secondary. "
            "Atributos clave: label, type, shape, size, orientation, iconClass, iconUrl, "
            "backgroundImageUrl, customClass, sendEventOnClick, receiveStateLabel, "
            "receiveStateSelected. "
            "JSON schema del compilador: "
            + json.dumps({
                "type": "ch5-button",
                "label": "", "x": 0, "y": 0, "w": 120, "h": 50,
                "color": "default",
            })
        ),
    },
    "ch5-slider": {
        "component_type": "ch5-slider",
        "description": (
            "Control deslizante analógico para volumen, brillo o "
            "nivel de iluminación en salas AV."
        ),
        "content": (
            "Componente ch5-slider: Control deslizante analógico para sistemas AV. "
            "Usado para volumen, brillo de pantalla o nivel de iluminación. "
            "Atributos clave: min, max, step, value, orientation, size, handleShape, "
            "handleSize, tooltipShowType, tooltipDisplayType, tapsettable, noHandle, "
            "sendEventOnChange, receiveStateValue. "
            "JSON schema del compilador: "
            + json.dumps({
                "type": "ch5-slider",
                "label": "", "x": 0, "y": 0, "w": 300, "h": 30,
            })
        ),
    },
    "ch5-video": {
        "component_type": "ch5-video",
        "description": (
            "Ventana de visualización de fuente de video HDMI, NDI o "
            "streaming en sistemas AV."
        ),
        "content": (
            "Componente ch5-video: Ventana de visualización de fuentes de video. "
            "Soporta HDMI, NDI y streaming en sistemas de control AV profesional. "
            "Atributos clave: aspectRatio, sourceType, snapshotRefreshRate, size, "
            "url, userId, password, sourceUrl, receiveStateUrl. "
            "JSON schema del compilador: "
            + json.dumps({
                "type": "ch5-video",
                "label": "", "x": 0, "y": 0, "w": 640, "h": 360,
            })
        ),
    },
    "ch5-text": {
        "component_type": "ch5-text",
        "description": (
            "Etiqueta de texto estática o dinámica para mostrar "
            "información en interfaces AV."
        ),
        "content": (
            "Componente ch5-text: Etiqueta de texto para interfaces AV profesionales. "
            "Muestra texto estático (etiquetas, títulos) o valores dinámicos recibidos "
            "del sistema de control. "
            "Atributos clave: label, labelInnerHTML, horizontalAlignment, "
            "verticalAlignment, multilineSupport, truncateText, receiveStateLabel. "
            "JSON schema del compilador: "
            + json.dumps({
                "type": "ch5-text",
                "label": "", "x": 0, "y": 0, "w": 200, "h": 40,
            })
        ),
    },
}


# ─── SINGLETON: modelo de embeddings ──────────────────────────────────────────
# Se carga una sola vez para evitar recargar ~80MB en cada llamada.

_model: SentenceTransformer | None = None


def _get_model() -> SentenceTransformer:
    """Retorna el modelo de embeddings (singleton, carga lazy)."""
    global _model
    if _model is None:
        _model = SentenceTransformer(EMBEDDING_MODEL)
    return _model


def _get_db_path() -> str:
    """Resuelve la ruta de LanceDB relativa al proyecto."""
    db_path = Path(LANCEDB_PATH)
    if not db_path.is_absolute():
        # Subir desde server_mcp/tools/ hasta la raiz del proyecto
        project_root = Path(__file__).parent.parent.parent.parent
        db_path = project_root / db_path
    return str(db_path)


def _format_seed_fallback(component_type: str) -> str:
    """
    Busca un esquema base en _SEED_SCHEMAS para un tipo de componente.

    Si el tipo exacto no existe en los seeds, retorna un mensaje generico
    con todos los tipos soportados.

    Args:
        component_type: Tipo CH5 buscado (ej. "ch5-button").

    Returns:
        String formateado con el esquema seed o mensaje informativo.
    """
    seed = _SEED_SCHEMAS.get(component_type)

    if seed:
        logger.info(
            "Usando SEED_SCHEMA como fallback para '%s'", component_type
        )
        return (
            f"--- {component_type} (SEED fallback) ---\n"
            f"[{seed['component_type']}] {seed['description']}\n"
            f"{seed['content']}\n\n"
        )

    # Tipo completamente desconocido
    supported = ", ".join(sorted(_SEED_SCHEMAS.keys()))
    logger.warning(
        "Tipo '%s' no encontrado en LanceDB ni en SEED_SCHEMAS. "
        "Tipos soportados: %s",
        component_type,
        supported,
    )
    return (
        f"--- {component_type} ---\n"
        f"[No encontrado] Tipo '{component_type}' no soportado. "
        f"Tipos disponibles: {supported}\n\n"
    )


# ─── FUNCION PRINCIPAL ────────────────────────────────────────────────────────

def search_component_schema(component_types: list[str]) -> str:
    """
    Busca en LanceDB los esquemas de componentes CH5 por similitud semantica.

    Para cada tipo de componente en la lista, genera un embedding de la query
    y busca el registro mas relevante en la tabla 'ch5_components'.
    Si LanceDB no tiene resultados, usa el SEED_SCHEMA como fallback.

    Args:
        component_types: Lista de tipos CH5 (ej. ["ch5-button", "ch5-slider"]).
                         Tambien acepta queries en lenguaje natural.

    Returns:
        String formateado con los esquemas encontrados, listo para insertar
        en el prompt de Gemini. Formato:

        --- ch5-button ---
        Boton de accion tactil para control AV...

        --- ch5-slider ---
        Control deslizante analogico...
    """
    if not component_types:
        return ""

    model = _get_model()
    db_path = _get_db_path()

    # Intentar conectar a LanceDB
    table = None
    try:
        db = lancedb.connect(db_path)
        table = db.open_table(TABLE_NAME)
    except Exception as e:
        logger.warning(
            "No se pudo conectar a LanceDB (%s). Usando solo SEED_SCHEMAS.", e
        )

    results_parts = []

    for component_type in component_types:
        # Si no hay tabla LanceDB, ir directo al fallback
        if table is None:
            results_parts.append(_format_seed_fallback(component_type))
            continue

        # Generar embedding de la query
        query_text = f"componente {component_type} para control AV Crestron CH5"
        query_vec = model.encode(query_text)

        # Buscar top-2 resultados mas relevantes
        try:
            results = (
                table.search(query_vec)
                .limit(2)
                .to_pandas()
            )
        except Exception as e:
            logger.warning(
                "Error buscando '%s' en LanceDB: %s. Usando fallback.",
                component_type,
                e,
            )
            results_parts.append(_format_seed_fallback(component_type))
            continue

        if results.empty:
            # ─── FALLBACK A SEED_SCHEMA ───────────────────────────────
            results_parts.append(_format_seed_fallback(component_type))
            continue

        # Formatear resultados de LanceDB
        section = f"--- {component_type} ---\n"
        for _, row in results.iterrows():
            section += f"[{row['component_type']}] {row['description']}\n"
            # Incluir contenido completo del mejor resultado (top-1)
            if _ == results.index[0]:
                content_preview = row["content"][:500]
                section += f"{content_preview}\n"
        section += "\n"
        results_parts.append(section)

    return "\n".join(results_parts)
