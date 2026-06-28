# Manual de Usuario — AV-MCP Automator
**RUP Fase:** Transición | **Artefacto:** Manual de Usuario | **Va al informe:** ✅ Sí
**Destinatario:** Especialista AV de DACER S.A.C.

---
> ⚠️ Este documento se redacta en la **Semana 13** (Fase de Transición).
> La estructura a continuación es el esquema que se completará.

## 1. Requisitos previos
- Python 3.11+ instalado
- Crestron Construct™ instalado y con un proyecto abierto
- Conexión a internet (para Gemini) o Ollama instalado (para modo offline)

## 2. Instalación

```bash
# Clonar el repositorio
git clone <url-del-repo>
cd AV-MCP_Automator

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tu clave de API de Gemini y la ruta del proyecto Crestron
```

## 3. Inicio del sistema

```bash
# Terminal 1: Servidor MCP
python src/server_mcp/main.py

# Terminal 2: Interfaz de usuario
streamlit run src/client/app.py
```

## 4. Uso paso a paso

### Paso 1 — Describir la pantalla
<!-- Completar en Semana 13 con capturas de pantalla reales -->

### Paso 2 — Seleccionar el tipo de panel
<!-- Completar en Semana 13 -->

### Paso 3 — Generar la interfaz
<!-- Completar en Semana 13 -->

### Paso 4 — Abrir en Crestron Construct
<!-- Completar en Semana 13 con capturas del resultado WYSIWYG -->

## 5. Solución de problemas frecuentes

| Problema | Causa probable | Solución |
|---|---|---|
| "API Key inválida" | Clave de Gemini incorrecta en .env | Verificar GEMINI_API_KEY en .env |
| "Cuota agotada" | Se superaron las 1,000 llamadas diarias | El sistema usa Ollama automáticamente |
| "El .cuig no abre en Construct" | Ruta incorrecta en .env | Verificar CRESTRON_PROJECT_PATH |
| Ollama no responde | El modelo no está descargado | Ejecutar: `ollama pull llama3.2:3b-instruct-q4_K_M` |
