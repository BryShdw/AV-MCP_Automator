# Modelo de Datos — LanceDB
**RUP Fase:** Elaboración — IT-2 (Semana 4) | **Va al informe:** ✅ Sí

## Tabla: `ch5_components`

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | string | Identificador único del esquema (ej. "ch5-button-v1") |
| `component_type` | string | Nombre del tag CH5 (ej. "ch5-button") |
| `description` | string | Descripción semántica para búsqueda vectorial |
| `json_schema` | string (JSON) | Esquema JSON que la IA debe completar |
| `html_attributes` | string (JSON) | Atributos CH5 requeridos en el bloque {Html} |
| `vector` | vector[384] | Embedding del campo description (all-MiniLM-L6-v2) |

## Fuente de los datos
Los esquemas se definen durante la Fase de Elaboración basándose en el
análisis forense de archivos .cuig y la documentación oficial de Crestron CH5.
No dependen de insumos externos al proyecto.

## Script de carga: `src/data_layer/ingest.py`
