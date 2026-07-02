"""
Script de ingesta — Carga y vectoriza documentación CH5 + esquemas semilla en LanceDB.

RUP Fase: Construcción — Iteración 3 (Semana 5, prototipo ejecutable con datos semilla)
Ejecución: python src/data_layer/ingest.py

Proceso:
  1. Lee los archivos .md de raw_docs/ (documentación de componentes CH5)
  2. Hace chunking por encabezados markdown (#, ##, ###)
  3. Genera embeddings con sentence-transformers (all-MiniLM-L6-v2)
  4. Guarda en LanceDB en la tabla 'ch5_components'
  5. Carga los SEED_SCHEMAS hardcodeados (ch5-button, ch5-slider, ch5-video, ch5-text)
"""
import os
import re
import sys
import json
import time
import pyarrow as pa
import lancedb
import numpy as np

# Fix encoding para Windows (cp1252 no soporta emojis/unicode extendido)
if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
from pathlib import Path
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

# ─── CONFIGURACIÓN ────────────────────────────────────────────────────────────

load_dotenv()

LANCEDB_PATH  = os.getenv("LANCEDB_PATH", "src/data_layer/lancedb_store")
TABLE_NAME    = os.getenv("LANCEDB_TABLE_NAME", "ch5_components")
RAW_DOCS_PATH = Path(__file__).parent / "raw_docs"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
EMBEDDING_DIM   = 384

# Archivos a filtrar (fuentes binarias convertidas a .md — no son documentación)
SKIP_PATTERNS = [".otf.md"]


# ─── DATOS SEMILLA ────────────────────────────────────────────────────────────
# Esquemas JSON estandarizados de los 4 componentes CH5 prioritarios.
# Estos proveen contexto base al Search_Tool incluso sin documentación scrapeada.

SEED_SCHEMAS = [
    {
        "id": "seed_ch5-button",
        "component_type": "ch5-button",
        "description": "Botón de acción táctil para control AV. Usado para encender/apagar dispositivos, cambiar fuentes o ejecutar macros.",
        "content": (
            "Componente ch5-button: Botón de acción táctil para control AV profesional. "
            "Tipos disponibles: default, info, text, danger, warning, success, primary, secondary. "
            "Atributos clave: label, type, shape, size, orientation, iconClass, iconUrl, "
            "backgroundImageUrl, customClass, sendEventOnClick, receiveStateLabel, "
            "receiveStateSelected. "
            "JSON schema del compilador: "
            + json.dumps({
                "type": "ch5-button",
                "label": "",
                "x": 0, "y": 0, "w": 120, "h": 50,
                "color": "default"
            })
        ),
    },
    {
        "id": "seed_ch5-slider",
        "component_type": "ch5-slider",
        "description": "Control deslizante analógico para volumen, brillo o nivel de iluminación en salas AV.",
        "content": (
            "Componente ch5-slider: Control deslizante analógico para sistemas AV. "
            "Usado para volumen, brillo de pantalla o nivel de iluminación. "
            "Atributos clave: min, max, step, value, orientation, size, handleShape, "
            "handleSize, tooltipShowType, tooltipDisplayType, tapsettable, noHandle, "
            "sendEventOnChange, receiveStateValue. "
            "JSON schema del compilador: "
            + json.dumps({
                "type": "ch5-slider",
                "label": "",
                "x": 0, "y": 0, "w": 300, "h": 30,
            })
        ),
    },
    {
        "id": "seed_ch5-video",
        "component_type": "ch5-video",
        "description": "Ventana de visualización de fuente de video HDMI, NDI o streaming en sistemas AV.",
        "content": (
            "Componente ch5-video: Ventana de visualización de fuentes de video. "
            "Soporta HDMI, NDI y streaming en sistemas de control AV profesional. "
            "Atributos clave: aspectRatio, sourceType, snapshotRefreshRate, size, "
            "url, userId, password, sourceUrl, receiveStateUrl. "
            "JSON schema del compilador: "
            + json.dumps({
                "type": "ch5-video",
                "label": "",
                "x": 0, "y": 0, "w": 640, "h": 360,
            })
        ),
    },
    {
        "id": "seed_ch5-text",
        "component_type": "ch5-text",
        "description": "Etiqueta de texto estática o dinámica para mostrar información en interfaces AV.",
        "content": (
            "Componente ch5-text: Etiqueta de texto para interfaces AV profesionales. "
            "Muestra texto estático (etiquetas, títulos) o valores dinámicos recibidos "
            "del sistema de control. "
            "Atributos clave: label, labelInnerHTML, horizontalAlignment, "
            "verticalAlignment, multilineSupport, truncateText, receiveStateLabel. "
            "JSON schema del compilador: "
            + json.dumps({
                "type": "ch5-text",
                "label": "",
                "x": 0, "y": 0, "w": 200, "h": 40,
            })
        ),
    },
]


# ─── COMPONENTES CH5 CONOCIDOS (para inferencia de tipo) ──────────────────────

CH5_COMPONENT_TAGS = [
    "ch5-button", "ch5-slider", "ch5-video", "ch5-text",
    "ch5-toggle", "ch5-tab-button", "ch5-datetime", "ch5-textinput",
    "ch5-image", "ch5-dpad", "ch5-keypad", "ch5-select",
    "ch5-spinner", "ch5-overlay-panel", "ch5-color-chip",
    "ch5-color-picker", "ch5-segmented-gauge", "ch5-signal-level-gauge",
    "ch5-wifi-signal-level-gauge", "ch5-animation",
    "ch5-button-list", "ch5-subpage-reference-list", "ch5-triggerview",
    "ch5-video-switcher", "ch5-qr-code",
]


# ─── FUNCIONES DE CHUNKING ────────────────────────────────────────────────────

def _should_skip_file(filename: str) -> bool:
    """Filtra archivos que no contienen documentación útil (e.g., fuentes .otf)."""
    return any(pattern in filename for pattern in SKIP_PATTERNS)


def _chunk_markdown_by_headers(text: str) -> list[str]:
    """
    Divide texto Markdown en chunks usando encabezados (#, ##, ###) como separadores.
    
    Cada chunk conserva su encabezado como primera línea para mantener contexto
    semántico en el embedding.
    
    Returns:
        Lista de strings, cada uno representando una sección del documento.
    """
    # Patrón: línea que empieza con 1-3 '#' seguido de espacio
    header_pattern = re.compile(r"^(#{1,3})\s+", re.MULTILINE)
    
    # Encontrar posiciones de todos los encabezados
    splits = list(header_pattern.finditer(text))
    
    if not splits:
        # Sin encabezados → el archivo entero es un chunk
        stripped = text.strip()
        return [stripped] if stripped else []
    
    chunks = []
    
    # Si hay contenido antes del primer encabezado, incluirlo
    preamble = text[:splits[0].start()].strip()
    if preamble:
        chunks.append(preamble)
    
    # Crear un chunk por cada sección entre encabezados
    for i, match in enumerate(splits):
        start = match.start()
        end = splits[i + 1].start() if i + 1 < len(splits) else len(text)
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
    
    return chunks


def _infer_component_type(text: str) -> str:
    """
    Infiere el tipo de componente CH5 mencionado en el chunk.
    
    Busca tags CH5 en el contenido. Si encuentra uno específico, lo retorna.
    Si encuentra múltiples o ninguno, retorna 'general'.
    """
    text_lower = text.lower()
    found = []
    
    for tag in CH5_COMPONENT_TAGS:
        # Buscar el tag como palabra (con < o espacio alrededor)
        if tag in text_lower:
            found.append(tag)
    
    if len(found) == 1:
        return found[0]
    
    # Si encontramos múltiples, intentar priorizar por el título (primer encabezado)
    if len(found) > 1:
        first_line = text_lower.split("\n")[0]
        for tag in found:
            if tag in first_line:
                return tag
        # Si no hay uno claro en el título, marcar como general
        return "general"
    
    return "general"


# ─── PIPELINE DE INGESTA ──────────────────────────────────────────────────────

def load_and_chunk_docs() -> list[dict]:
    """
    Lee todos los .md de raw_docs/ y los divide en chunks por encabezado.
    
    Returns:
        Lista de diccionarios con keys: id, component_type, description, content
    """
    records = []
    files_processed = 0
    files_skipped = 0
    
    if not RAW_DOCS_PATH.exists():
        print(f"⚠️  Carpeta raw_docs no encontrada: {RAW_DOCS_PATH}")
        return records
    
    md_files = sorted(RAW_DOCS_PATH.glob("*.md"))
    
    if not md_files:
        print("⚠️  No se encontraron archivos .md en raw_docs/")
        return records
    
    for md_file in md_files:
        # Filtrar archivos no-documentación
        if _should_skip_file(md_file.name):
            files_skipped += 1
            continue
        
        text = md_file.read_text(encoding="utf-8", errors="replace")
        
        if not text.strip():
            files_skipped += 1
            continue
        
        chunks = _chunk_markdown_by_headers(text)
        file_stem = md_file.stem  # nombre sin extensión
        
        for idx, chunk_text in enumerate(chunks):
            # Filtrar chunks muy cortos (< 30 chars) — no aportan semánticamente
            if len(chunk_text) < 30:
                continue
            
            record = {
                "id": f"{file_stem}_{idx}",
                "component_type": _infer_component_type(chunk_text),
                "description": chunk_text[:200].replace("\n", " ").strip(),
                "content": chunk_text,
            }
            records.append(record)
        
        files_processed += 1
    
    print(f"📂 Archivos procesados: {files_processed}  |  Saltados: {files_skipped}")
    print(f"📝 Chunks generados de documentación: {len(records)}")
    
    return records


def build_seed_records() -> list[dict]:
    """
    Construye los registros de datos semilla de los 4 componentes CH5 prioritarios.
    
    Returns:
        Lista de diccionarios con keys: id, component_type, description, content
    """
    records = []
    for seed in SEED_SCHEMAS:
        records.append({
            "id": seed["id"],
            "component_type": seed["component_type"],
            "description": seed["description"][:200],
            "content": seed["content"],
        })
    return records


def generate_embeddings(texts: list[str], model: SentenceTransformer) -> np.ndarray:
    """
    Genera embeddings para una lista de textos usando el modelo sentence-transformers.
    
    Args:
        texts: Lista de strings a vectorizar.
        model: Modelo SentenceTransformer cargado.
    
    Returns:
        Array numpy de shape (len(texts), EMBEDDING_DIM).
    """
    print(f"🧠 Generando embeddings para {len(texts)} registros...")
    embeddings = model.encode(
        texts,
        show_progress_bar=True,
        batch_size=64,
        normalize_embeddings=True,
    )
    return embeddings


def index_to_lancedb(records: list[dict], embeddings: np.ndarray) -> int:
    """
    Escribe los registros con sus embeddings en la tabla LanceDB.
    
    Si la tabla ya existe, se elimina y recrea (ingesta limpia para prototipo IT-3).
    
    Args:
        records: Lista de diccionarios con id, component_type, description, content.
        embeddings: Array numpy con los vectores correspondientes.
    
    Returns:
        Número de registros indexados.
    """
    # Resolver la ruta de LanceDB relativa al proyecto
    db_path = Path(LANCEDB_PATH)
    if not db_path.is_absolute():
        db_path = Path(__file__).parent.parent.parent / db_path
    
    print(f"💾 Conectando a LanceDB en: {db_path}")
    db = lancedb.connect(str(db_path))
    
    # Preparar datos para LanceDB
    data = []
    for i, record in enumerate(records):
        data.append({
            "id": record["id"],
            "component_type": record["component_type"],
            "description": record["description"],
            "content": record["content"],
            "vector": embeddings[i].tolist(),
        })
    
    # Definir schema con PyArrow
    schema = pa.schema([
        pa.field("id", pa.string()),
        pa.field("component_type", pa.string()),
        pa.field("description", pa.string()),
        pa.field("content", pa.string()),
        pa.field("vector", pa.list_(pa.float32(), EMBEDDING_DIM)),
    ])
    
    # Eliminar tabla existente si la hay (ingesta limpia)
    existing_tables = db.list_tables()
    if TABLE_NAME in existing_tables:
        db.drop_table(TABLE_NAME)
        print(f"🗑️  Tabla '{TABLE_NAME}' existente eliminada.")
    
    # Crear tabla con datos
    table = db.create_table(TABLE_NAME, data=data, schema=schema)
    
    count = table.count_rows()
    print(f"✅ Tabla '{TABLE_NAME}' creada con {count} registros.")
    
    return count


def run_ingest():
    """
    Pipeline completo de ingesta:
      1. Cargar modelo de embeddings
      2. Leer y chunkear documentación de raw_docs/
      3. Agregar seed schemas
      4. Generar embeddings
      5. Indexar en LanceDB
    """
    print("=" * 70)
    print("  AV-MCP Automator — Ingesta de documentación CH5 en LanceDB")
    print("  RUP Fase: Construcción — IT-3")
    print("=" * 70)
    print()
    
    start_time = time.time()
    
    # 1. Cargar modelo de embeddings
    print(f"📦 Cargando modelo de embeddings: {EMBEDDING_MODEL}")
    print("   (Primera ejecución descargará ~80MB)")
    model = SentenceTransformer(EMBEDDING_MODEL)
    print(f"   ✓ Modelo cargado. Dimensión de embeddings: {model.get_embedding_dimension()}")
    print()
    
    # 2. Leer y chunkear documentación
    print("─── Fase 1: Chunking de documentación ─────────────────────────────")
    doc_records = load_and_chunk_docs()
    print()
    
    # 3. Agregar seeds
    print("─── Fase 2: Datos semilla ─────────────────────────────────────────")
    seed_records = build_seed_records()
    print(f"🌱 Seeds cargados: {len(seed_records)} ({', '.join(s['component_type'] for s in seed_records)})")
    print()
    
    # 4. Combinar todos los registros
    all_records = doc_records + seed_records
    
    if not all_records:
        print("❌ No hay registros para indexar. Abortando.")
        return
    
    # 5. Generar embeddings
    print("─── Fase 3: Generación de embeddings ──────────────────────────────")
    # Usar 'content' como texto fuente para los embeddings (más contexto que 'description')
    texts = [r["content"] for r in all_records]
    embeddings = generate_embeddings(texts, model)
    print()
    
    # 6. Indexar en LanceDB
    print("─── Fase 4: Indexación en LanceDB ─────────────────────────────────")
    total_indexed = index_to_lancedb(all_records, embeddings)
    
    # 7. Resumen final
    elapsed = time.time() - start_time
    print()
    print("=" * 70)
    print("  RESUMEN DE INGESTA")
    print("=" * 70)
    print(f"  📝 Chunks de documentación:  {len(doc_records)}")
    print(f"  🌱 Schemas semilla:          {len(seed_records)}")
    print(f"  ✅ Total registros indexados: {total_indexed}")
    print(f"  ⏱️  Tiempo total:             {elapsed:.1f}s")
    print(f"  💾 Base de datos:             {LANCEDB_PATH}")
    print(f"  📊 Tabla:                     {TABLE_NAME}")
    print("=" * 70)


# ─── ENTRY POINT ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    run_ingest()
