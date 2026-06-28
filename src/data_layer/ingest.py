"""
Script de ingesta — Carga y vectoriza los esquemas de componentes CH5 en LanceDB.

RUP Fase: Construcción — Iteración 3 (Semana 5, prototipo ejecutable con datos semilla)
Ejecución: python src/data_layer/ingest.py

Proceso:
  1. Lee los archivos .md de raw_docs/ (documentación de componentes CH5)
  2. Hace chunking por sección (MarkdownHeaderTextSplitter)
  3. Genera embeddings con sentence-transformers (all-MiniLM-L6-v2)
  4. Guarda en LanceDB en la tabla 'ch5_components'
"""
import os
import json
import lancedb
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

LANCEDB_PATH  = os.getenv("LANCEDB_PATH", "src/data_layer/lancedb_store")
TABLE_NAME    = os.getenv("LANCEDB_TABLE_NAME", "ch5_components")
RAW_DOCS_PATH = Path("src/data_layer/raw_docs")

# ─── DATOS SEMILLA (Semana 5 — prototipo ejecutable) ──────────────────────────
SEED_SCHEMAS = [
    {
        "id": "ch5-button-v1",
        "component_type": "ch5-button",
        "description": "Botón de acción táctil para control AV. Usado para encender/apagar dispositivos, cambiar fuentes de video o ejecutar macros.",
        "json_schema": json.dumps({ "type": "ch5-button", "label": "", "x": 0, "y": 0, "w": 120, "h": 50, "color": "default" }),
    },
    {
        "id": "ch5-slider-v1",
        "component_type": "ch5-slider",
        "description": "Control deslizante analógico para volumen, brillo de pantalla o nivel de iluminación en salas AV.",
        "json_schema": json.dumps({ "type": "ch5-slider", "label": "", "x": 0, "y": 0, "w": 300, "h": 30 }),
    },
    {
        "id": "ch5-video-v1",
        "component_type": "ch5-video",
        "description": "Ventana de visualización de fuente de video HDMI, NDI o streaming en sistemas de control AV profesional.",
        "json_schema": json.dumps({ "type": "ch5-video", "label": "", "x": 0, "y": 0, "w": 640, "h": 360 }),
    },
]


def ingest_seed_data():
    """Carga los esquemas semilla en LanceDB para el prototipo ejecutable (Semana 5)."""
    # TODO (Semana 5): Implementar conexión LanceDB y carga de datos semilla
    # Referencia: docs/02_Elaboration/diagrams/modelo_datos_lancedb.md
    print("TODO (Semana 5): Implementar ingest_seed_data()")
    for schema in SEED_SCHEMAS:
        print(f"  → Pendiente de indexar: {schema['id']}")


if __name__ == "__main__":
    ingest_seed_data()
