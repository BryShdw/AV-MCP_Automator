# AV-MCP Automator

Middleware basado en Model Context Protocol para la generación automática de interfaces nativas de Crestron Construct™ (.cuig ) mediante IA generativa.

**Empresa:** DACER S.A.C. — Miraflores, Lima, Perú  
**Practicante:** Brayan Delgado Oblitas  
**Metodología:** RUP adaptado (desarrollador único) — 14 semanas  

---

## Requisitos

- Python 3.10 o superior (recomendado 3.11+)
- Git
- Crestron Construct™ instalado en el sistema
- Una clave de API válida para Gemini (Google AI Studio)

## Instalación

```bash
# 1. Clonar el repositorio
git clone <url-del-repositorio>
cd AV-MCP_Automator

# 2. Crear y activar el entorno virtual (recomendado)
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt
```

## Configuración del .env

Por seguridad, las credenciales del proyecto no se suben al repositorio. Debes configurar tu propio archivo local basándote en el ejemplo proporcionado.

```bash
# 1. Copiar el archivo de ejemplo
cp .env.example .env

# 2. Editar .env con tus credenciales
```
Asegúrate de editar el archivo `.env` recién creado e introducir tu `GEMINI_API_KEY`.

## Cómo ejecutar el proyecto

Para correr el proyecto completo se necesitan dos terminales (ambas con el entorno virtual activado):

```bash
# 1. (Opcional - Primera vez) Indexar documentación en LanceDB
python src/data_layer/ingest.py

# 2. Iniciar servidor MCP (Terminal 1)
python src/server_mcp/main.py

# 3. Iniciar UI de Cliente (Terminal 2)
streamlit run src/client/app.py
```

### Selección de proyecto Crestron

Al abrir la UI por primera vez, selecciona tu proyecto Crestron Construct:

1. Haz clic en **📂 Explorar...** para abrir el selector de carpetas nativo.
2. Navega hasta `Documents/Crestron/Crestron Construct/Solutions/MiProyecto/`.
3. El sistema detecta automáticamente el nombre del proyecto.
4. Los archivos `.cuig` se generarán en `Solutions/MiProyecto/MiProyecto/`.

> **Nota:** La ruta del proyecto se persiste automáticamente entre sesiones. No necesitas editar el archivo `.env` para configurar la ruta del proyecto.

## Estructura principal del proyecto

```
AV-MCP_Automator/
├── docs/                   # Fases RUP: Inicio y Elaboración
├── src/                    # Fase RUP: Construcción
│   ├── client/             # Capa 1 — UI Streamlit (con selector de proyecto)
│   ├── server_mcp/         # Capa 2 — Servidor FastMCP + Compilador .cuig
│   ├── core_ai/            # Capa 3 — Enrutador IA (Gemini 2.5 Flash-Lite)
│   └── data_layer/         # Capa 4 — LanceDB + documentación fuente
├── tests/                  # Pruebas unitarias e integración
├── deploy/                 # Manual de usuario y guía de despliegue
├── .env.example            # Variables de entorno requeridas (Plantilla segura)
└── requirements.txt        # Dependencias Python
```

## Dependencias importantes (Stack Tecnológico)

| Capa | Tecnología |
|---|---|
| UI Cliente | Streamlit (Python) |
| Servidor MCP / Compilador | FastMCP (Python) |
| IA Principal | Gemini 2.5 Flash-Lite (API) |
| Base Vectorial | LanceDB |
| Ecosistema destino | Crestron Construct™ (.cuig / .cuib) |

## Licencia

Desarrollado para uso interno en DACER S.A.C. Todos los derechos reservados salvo que se indique lo contrario.
