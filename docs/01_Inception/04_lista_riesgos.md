# Lista de Riesgos — AV-MCP Automator
**RUP Fase:** Inicio — IT-1 (Semana 2) | **Va al informe:** ✅ Sí

| ID | Riesgo | Prob. | Impacto | Mitigación |
|---|---|---|---|---|
| R-01 | No conseguir archivos .cuig de referencia para ingeniería inversa | Media | Alto | Buscar proyectos de ejemplo en foros oficiales de Crestron y documentación pública |
| R-02 | Gemini alucina atributos ccid_* propietarios de Crestron | Alta | Alto | La IA solo genera JSON simple; Python ensambla el .cuig con plantillas deterministas |
| R-03 | Agotamiento de la cuota de 1,000 llamadas/día de Gemini Flash-Lite | Media | Medio | Ninguna |
| R-04 | Incompatibilidad de .cuig generados con la versión de Construct instalada | Media | Alto | Ingeniería inversa en Semanas 1–2 para detectar la versión exacta del formato |
| R-05 | RAM insuficiente al ejecutar Ollama + LanceDB + Streamlit en paralelo | Baja | Medio | Ollama solo carga el modelo cuando Gemini falla; LanceDB embebida < 1 GB |
