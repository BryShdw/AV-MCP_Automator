"""
Capa 1 — UI Cliente
Interfaz Streamlit para el especialista AV de DACER S.A.C.

RUP Fase: Construcción — Iteración 4 (Semana 10)
"""
import streamlit as st

st.set_page_config(
    page_title="AV-MCP Automator",
    page_icon="🎛️",
    layout="wide",
)

st.title("🎛️ AV-MCP Automator")
st.caption("Generador de interfaces Crestron CH5 — DACER S.A.C.")

# ─── PANEL DE ENTRADA ─────────────────────────────────────────────────────────
with st.form("layout_form"):
    prompt = st.text_area(
        label="Describe la pantalla que necesitas:",
        placeholder="Ej: Crea una página para el proyector con botón de encendido, apagado y control de volumen",
        height=120,
    )
    panel_type = st.selectbox(
        "Tipo de panel destino:",
        options=["TSW-1070 (10\")", "TSW-770 (7\")", "Web Xpanel", "iPad"],
    )
    submitted = st.form_submit_button("⚙️ Generar interfaz")

# ─── LOG DE PROCESO ───────────────────────────────────────────────────────────
if submitted and prompt:
    with st.spinner("Procesando..."):
        # TODO (Semana 10): Conectar con servidor MCP via stdio (JSON-RPC 2.0)
        st.info("🔧 Conexión con servidor MCP — Por implementar en Semana 10")

        # Placeholder de output
        st.success("✅ Archivo generado: `NombrePagina.cuig`")
        st.code("ruta: C:/Users/.../Crestron/Projects/DACER_Project/NombrePagina.cuig")
