# ACTA DE APROBACIÓN DE ARQUITECTURA
**Código:** ACTA-003
**Fecha:** 09 de mayo de 2026
**Hito RUP:** LCA (Lifecycle Architecture)
**Fase:** Fin de Elaboración

## Descripción de la Arquitectura Aprobada
Se ha validado y aprobado la arquitectura en 5 capas basada en el patrón "**Compilador MCP**". Este modelo delega exclusivamente el razonamiento lógico espacial a la inteligencia artificial (Gemini) en formato JSON, y asigna el ensamblaje sintáctico propietario (formato Crestron `.cuig`) a un script Python determinista.

Las cinco capas son:
1. **UI Cliente:** Streamlit
2. **Servidor MCP y Compilador:** FastMCP (Python)
3. **Router IA:** Gemini Flash-Lite
4. **Base de Datos:** LanceDB (Vectorial)
5. **Salida/Destino:** Archivos Crestron `.cuig` / `.cuib` en disco

## Decisiones Arquitectónicas Clave
| Decisión | Alternativa rechazada | Justificación |
|---|---|---|
| **Patrón Compilador MCP** | IA genera el `.cuig` directamente | Prevención de alucinaciones en sintaxis propietaria de Crestron y reducción drástica del uso de tokens (contexto API). |
| **Almacenamiento RAG con LanceDB** | ChromaDB / Base de datos SQL | LanceDB es embebida, opera bajo 1GB de RAM (ideal para hardware local limitado) y provee búsqueda vectorial rápida. |
| **Modelo Gemini 2.5 Flash-Lite** | Ollama Local / GPT-4o | Cuota gratuita masiva (1,000 req/día) que permite coste de licencias cero (S/. 0), cumpliendo la restricción presupuestaria. |
| **Separación de Lógica Visual** | Uso de Flexbox / Grid | Crestron Construct requiere posicionamiento absoluto estricto (x, y, w, h); la arquitectura transpone coordenadas para compatibilidad. |

## Evidencia del Prototipo Ejecutable
Durante la validación de este hito, se demostró:
1. La recuperación semántica exitosa de un esquema JSON desde LanceDB.
2. La generación y validación Pydantic de la estructura de un layout básico.
3. El primer ensamblaje estructural programático de un archivo con los cuatro bloques base de un archivo `.cuig`.

## Aprobación
Con este documento se da por aprobada la arquitectura base y se autoriza el avance formal hacia la **Fase de Construcción**, cuyo foco será poblar las plantillas de los componentes y estabilizar el ensamblador.

_________________________  _________________________  _________________________
Brayan Delgado Oblitas     [Tutor DACER]              [Tutora universitaria]
Practicante                Supervisor empresa         Tutora académica
