# Guía de Despliegue — AV-MCP Automator
**Versión:** 1.0
**Fecha:** Junio 2026

## 1. Requisitos del Sistema
Para instalar y ejecutar el AV-MCP Automator en producción, el equipo host debe cumplir con:
- **Sistema Operativo:** Windows 10/11 (recomendado para integradores Crestron) o macOS.
- **Python:** Versión 3.11 o superior.
- **Memoria RAM:** Mínimo 8 GB (Recomendado 16 GB).
- **Almacenamiento:** Al menos 1 GB de espacio libre (para la base LanceDB y entornos virtuales).

## 2. Obtener el Código Fuente
Asegúrese de clonar o extraer el código fuente del proyecto en una carpeta local de fácil acceso.
No ubique la carpeta en directorios temporales o en el Escritorio para evitar problemas de permisos.

## 3. Instalación de Dependencias
Abra su terminal o PowerShell en la carpeta raíz del proyecto y ejecute:
1. Crear entorno virtual: `python -m venv venv`
2. Activar entorno (Windows): `.\venv\Scripts\activate`
3. Activar entorno (Mac/Linux): `source venv/bin/activate`
4. Instalar librerías: `pip install -r requirements.txt`

## 4. Configuración del Archivo `.env`
Renombre o copie el archivo `.env.example` a `.env` en la raíz del proyecto y complete las variables:

| Variable | Descripción | Ejemplo |
|---|---|---|
| `GEMINI_API_KEY` | Clave API gratuita para usar el modelo LLM. Obligatorio. | `AIzaSy...` |
| `GEMINI_MODEL` | El modelo a usar (se recomienda Flash-Lite por velocidad). | `gemini-2.5-flash` |
| `LANCEDB_PATH` | Ruta local donde se almacenarán los vectores de LanceDB. | `./data/lancedb` |
| `LANCEDB_TABLE_NAME` | Nombre de la tabla vectorial a crear/consultar. | `ch5_components` |
| `MCP_TRANSPORT` | Protocolo de comunicación interna del servidor FastMCP. | `stdio` |

## 5. Inicialización de la Base de Datos Vectorial
El sistema incluye la base vectorial LanceDB poblada. Si se requiere reinstalar desde cero, ejecute el script de indexación local que procesa la documentación de Crestron y genera los embeddings. 

## 6. Verificación de la Instalación
Para verificar que todo esté en orden, ejecute la suite de pruebas unitarias (si está disponible en su rama):
Ejecute: `pytest tests/ -v`
Resultado esperado: Todas las pruebas deben reportar "PASSED".

## 7. Inicio del Sistema
Para arrancar la interfaz gráfica para el usuario final, ejecute:
`streamlit run app.py` (o el script principal de entrada del proyecto UI).
Se abrirá automáticamente el navegador web predeterminado apuntando a `http://localhost:8501`.

## 8. Actualización del Sistema a Versiones Futuras
Si existen actualizaciones del código fuente (por ejemplo, nuevas plantillas CH5):
1. Detenga el servidor de Streamlit (Ctrl+C).
2. Reemplace los archivos fuente.
3. Con el entorno activado, ejecute nuevamente `pip install -r requirements.txt` por si hay dependencias nuevas.
4. Reinicie el servidor con `streamlit run app.py`.
