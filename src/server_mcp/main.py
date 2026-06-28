"""
Capa 2 — Servidor MCP & Compilador
Punto de entrada del servidor FastMCP.

RUP Fase: Construcción — Iteración 3 (Semana 5, prototipo ejecutable)
"""
from fastmcp import FastMCP
from tools.search_tool import search_component_schema
from tools.builder_tool import build_cuig_file
from tools.cuig_tool import update_cuib_project

mcp = FastMCP(
    name="AV-MCP Automator",
    description="Servidor MCP para generación de interfaces Crestron CH5 nativas (.cuig/.cuib)",
)

# ─── REGISTRO DE HERRAMIENTAS ─────────────────────────────────────────────────
mcp.tool(search_component_schema)
mcp.tool(build_cuig_file)
mcp.tool(update_cuib_project)

if __name__ == "__main__":
    # Transporte: stdio (comunicación local con Streamlit)
    mcp.run(transport="stdio")
