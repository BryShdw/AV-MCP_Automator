"""
Plantilla para el bloque {FileMetadata} del archivo .cuig.
RUP Fase: Construcción — Iteración 3 (Semana 6)
"""
from datetime import datetime


def build_metadata_block(page_name: str, construct_version: str = "2.0") -> str:
    """
    Genera el bloque {FileMetadata} de un archivo .cuig.

    Args:
        page_name:         Nombre de la página
        construct_version: Versión de Crestron Construct (detectada en análisis forense)

    Returns:
        String con el bloque {FileMetadata} completo
    """
    # TODO (Semana 6): Completar con el formato exacto detectado en el análisis forense
    # de los archivos .cuig reales de DACER (docs/01_Inception/05_analisis_forense_cuig.md)
    now = datetime.now().isoformat()
    return f"""{{FileMetadata}}
PageName={page_name}
ConstructVersion={construct_version}
CreatedDate={now}
{{/FileMetadata}}"""
