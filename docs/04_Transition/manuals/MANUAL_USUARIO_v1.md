# Manual de Usuario — AV-MCP Automator
**Versión:** 1.0
**Fecha:** Junio 2026

## 1. Introducción
El AV-MCP Automator es un sistema diseñado para los ingenieros AV de DACER S.A.C. Su objetivo es generar automáticamente archivos de diseño visual (`.cuig`) para pantallas táctiles Crestron CH5 a partir de descripciones en lenguaje natural. En lugar de arrastrar y soltar componentes manualmente, el ingeniero simplemente describe qué controles necesita en la pantalla, y el sistema construye el archivo base listo para ser editado visualmente en Crestron Construct.

## 2. Requisitos Previos
Para usar el sistema en su equipo de trabajo, necesita tener instalado:
- **Python 3.11** o superior.
- **Crestron Construct** (versión actual soportada por la empresa).
- **API Key de Gemini** activa (generada gratuitamente en Google AI Studio).

## 3. Instalación
La instalación inicial requiere configurar el entorno:
1. Abra su terminal o consola de comandos en la carpeta del sistema.
2. Cree un entorno virtual y actívelo.
3. Instale las dependencias necesarias.
4. (Consulte la "Guía de Despliegue" para el detalle técnico de estos pasos).

## 4. Guía de Uso Rápido
Para generar una interfaz siga estos 4 pasos esenciales:

1. **Seleccionar el Proyecto:** Al abrir la aplicación, use el botón superior para buscar y seleccionar la carpeta donde guarda sus proyectos de Crestron Construct. El sistema recordará esta carpeta para el futuro.
2. **Elegir Panel Destino y Tema:** Seleccione el modelo físico de la pantalla táctil (por ejemplo, TSW-770) y escoja la paleta de colores visuales (ejemplo, "Corporate Blue").
3. **Describir la Interfaz:** En el cuadro de texto principal, escriba qué controles necesita. Ejemplo: *"Necesito una página para el control de audio. Incluye un deslizador para el volumen maestro y un botón rojo grande para silenciar todo."*
4. **Generar y Abrir:** Presione el botón "Generar Interfaz". En menos de 10 segundos, el sistema procesará su solicitud, creará el archivo `.cuig` y mostrará un mensaje de éxito. Luego, abra Crestron Construct y verá la nueva página lista para configurar sus Joins.

## 5. Plantillas de Sala Disponibles
El sistema entiende contextos. Usted puede solicitar:

| Plantilla | Descripción | Cuándo usar |
|---|---|---|
| **Sala de Conferencias** | Distribución típica con controles de proyector, ecualización y selectores de fuente de video. | Reuniones corporativas estándar. |
| **Aula Educativa** | Controles simplificados, botones grandes, énfasis en control de volumen y encendido/apagado general. | Universidades o colegios. |
| **Auditorio** | Múltiples zonas de audio, controles complejos de iluminación y escenarios. | Espacios grandes o teatros. |

## 6. Selección de Panel de Destino
| Panel Disponible | Resolución (Ancho x Alto) | Uso Típico |
|---|---|---|
| TST-1080 (Landscape) | 1920 x 1200 | Panel inalámbrico premium corporativo. |
| TSW-1070 (Landscape) | 1920 x 1200 | Panel de pared de 10" para salas grandes. |
| TSW-770 (Landscape) | 1280 x 800 | Panel de pared estándar de 7" para huddle rooms. |
| Personalizado | Especificado por el usuario | Cuando use un modelo no listado o Web Xpanel. |

## 7. Temas Visuales Pro AV
Seleccione uno antes de generar:
- **Dark Pro:** Fondo oscuro profundo con acentos sutiles, ideal para salas de cine o auditorios oscuros.
- **Corporate Blue:** Tonos azules y blancos, transmite limpieza y profesionalismo corporativo.
- **Slate Dark:** Tonos grises y metálicos para entornos industriales o técnicos.
- **Academic Light:** Colores claros de alto contraste, pensado para aulas muy iluminadas donde la lectura fácil es primordial.

## 8. Solución de Problemas
| Síntoma | Causa Probable | Solución |
|---|---|---|
| Error "API Key Inválida" | La llave de Google expiró o no está en el `.env`. | Genere una nueva en Google AI Studio y póngala en su archivo `.env`. |
| La página no aparece en Construct | El proyecto `.cuib` estaba abierto y Construct no recargó. | Cierre y vuelva a abrir Crestron Construct. |
| Elementos superpuestos | El prompt pidió demasiados elementos para una pantalla pequeña. | Reduzca la cantidad de componentes o pida que se distribuyan en dos páginas. |

## 9. Buenas Prácticas para Prompts
- **Sea específico con la disposición:** *"Coloca el control de volumen a la derecha y los botones de fuente a la izquierda."*
- **Limite la cantidad:** Pida un máximo de 10 a 12 elementos por página para evitar saturación visual.
- **Mencione el tipo de elemento:** Diga "un botón de apagado", "un deslizador de volumen", o "un texto de cabecera" para ayudar al sistema a escoger el componente CH5 correcto.

## 10. Contacto de Soporte
Ante cualquier eventualidad crítica en producción, consulte el repositorio interno de ingeniería o contacte a los desarrolladores de la plataforma.
