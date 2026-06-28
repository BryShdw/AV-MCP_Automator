# AV-MCP Automator

Middleware basado en Model Context Protocol para la generación automática de interfaces
nativas de Crestron Construct™ (.cuig / .cuib) mediante IA generativa.

**Empresa:** DACER S.A.C. — Miraflores, Lima, Perú  
**Practicante:** Brayan Delgado Oblitas  
**Metodología:** RUP adaptado (desarrollador único) — 14 semanas  

---

## Estructura del proyecto

```
AV-MCP_Automator/
├── docs/                   # Fases RUP: Inicio y Elaboración
│   ├── 01_Inception/       # Visión, casos de uso, requisitos, riesgos, glosario
│   └── 02_Elaboration/     # DAS, esquema JSON compilador, diagramas UML
│       ├── architecture/
│       ├── schemas/
│       └── diagrams/
├── src/                    # Fase RUP: Construcción
│   ├── client/             # Capa 1 — UI Streamlit
│   ├── server_mcp/         # Capa 2 — Servidor FastMCP + Compilador .cuig
│   │   ├── tools/          # search_tool, builder_tool, cuig_tool
│   │   └── templates/      # Plantillas Python por componente CH5
│   ├── core_ai/            # Capa 3 — Enrutador IA (Gemini → Ollama fallback)
│   │   ├── prompts/        # System prompts
│   │   └── schemas/        # Modelos Pydantic para validar JSON de Gemini
│   └── data_layer/         # Capa 4 — LanceDB + documentación fuente
│       ├── raw_docs/       # Docs .md de Crestron para indexar
│       └── lancedb_store/  # Base vectorial embebida (generada en runtime)
├── tests/                  # Pruebas unitarias e integración
├── deploy/
│   └── manuals/            # Manual de usuario y guía de despliegue (Fase Transición)
├── .env.example            # Variables de entorno requeridas
└── requirements.txt        # Dependencias Python
```

## Inicio rápido

```bash
# 1. Clonar e instalar dependencias
pip install -r requirements.txt

# 2. Configurar variables de entorno
cp .env.example .env
# Editar .env con tu clave de API de Gemini

# 3. Indexar documentación en LanceDB
python src/data_layer/ingest.py

# 4. Iniciar servidor MCP
python src/server_mcp/main.py

# 5. Iniciar UI (en otra terminal)
streamlit run src/client/app.py
```

## Stack tecnológico

| Capa | Tecnología |
|---|---|
| UI Cliente | Streamlit (Python) |
| Servidor MCP / Compilador | FastMCP (Python) |
| IA Principal | Gemini 2.5 Flash-Lite (API) |
| IA Fallback | Ollama + Llama 3.2 3B (Q4_K_M) |
| Base Vectorial | LanceDB |
| Ecosistema destino | Crestron Construct™ (.cuig / .cuib) |

## Documentación del proyecto

Ver `docs/02_Elaboration/architecture/AV-MCP_Automator_Contexto_Proyecto.md`
para el documento maestro de contexto del proyecto.
