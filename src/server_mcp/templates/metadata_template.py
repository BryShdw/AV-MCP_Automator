"""
Plantilla para el bloque {FileMetadata} del archivo .cuig.

RUP Fase: Construccion — Iteracion 3 (Semana 6)
Fuente: docs/01_Inception/05_analisis_forense_cuig.md — Bloque 1

Valores hardcodeados directamente del analisis forense del proyecto "Exercise 1".
"""
from datetime import datetime, timezone, timedelta


# ─── CONSTANTES DEL FORENSE ──────────────────────────────────────────────────
# Versiones fijas detectadas en archivos .cuig reales de Crestron Construct

SCHEMA_VERSION = "1.0.0.0"
CREATED_BY_APP_HOST = "2.1101.2.0"
LAST_MODIFIED_BY_APP_HOST = "2.1101.2.0"
CREATED_BY_PROJECT_APP = "1.4601.12.0"
LAST_MODIFIED_BY_PROJECT_APP = "1.4601.12.0"
MINIMUM_PROJECT_APP = "1.2600.1"
MINIMUM_APP_HOST = "2.901.0"

# Zona horaria Lima (UTC-5) — usada en timestamps del forense
TZ_LIMA = timezone(timedelta(hours=-5))


def _get_cuig_timestamp() -> str:
    """
    Genera un timestamp en el formato exacto del analisis forense.
    Formato: "2026-06-23 20:49:03.017511-05:00"
    """
    now = datetime.now(TZ_LIMA)
    # strftime no incluye el offset con ':', lo construimos manualmente
    base = now.strftime("%Y-%m-%d %H:%M:%S.%f")
    return f"{base}-05:00"


def build_metadata_block() -> str:
    """
    Genera el bloque {FileMetadata} de un archivo .cuig.

    Todos los valores son hardcodeados segun el analisis forense.
    Los timestamps Created y Modified se generan al momento de la llamada.

    Returns:
        String con el bloque {FileMetadata} completo, listo para insertar en .cuig
    """
    ts = _get_cuig_timestamp()

    return (
        "{FileMetadata}\n"
        f"Schema = \"{SCHEMA_VERSION}\"\n"
        f"CreatedByAppHost = \"{CREATED_BY_APP_HOST}\"\n"
        f"Created = {ts}\n"
        f"LastModifiedByAppHost = \"{LAST_MODIFIED_BY_APP_HOST}\"\n"
        f"Modified = {ts}\n"
        f"CreatedByProjectApp = \"{CREATED_BY_PROJECT_APP}\"\n"
        f"LastModifiedByProjectApp = \"{LAST_MODIFIED_BY_PROJECT_APP}\"\n"
        f"MinimumProjectApp = \"{MINIMUM_PROJECT_APP}\"\n"
        f"MinimumAppHost = \"{MINIMUM_APP_HOST}\""
    )
