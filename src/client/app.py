"""
Capa 1 — UI Cliente (Streamlit)
Interfaz completa para el especialista AV de DACER S.A.C.

RUP Fase: Construccion — Iteracion 4 (Semana 10)

Flujo directo (sin servidor MCP en esta sesion):
  app.py → search_tool.search_component_schema()
         → router.get_layout_from_ai()
         → builder_tool.build_cuig_file()
         → Mostrar resultado en UI
"""
import sys
import json
import os
import time
import platform
from pathlib import Path

# ─── RESOLVER IMPORTS ─────────────────────────────────────────────────────────
# Streamlit ejecuta app.py como script directo, no como modulo de paquete.
# Agregar la raiz del proyecto a sys.path permite importar src.* correctamente.
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st
from dotenv import load_dotenv

load_dotenv(PROJECT_ROOT / ".env")

GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

# Importar capa 3 (Router IA) directamente, pero comunicarse con Capa 2 (MCP Server) vía JSON-RPC
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from src.core_ai.router import (
    get_layout_from_ai, load_system_prompt,
    format_panel_constraints, build_user_prompt,
)

async def call_mcp_tool(tool_name: str, arguments: dict) -> any:
    """Invoca una herramienta en el servidor MCP vía stdio."""
    server_script = str(PROJECT_ROOT / "src" / "server_mcp" / "main.py")
    server_params = StdioServerParameters(
        command=sys.executable,
        args=[server_script],
        env=os.environ.copy()
    )
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool(tool_name, arguments)
            # FastMCP devuelve TextContent, devolvemos el texto del primer resultado
            if result.content and len(result.content) > 0:
                return result.content[0].text
            return None


# ─── BOOTSTRAP ICONS & ICON HELPER ───────────────────────────────────────────
st.markdown(
    '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.13.1/font/bootstrap-icons.min.css">',
    unsafe_allow_html=True
)

def icon(name: str, size: int = 16, color: str = "currentColor") -> str:
    """
    Genera HTML de un icono de Bootstrap Icons para usar en st.markdown().
    name: nombre del icono sin el prefijo 'bi-' (ej: "folder2-open", "cpu", "check-circle")
    """
    return (
        f'<i class="bi bi-{name}" '
        f'style="font-size:{size}px; color:{color}; vertical-align:middle;"></i>'
    )



# ─── CATALOGO DE PANELES CRESTRON ─────────────────────────────────────────────
# Fuente: docs.crestron.com 2024 — Resoluciones nativas de cada modelo

CRESTRON_PANELS = {
    # Wireless
    "TST-1080 (Wireless 10.1\")":   {"w": 1920, "h": 1080, "ratio": "16:9",  "category": "Wireless"},
    "TST-902 (Wireless 8.7\")":     {"w": 1008, "h": 588,  "ratio": "12:7",  "category": "Wireless"},
    "TSR-310 (Wireless 3\" Portrait)": {"w": 320, "h": 480, "ratio": "3:2", "category": "Wireless"},

    # Wall Mount
    "TSW-1070 (Wall 10.1\")":       {"w": 1920, "h": 1200, "ratio": "16:10", "category": "Wall Mount"},
    "TSW-770 (Wall 7\")":           {"w": 1280, "h": 800,  "ratio": "16:10", "category": "Wall Mount"},
    "TSW-570 (Wall 5\")":           {"w": 1280, "h": 720,  "ratio": "16:9",  "category": "Wall Mount"},
    "TSW-570P (Wall 5\" Portrait)": {"w": 720,  "h": 1280, "ratio": "16:9",  "category": "Wall Mount"},

    # Tabletop
    "TS-1070 (Tabletop 10.1\")":    {"w": 1920, "h": 1200, "ratio": "16:10", "category": "Tabletop"},
    "TS-770 (Tabletop 7\")":        {"w": 1280, "h": 800,  "ratio": "16:10", "category": "Tabletop"},
    "TS-1542 (Tabletop 15.6\")":    {"w": 1920, "h": 1080, "ratio": "16:9",  "category": "Tabletop"},
    "FT-TS600-B (Tabletop 5\")":    {"w": 800,  "h": 480,  "ratio": "15:9",  "category": "Tabletop"},

    # Display
    "TSD-2220 (Display 21.5\")":    {"w": 1920, "h": 1080, "ratio": "16:9",  "category": "Display"},

    # Virtual
    "Web Xpanel (PC/Tablet)":       {"w": 1280, "h": 800,  "ratio": "16:10", "category": "Virtual"},

    # Personalizado
    "Personalizado":              {"w": None, "h": None, "ratio": "custom", "category": "Custom"},
}

# Tipos CH5 soportados — se pasan al Search_Tool
CH5_TYPES = ["ch5-button", "ch5-slider", "ch5-video", "ch5-text", "ch5-toggle"]

# Archivo de configuracion local para persistir la ultima ruta usada
CONFIG_FILE = PROJECT_ROOT / ".av_mcp_config.json"


# ─── PLANTILLAS DE SALA POR CASO DE USO ──────────────────────────────────────
# Prompts pre-construidos para los tipos de sala mas comunes en Pro AV.
# El usuario selecciona su tipo de sala y el prompt se pre-llena.

ROOM_TEMPLATES = {
    "Sala de Conferencias": {
        "prompt": (
            "Crea una interfaz para sala de conferencias corporativa con: "
            "sección superior de control de video (botón Encender proyector, "
            "botón Apagar proyector, selector de fuente HDMI 1/HDMI 2/Laptop), "
            "sección central de audio (slider de volumen principal, botón Mute, "
            "slider de volumen de micrófonos), sección inferior de iluminación "
            "(slider de brillo, botones Modo Presentación/Modo Video/Apagado). "
            "Usar layout en tres filas horizontales con separación clara entre secciones."
        ),
        "description": "Proyector + audio + iluminación",
        "icon": "briefcase",
    },
    "Aula / Salón Educativo": {
        "prompt": (
            "Crea una interfaz para aula educativa con: fila superior con botón "
            "Encender pantalla interactiva, botón Apagar, botón Pantalla completa. "
            "Fila media con slider de volumen del sistema y botón Mute. Fila inferior "
            "con 4 botones de fuente: PC Docente, HDMI Laptop, Cámara Documento, "
            "Streaming. Incluir botón grande de Apagado Total en esquina inferior derecha."
        ),
        "description": "Pantalla interactiva + fuentes + volumen",
        "icon": "mortarboard",
    },
    "Sala VIP / Hospitalidad": {
        "prompt": (
            "Crea una interfaz premium para sala VIP con: sección de bienvenida con "
            "título 'Control de Sala', sección de iluminación con slider de brillo y "
            "3 botones de ambiente (Reunión/Presentación/Relajado), sección audiovisual "
            "con botón Encender TV, selector de fuente (Cable/AppleTV/HDMI), slider de "
            "volumen. Diseño elegante con elementos centrados y espaciado generoso."
        ),
        "description": "Iluminación + TV + fuentes multimedia",
        "icon": "gem",
    },
    "Sala de Control / NOC": {
        "prompt": (
            "Crea una interfaz para sala de control con múltiples pantallas: fila de "
            "monitoreo con 3 indicadores de estado (verde/rojo), sección de control de "
            "video wall con botones de layout (1x1, 2x2, 3x3), sección de audio con "
            "slider de volumen y selector de fuente de audio, sección de accesos rápidos "
            "con botones Modo Normal/Modo Alarma/Modo Silencio."
        ),
        "description": "Video wall + monitoreo + accesos rápidos",
        "icon": "cpu",
    },
    "Auditorio / Teatro": {
        "prompt": (
            "Crea una interfaz para auditorio con: control de escenario (botones Telón "
            "Arriba/Abajo, slider de iluminación de escenario), control de proyección "
            "(botón Encender proyector, selector de fuente, slider de brillo), control "
            "de audio (slider de volumen principal, slider de micrófonos, botón Mute "
            "general), control de iluminación de sala (slider de intensidad, botones "
            "Modo Espectáculo/Modo Intermedio/Modo Completo)."
        ),
        "description": "Escenario + proyección + audio + sala",
        "icon": "easel",
    },
    "Personalizado": {
        "prompt": "",
        "description": "Escribe tu propio prompt desde cero",
        "icon": "pencil",
    },
}






# ─── FUNCIONES DE PROYECTO ────────────────────────────────────────────────────

def get_solutions_default_path() -> str:
    """Retorna la ruta por defecto de Solutions segun el SO."""
    if platform.system() == "Windows":
        return os.path.join(
            os.path.expanduser("~"),
            "Documents", "Crestron", "Crestron Construct", "Solutions",
        )
    return os.path.expanduser("~")


def select_folder() -> str | None:
    """
    Abre un dialogo nativo de seleccion de carpeta usando tkinter.
    Retorna la ruta seleccionada o None si se cancelo.
    """
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    root.wm_attributes("-topmost", 1)
    folder = filedialog.askdirectory(
        title="Selecciona la carpeta de tu proyecto Crestron Construct",
        initialdir=get_solutions_default_path(),
    )
    root.destroy()
    return folder if folder else None


def get_cuig_output_path(project_root: str) -> str:
    """
    Dado Solutions/MiProyecto/, retorna Solutions/MiProyecto/MiProyecto/
    que es donde Crestron Construct espera los archivos .cuig.
    """
    project_name = os.path.basename(project_root.rstrip("/\\"))
    inner_path = os.path.join(project_root, project_name)

    if not os.path.exists(inner_path):
        # El proyecto existe pero la carpeta interna no — crearla
        os.makedirs(inner_path, exist_ok=True)

    return inner_path


def get_cuib_path(project_root: str) -> str:
    """Retorna la ruta al archivo .cuib del proyecto."""
    project_name = os.path.basename(project_root.rstrip("/\\"))
    inner_path = os.path.join(project_root, project_name)
    return os.path.join(inner_path, f"{project_name}.cuib")


def list_existing_pages(output_path: str) -> list[str]:
    """Lista los archivos .cuig existentes en la carpeta de salida."""
    if not os.path.exists(output_path):
        return []
    return sorted([f for f in os.listdir(output_path) if f.endswith(".cuig")])


def save_last_project(path: str) -> None:
    """Guarda la ultima ruta de proyecto usada en el archivo de configuracion local."""
    CONFIG_FILE.write_text(json.dumps({"last_project": path}, indent=2), encoding="utf-8")


def load_last_project() -> str | None:
    """Carga la ultima ruta de proyecto desde el archivo de configuracion local."""
    if CONFIG_FILE.exists():
        try:
            data = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
            return data.get("last_project")
        except (json.JSONDecodeError, KeyError):
            return None
    return None


def _extract_component_types(user_input: str) -> list[str]:
    """
    Infiere que tipos de componentes CH5 se mencionan en el prompt del usuario.

    Busca palabras clave en espanol e ingles para mapear a tipos CH5.
    Siempre incluye ch5-button y ch5-text como base minima.
    """
    keywords_map = {
        "ch5-button": [
            "boton", "botón", "button", "encender", "apagar",
            "on", "off", "macro", "activar", "desactivar",
        ],
        "ch5-slider": [
            "slider", "volumen", "brillo", "deslizante", "nivel",
            "iluminacion", "iluminación", "fader", "volume",
        ],
        "ch5-video": [
            "video", "camara", "cámara", "hdmi", "ndi",
            "streaming", "pantalla", "fuente",
        ],
        "ch5-text": [
            "texto", "etiqueta", "label", "titulo", "título",
            "nombre", "estado", "text",
        ],
        "ch5-toggle": [
            "toggle", "interruptor", "switch", "mute",
            "silenciar", "encendido", "on/off",
        ],
        "ch5-header": [
            "título", "titulo", "header", "encabezado", "h1",
        ],
    }

    input_lower = user_input.lower()
    detected = set()

    for ch5_type, keywords in keywords_map.items():
        for kw in keywords:
            if kw in input_lower:
                detected.add(ch5_type)
                break

    # Minimo: siempre buscar button y text (son los mas comunes)
    detected.add("ch5-button")
    detected.add("ch5-text")

    return sorted(detected)


def analyze_prompt_quality(prompt: str) -> dict:
    """
    Analiza el prompt del usuario y sugiere mejoras.
    Sin llamada a IA — solo reglas locales basadas en palabras clave.

    Returns:
        Dict con score (0-100), issues (list[str]), suggestions (list[str]).
    """
    issues = []
    suggestions = []
    score = 100

    # Verificar longitud minima
    word_count = len(prompt.split())
    if word_count < 10:
        issues.append("El prompt es muy corto")
        suggestions.append(
            "Describe al menos los dispositivos principales y la organización"
        )
        score -= 40

    # Verificar mencion de controles especificos
    control_words = [
        "botón", "boton", "slider", "control", "encender", "apagar",
        "volumen", "brillo", "fuente", "button", "toggle", "mute",
    ]
    has_controls = any(w in prompt.lower() for w in control_words)
    if not has_controls:
        issues.append("No se mencionan controles específicos")
        suggestions.append("Agrega botones, sliders u otros controles concretos")
        score -= 30

    # Verificar indicaciones de layout/organizacion
    layout_words = [
        "fila", "columna", "sección", "seccion", "izquierda", "derecha",
        "superior", "inferior", "centro", "layout", "arriba", "abajo",
    ]
    has_layout = any(w in prompt.lower() for w in layout_words)
    if not has_layout:
        suggestions.append(
            "Indica cómo organizar los elementos (filas, secciones, columnas)"
        )
        score -= 10

    # Verificar que se mencione el tipo de sala o contexto
    context_words = [
        "sala", "aula", "auditorio", "oficina", "conferencia", "reunión",
        "reunion", "teatro", "hotel", "control", "vip", "educativ",
    ]
    has_context = any(w in prompt.lower() for w in context_words)
    if not has_context:
        suggestions.append("Menciona el tipo de sala o contexto de uso")
        score -= 10

    # NUEVA VALIDACIÓN: detectar solicitud de múltiples páginas
    multi_page_words = ["pantalla de inicio", "pantalla de control", "primera pantalla",
                        "segunda pantalla", "página de inicio", "otra página",
                        "siguiente pantalla", "flujo de pantallas", "varias páginas"]
    mentions_multi_page = sum(1 for w in multi_page_words if w in prompt.lower())

    if mentions_multi_page >= 2:
        issues.append("El prompt parece describir múltiples páginas")
        suggestions.append(
            "Este sistema genera UNA página por solicitud. Considera dividir tu "
            "descripción en generaciones separadas (primero la página de inicio, "
            "luego la de control) para obtener mejores resultados."
        )
        score -= 25

    return {"score": max(score, 0), "issues": issues, "suggestions": suggestions}


# ─── PAGE CONFIG ──────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="AV-MCP Automator",
    page_icon=":material/settings_input_hdmi:",
    layout="wide",
)

# ─── INICIALIZAR SESSION STATE ────────────────────────────────────────────────

if "project_path" not in st.session_state:
    last = load_last_project()
    if last and os.path.isdir(last):
        st.session_state["project_path"] = last
        st.session_state["project_name"] = os.path.basename(last.rstrip("/\\"))
    else:
        st.session_state["project_path"] = ""
        st.session_state["project_name"] = ""

if "selected_template" not in st.session_state:
    st.session_state["selected_template"] = "Personalizado"

# ─── SIDEBAR ──────────────────────────────────────────────────────────────────

with st.sidebar:
    st.image(
        "https://img.icons8.com/color/96/control-panel.png",
        width=64,
    )
    st.title("AV-MCP Automator")
    st.caption("DACER S.A.C. — Miraflores, Lima")

    st.divider()

    # ─── Selector de panel agrupado ───────────────────────────────────
    st.markdown(
        f'### {icon("display", 20)} Panel de destino',
        unsafe_allow_html=True
    )

    panel_options = list(CRESTRON_PANELS.keys())
    selected_panel = st.selectbox(
        "Selecciona el panel:",
        options=panel_options,
        index=0,
        help="Define las dimensiones del canvas según el panel Crestron de destino",
    )

    panel_info = CRESTRON_PANELS[selected_panel]

    # Si es personalizado, mostrar inputs de dimensiones
    if panel_info["w"] is None:
        col1, col2 = st.columns(2)
        with col1:
            custom_w = st.number_input(
                "Ancho (px):", min_value=320, max_value=3840,
                value=1280, step=1,
            )
        with col2:
            custom_h = st.number_input(
                "Alto (px):", min_value=240, max_value=2160,
                value=800, step=1,
            )
        canvas_w, canvas_h = custom_w, custom_h
    else:
        canvas_w = panel_info["w"]
        canvas_h = panel_info["h"]

    # Info de resolución y categoría
    ratio_display = f"{canvas_w} × {canvas_h} px"
    category = panel_info["category"]
    st.markdown(
        f'{icon("rulers", 14)} Resolución: **{ratio_display}** | Categoría: {category}',
        unsafe_allow_html=True
    )

    # Mini preview proporcional del canvas
    aspect = canvas_w / canvas_h
    preview_w = 200
    preview_h = int(preview_w / aspect)
    st.markdown(
        f'<div style="width:{preview_w}px;height:{preview_h}px;border:2px solid #444;'
        f'background:#1a1a2e;border-radius:4px;display:flex;align-items:center;'
        f'justify-content:center;color:#888;font-size:11px;">'
        f'{ratio_display}'
        f'</div>',
        unsafe_allow_html=True,
    )

    st.divider()
    st.markdown(
        f"**Stack:** Gemini Pro · LanceDB · FastMCP\n\n"
        f"**Fase RUP:** Construcción — IT-4"
    )

# ─── MAIN AREA ────────────────────────────────────────────────────────────────

st.markdown(
    f'# {icon("display", 32)} Generador de Interfaces Crestron CH5',
    unsafe_allow_html=True
)
st.markdown(
    "Describe en lenguaje natural la pantalla de control que necesitas. "
    "El sistema genera automáticamente un archivo **`.cuig`** nativo de "
    "Crestron Construct."
)

# ─── SELECTOR DE PROYECTO ────────────────────────────────────────────────────

st.markdown(
    f'### {icon("folder2-open", 20)} Proyecto Crestron Construct',
    unsafe_allow_html=True
)

col_path, col_browse = st.columns([4, 1])

with col_path:
    manual_path = st.text_input(
        "Ruta de la carpeta del proyecto:",
        value=st.session_state.get("project_path", ""),
        placeholder=r"C:\Users\...\Solutions\MiProyecto",
        help="Selecciona la carpeta raíz del proyecto (Solutions/MiProyecto/)",
        key="manual_path_input",
    )

with col_browse:
    st.markdown("<br>", unsafe_allow_html=True)  # Alinear verticalmente
    browse_clicked = st.button("Explorar...", use_container_width=True)

# Manejar el boton de explorar carpetas
if browse_clicked:
    folder = select_folder()
    if folder:
        st.session_state["project_path"] = folder
        st.session_state["project_name"] = os.path.basename(folder.rstrip("/\\"))
        save_last_project(folder)
        st.rerun()

# Manejar la entrada manual de ruta
if manual_path and manual_path != st.session_state.get("project_path", ""):
    clean_path = manual_path.strip().rstrip("/\\")
    if os.path.isdir(clean_path):
        st.session_state["project_path"] = clean_path
        st.session_state["project_name"] = os.path.basename(clean_path)
        save_last_project(clean_path)
        st.rerun()
    else:
        st.warning(f"La ruta no existe: `{clean_path}`")

# Display del proyecto activo
project_path = st.session_state.get("project_path", "")
project_name = st.session_state.get("project_name", "")

if project_path and os.path.isdir(project_path):
    output_path = get_cuig_output_path(project_path)
    existing_pages = list_existing_pages(output_path)

    # Verificar si existe el .cuib
    cuib_path = get_cuib_path(project_path)
    cuib_exists = os.path.isfile(cuib_path)

    st.markdown(
        f'<div style="padding:15px; border-radius:5px; background-color:rgba(63, 185, 80, 0.1); '
        f'border:1px solid rgba(63, 185, 80, 0.2); margin-bottom:15px;">'
        f'{icon("crosshair", 16, "#3FB950")} <strong>Proyecto activo:</strong> {project_name}<br><br>'
        f'<strong>Carpeta de salida:</strong> <code>{output_path}</code><br><br>'
        f'<strong>Archivo .cuib:</strong> {"Detectado" if cuib_exists else "No encontrado"}<br><br>'
        f'<strong>Páginas existentes ({len(existing_pages)}):</strong> '
        f'{", ".join(f"<code>{p}</code>" for p in existing_pages) if existing_pages else "Ninguna"}'
        f'</div>',
        unsafe_allow_html=True
    )
else:
    st.markdown(
        f'<div style="padding:15px; border-radius:5px; background-color:rgba(210, 153, 34, 0.1); '
        f'border:1px solid rgba(210, 153, 34, 0.2); margin-bottom:15px; color:#D29922;">'
        f'{icon("exclamation-triangle-fill", 16, "#D29922")} <strong>No hay proyecto seleccionado.</strong> '
        f'Usa el botón Explorar o ingresa la ruta manualmente para continuar.'
        f'</div>',
        unsafe_allow_html=True
    )

st.divider()

# ─── PLANTILLAS DE SALA (SELECTOR RAPIDO) ─────────────────────────────────────

st.markdown(
    f'### {icon("building", 20)} ¿Con qué tipo de sala estás trabajando?',
    unsafe_allow_html=True
)

cols = st.columns(3)
for i, (name, template) in enumerate(ROOM_TEMPLATES.items()):
    with cols[i % 3]:
        if st.button(
            name,
            use_container_width=True,
            help=template["description"],
            key=f"template_{i}",
        ):
            st.session_state["selected_template"] = name
            if template["prompt"]:
                st.session_state["prompt_input"] = template["prompt"]
            st.rerun()

# Indicador de plantilla activa
selected_tpl = st.session_state.get("selected_template", "Personalizado")
if selected_tpl != "Personalizado":
    st.markdown(
        f'{icon("file-earmark-text", 14)} Plantilla activa: **{selected_tpl}** — edita el prompt si lo necesitas',
        unsafe_allow_html=True
    )
# ─── GUIA CONTEXTUAL DE PROMPT ────────────────────────────────────────────────

with st.expander(f'{icon("lightbulb", 16)} ¿Cómo escribir un buen prompt? (haz clic para ver)'):
    st.markdown("""
### Un buen prompt AV incluye:

**1. Tipo de sala o contexto:**
> "Sala de conferencias corporativa", "Aula universitaria", "Sala VIP de hotel"

**2. Dispositivos a controlar (sé específico):**
> (Incorrecto) "botones para el proyector"
> (Correcto) "botón Encender proyector, botón Apagar proyector, botón Congelar imagen"

**3. Organización visual:**
> "sección superior para video, sección central para audio"
> "layout en 3 columnas: izquierda audio, centro video, derecha iluminación"

**4. Cantidad y tipo de controles:**
> "2 sliders de volumen (sala y micrófonos)"
> "4 botones de fuente de video"
> "3 niveles de iluminación preestablecidos"

### Ejemplo completo:
```
Sala de reuniones ejecutiva con:
- Fila superior: botón Encender proyector (grande, verde),
  botón Apagar (rojo), botón Mute Video
- Centro: slider de volumen del sistema (ancho completo),
  slider de volumen de micrófonos
- Fila inferior: 3 botones de fuente (HDMI 1 / HDMI 2 / Laptop),
  botón Apagado Total (destacado en rojo)
Layout limpio con fondo oscuro y texto blanco.
```
    """)

st.divider()

# ─── FORMULARIO DE ENTRADA ────────────────────────────────────────────────────

prompt = st.text_area(
    label="Describe la pantalla que necesitas:",
    placeholder=(
        "Ej: Crea una página para el proyector con botón de encendido, "
        "apagado y control de volumen"
    ),
    height=120,
    key="prompt_input",
)

# ─── ANALISIS DE CALIDAD DEL PROMPT ───────────────────────────────────────────

if prompt:
    analysis = analyze_prompt_quality(prompt)
    score = analysis["score"]

    col_label, col_bar = st.columns([1, 3])
    with col_label:
        st.caption("Calidad del prompt")
    with col_bar:
        st.progress(score / 100)

    # Mostrar número y estado textual debajo
    if score >= 70:
        st.markdown(
            f'{icon("check-circle-fill", 14, "#3FB950")} '
            f'**{score}/100** — Prompt listo para generar',
            unsafe_allow_html=True
        )
    elif score >= 40:
        st.markdown(
            f'{icon("exclamation-triangle-fill", 14, "#D29922")} '
            f'**{score}/100** — Puedes mejorar el prompt',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'{icon("x-circle-fill", 14, "#F85149")} '
            f'**{score}/100** — El prompt necesita más detalle',
            unsafe_allow_html=True
        )

    if analysis["suggestions"]:
        for s in analysis["suggestions"]:
            st.markdown(
                f'<span style="font-size: 12px; color: #888;">{icon("info-circle", 12)} {s}</span>',
                unsafe_allow_html=True
            )

col_btn, col_info = st.columns([1, 3])
with col_btn:
    generate_btn = st.button(
        "Generar interfaz",
        type="primary",
        use_container_width=True,
        disabled=not (project_path and os.path.isdir(project_path)),
    )
with col_info:
    if prompt:
        detected = _extract_component_types(prompt)
        st.caption(f"Componentes detectados: {', '.join(detected)}")


# ─── FLUJO DE GENERACION ─────────────────────────────────────────────────────

if generate_btn and prompt:
    # Validar que hay proyecto seleccionado
    if not project_path or not os.path.isdir(project_path):
        st.error("Selecciona un proyecto Crestron válido antes de generar.")
        st.stop()

    # Obtener la carpeta de salida (Solutions/MiProyecto/MiProyecto/)
    output_path = get_cuig_output_path(project_path)

    # Detectar tipos de componentes del prompt
    component_types = _extract_component_types(prompt)

    with st.status("Generando interfaz...", expanded=True) as status:

        # ─── Paso 1: Search_Tool ──────────────────────────────────────
        st.markdown(
            f'{icon("search", 14)} Buscando esquemas en LanceDB...',
            unsafe_allow_html=True
        )
        t0 = time.time()

        try:
            # Llamada al servidor MCP vía stdio
            schemas = asyncio.run(call_mcp_tool("search_component_schema", {"component_types": component_types}))
            t_search = time.time() - t0
            st.markdown(
                f'{icon("check-circle-fill", 14, "#3FB950")} Esquemas recuperados ({t_search:.1f}s)',
                unsafe_allow_html=True
            )
        except Exception as e:
            st.error(f"Error en Search_Tool: {e}")
            status.update(label="Error en búsqueda", state="error")
            st.stop()

        # ─── Paso 2: Router IA (Gemini) ──────────────────────────────
        st.markdown(
            f'{icon("cpu", 14)} Consultando Gemini Pro ({GEMINI_MODEL}) (canvas {canvas_w}×{canvas_h})...',
            unsafe_allow_html=True
        )
        t0 = time.time()

        # Construir los prompts para Gemini Pro
        try:
            system_prompt_template = load_system_prompt()
            panel_constraints_text = format_panel_constraints(canvas_w, canvas_h)
            system_prompt = system_prompt_template.format(
                canvas_width=canvas_w,
                canvas_height=canvas_h,
                panel_constraints=panel_constraints_text,
                background_color="AUTO",
                primary_color="AUTO",
                text_color="AUTO",
                border_color="AUTO",
                panel_background_color="AUTO",
            )
            user_prompt = build_user_prompt(prompt, component_schemas=schemas)
        except Exception as e:
            st.error(f"Error al construir los prompts: {e}")
            status.update(label="Error de configuración", state="error")
            st.stop()

        try:
            layout_json = get_layout_from_ai(system_prompt, user_prompt)
            t_ai = time.time() - t0
            st.markdown(
                f'{icon("check-circle-fill", 14, "#3FB950")} Layout JSON recibido ({t_ai:.1f}s)',
                unsafe_allow_html=True
            )
        except RuntimeError as e:
            st.error(f"Error al generar el layout: {e}")
            status.update(label="Error de IA", state="error")
            st.stop()
        except Exception as e:
            st.error(f"Error inesperado en Router IA: {e}")
            status.update(label="Error IA", state="error")
            st.stop()

        # ─── Paso 3: Builder_Tool ────────────────────────────────────
        st.markdown(
            f'{icon("gear-fill", 14)} Ensamblando archivo .cuig en <code>{output_path}</code>...',
            unsafe_allow_html=True
        )
        t0 = time.time()

        try:
            bg_color_to_use = layout_json.get("theme_background_color", "#0D1117")

            # Llamada al servidor MCP vía stdio
            cuig_path = asyncio.run(call_mcp_tool("build_cuig_file", {
                "layout_json": layout_json,
                "output_dir": output_path,
                "background_color": bg_color_to_use
            }))
            t_build = time.time() - t0
            st.markdown(
                f'{icon("check-circle-fill", 14, "#3FB950")} Archivo ensamblado ({t_build:.1f}s)',
                unsafe_allow_html=True
            )
        except Exception as e:
            st.error(f"Error en Builder_Tool: {e}")
            status.update(label="Error de ensamblaje", state="error")
            st.stop()

        # ─── Éxito ────────────────────────────────────────────────────
        t_total = t_search + t_ai + t_build
        status.update(
            label=f"Interfaz generada en {t_total:.1f}s",
            state="complete",
        )

    # ─── RESULTADOS ───────────────────────────────────────────────────────

    st.divider()

    # Archivo generado
    st.markdown(
        f'<div style="padding: 10px; border-radius: 5px; background-color: rgba(63, 185, 80, 0.1); '
        f'border: 1px solid rgba(63, 185, 80, 0.2); margin-bottom: 10px;">'
        f'{icon("check-circle-fill", 14, "#3FB950")} Archivo generado: <strong>{Path(cuig_path).name}</strong>'
        f'</div>',
        unsafe_allow_html=True
    )
    st.code(cuig_path, language="text")

    # Métricas
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Búsqueda", f"{t_search:.1f}s")
    col2.metric("Gemini Pro", f"{t_ai:.1f}s")
    col3.metric("Ensamblaje", f"{t_build:.1f}s")
    col4.metric("Panel", f"{canvas_w}×{canvas_h}")

    # JSON de Gemini (expandible)
    with st.expander(f'{icon("braces", 16)} JSON generado por Gemini Pro', expanded=False):
        st.json(layout_json)

    # Resumen de elementos
    with st.expander(f'{icon("grid-3x3-gap", 16)} Elementos generados', expanded=True):
        page_name_result = layout_json.get("page_name", "—")
        elements = layout_json.get("elements", [])
        st.markdown(f"**Página:** {page_name_result}")
        st.markdown(f"**Canvas:** {layout_json.get('canvas_width', '?')} × {layout_json.get('canvas_height', '?')} px")
        st.markdown(f"**Elementos:** {len(elements)}")

        for i, el in enumerate(elements, 1):
            el_type = el.get("type", "?")
            el_label = el.get("label", "—")
            el_pos = f"({el.get('x', 0)}, {el.get('y', 0)})"
            el_size = f"{el.get('w', 0)}×{el.get('h', 0)}"
            st.markdown(
                f"  {i}. `{el_type}` — **{el_label}** "
                f"· pos {el_pos} · size {el_size}"
            )

elif generate_btn and not prompt:
    st.warning("Escribe una descripción antes de generar.")
