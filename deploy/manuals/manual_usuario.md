# Manual de Usuario — AV-MCP Automator
**RUP Fase:** Transición | **Artefacto:** Manual de Usuario | **Va al informe:** ✅ Sí
**Destinatario:** Especialista AV de DACER S.A.C.

---
> ⚠️ Este documento se redacta en la **Semana 13** (Fase de Transición).
> La estructura a continuación es el esquema que se completará.

## 1. Requisitos previos
- Python 3.11+ instalado
- Crestron Construct™ instalado y con un proyecto creado
- Conexión a internet (para Gemini 2.5 Flash-Lite)

## 2. Instalación

```bash
# Clonar el repositorio
git clone <url-del-repo>
cd AV-MCP_Automator

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tu clave de API de Gemini (GEMINI_API_KEY)
```

## 3. Inicio del sistema

```bash
# Terminal 1: Servidor MCP
python src/server_mcp/main.py

# Terminal 2: Interfaz de usuario
streamlit run src/client/app.py
```

## 4. Uso paso a paso

### Paso 1 — Seleccionar el proyecto Crestron
Al abrir la UI por primera vez, selecciona tu proyecto:
1. Haz clic en **📂 Explorar...** para abrir el selector de carpetas
2. Navega hasta `Documents/Crestron/Crestron Construct/Solutions/MiProyecto/`
3. El sistema detecta automáticamente el nombre del proyecto
4. Verás un panel con la información del proyecto activo y las páginas existentes

> La ruta se guarda automáticamente. La próxima vez que abras la app, tu proyecto estará preseleccionado.

### Paso 2 — Seleccionar el tipo de panel
<!-- Completar en Semana 13 -->

### Paso 3 — Describir la pantalla
<!-- Completar en Semana 13 con capturas de pantalla reales -->

### Paso 4 — Generar la interfaz
<!-- Completar en Semana 13 -->

### Paso 5 — Abrir en Crestron Construct
El archivo `.cuig` generado se guarda automáticamente en la subcarpeta interna
del proyecto (`Solutions/MiProyecto/MiProyecto/`). Crestron Construct detecta
las nuevas páginas automáticamente al abrir la solución.
<!-- Completar en Semana 13 con capturas del resultado WYSIWYG -->

## 5. Solución de problemas frecuentes

| Problema | Causa probable | Solución |
|---|---|---|
| "API Key inválida" | Clave de Gemini incorrecta en .env | Verificar GEMINI_API_KEY en .env |
| "Cuota agotada" | Se superaron las 1,000 llamadas diarias | Esperar al día siguiente o usar otra clave |
| "El .cuig no abre en Construct" | Carpeta de proyecto incorrecta | Verificar que el proyecto seleccionado en la UI coincide con la solución en Construct |
| Botón "Generar" deshabilitado | No hay proyecto seleccionado | Usar 📂 Explorar o escribir la ruta manualmente |
