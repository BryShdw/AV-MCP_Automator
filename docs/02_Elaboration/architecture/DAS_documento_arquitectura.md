# Documento de Arquitectura del Software (DAS)
**RUP Fase:** Elaboración — IT-2 (Semana 3) | **Va al informe:** ✅ Sí

## 1. Propósito
Describe la arquitectura del AV-MCP Automator, justifica las decisiones de diseño
y sirve como referencia técnica durante la Fase de Construcción.

## 2. Patrón central: "Compilador MCP"
La IA razona sobre un JSON abstracto; Python ensambla deterministamente el .cuig.
Esto elimina alucinaciones en IDs únicos y atributos ccid_* propietarios de Crestron.

## 3. Diagrama de capas
Ver: `AV-MCP_Automator_Contexto_Proyecto.md` → Sección 4.1

## 4. Descripción de capas

### Capa 1 — UI Cliente (Streamlit)
Interfaz web local. Recibe el prompt en lenguaje natural y el tipo de panel destino.
Comunica con el Servidor MCP vía JSON-RPC 2.0 por stdio.

### Capa 2 — Servidor MCP & Compilador (FastMCP)
Núcleo del sistema. Expone tres herramientas:
- `search_tool`: recupera esquemas JSON de componentes CH5 desde LanceDB
- `builder_tool`: ensambla el archivo .cuig a partir del JSON validado
- `cuig_tool`: actualiza el archivo .cuib del proyecto

### Capa 3 — Enrutador IA (Router Layer)
Envía el prompt a Gemini 2.5 Flash-Lite (principal).

### Capa 4 — Base de Datos Vectorial (LanceDB)
Almacena esquemas JSON estandarizados de componentes CH5 y documentación técnica
de Crestron. Recuperación por similitud semántica (embeddings all-MiniLM-L6-v2).

### Capa 5 — Destino (archivos .cuig / .cuib en disco)
Archivos nativos de Crestron Construct escritos en la ruta configurada en .env.
El ingeniero AV los abre directamente en Construct para edición visual.

## 5. Decisiones de arquitectura

| Decisión | Rechazada | Justificación |
|---|---|---|
| IA genera JSON; Python ensambla .cuig | IA genera .cuig directamente | Elimina alucinaciones en IDs y atributos ccid_* |
| LanceDB embebida | ChromaDB / Pinecone | < 1 GB RAM; sin servidor externo; S/. 0 |
| Transporte stdio para MCP | HTTP/SSE | Comunicación local sin overhead de red |

## 6. Vistas UML
- Diagrama de Componentes → `diagrams/diagrama_secuencia_uml.md`
- Diagrama de Secuencia (flujo completo) → `diagrams/diagrama_secuencia_uml.md`
- Flujo del Builder_Tool → `diagrams/flujo_builder_tool.md`
