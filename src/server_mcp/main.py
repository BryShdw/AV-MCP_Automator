"""
Capa 2 — Servidor MCP & Compilador
Punto de entrada del servidor FastMCP.

RUP Fase: Construccion — Iteracion 3 (Semana 5, prototipo ejecutable)

Arquitectura simplificada (descubierta en el analisis forense):
  - Search_Tool: recupera esquemas CH5 desde LanceDB
  - Builder_Tool: genera el .cuig completo Y lo escribe en disco
  - Cuig_Tool: ELIMINADO — el .cuib no necesita modificarse,
    Crestron Construct detecta los .cuig automaticamente por presencia en la carpeta.
"""
from fastmcp import FastMCP
from tools.search_tool import search_component_schema
from tools.builder_tool import build_cuig_file

mcp = FastMCP(
    name="AV-MCP Automator",
    description="Servidor MCP para generacion de interfaces Crestron CH5 nativas (.cuig)",
)

# ─── REGISTRO DE HERRAMIENTAS (2 tools, no 3) ────────────────────────────────
mcp.tool(search_component_schema)
mcp.tool(build_cuig_file)

if __name__ == "__main__":
    # Transporte: stdio (comunicacion local con Streamlit)
    mcp.run(transport="stdio")
