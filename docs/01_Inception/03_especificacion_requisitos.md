# Especificación de Requisitos — AV-MCP Automator
**RUP Fase:** Inicio — IT-1 (Semana 2) | **Va al informe:** ✅ Sí

## Requisitos Funcionales

| ID | Requisito | Prioridad |
|---|---|---|
| RF-01 | Generar archivos .cuig válidos a partir de un prompt en lenguaje natural | Alta |
| RF-02 | Actualizar el archivo .cuib del proyecto con cada nueva página generada | Alta |
| RF-03 | Recuperar el esquema JSON del componente CH5 solicitado desde LanceDB | Alta |
| RF-04 | Conmutar automáticamente a Ollama si la API de Gemini falla o agota cuota | Media |
| RF-05 | Validar que el HTML del .cuig no contiene etiquetas CH5 malformadas | Media |
| RF-06 | Restringir componentes según el tipo de panel destino (x60, iOS, etc.) | Baja |

## Requisitos No Funcionales

| ID | Requisito | Valor objetivo |
|---|---|---|
| RNF-01 | Tiempo de respuesta (prompt → archivo generado) | < 10 segundos |
| RNF-02 | Presupuesto de licencias del stack | S/. 0 |
| RNF-03 | Consumo de RAM en modo operación (Gemini como principal) | < 4 GB |
| RNF-04 | Tasa de apertura sin errores de .cuig en Crestron Construct | 100% |
