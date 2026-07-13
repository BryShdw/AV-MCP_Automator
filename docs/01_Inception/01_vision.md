# Documento de Visión — AV-MCP Automator
**Fase RUP:** Inicio

## 1. Problema
El desarrollo de interfaces gráficas en Crestron Construct consume una parte desproporcionada del tiempo del departamento de ingeniería de DACER S.A.C. Los especialistas AV deben maquetar manualmente cada pantalla táctil, arrastrando componentes, configurando colores y parámetros estándar de manera iterativa. Este proceso repetitivo impacta negativamente en los tiempos del proyecto general, creando cuellos de botella en la fase de programación e instalación de múltiples proyectos simultáneos.

## 2. Propuesta de Solución
La propuesta es desarrollar el **AV-MCP Automator**, un middleware que utiliza inteligencia artificial generativa (Gemini) para transformar descripciones de salas en lenguaje natural directamente en archivos nativos de diseño. A través del estándar Model Context Protocol (MCP), el sistema procesa los requerimientos espaciales del ingeniero, recupera plantillas de componentes (botones, sliders, texto) desde una base vectorial (LanceDB) y ensambla archivos `.cuig` compatibles con el IDE Crestron Construct. El ingeniero simplemente abre la página generada y continúa su flujo de trabajo visual normal.

## 3. Stakeholders
| Stakeholder | Rol | Interés |
|---|---|---|
| DACER S.A.C. (Empresa) | Patrocinador / Beneficiario final | Optimizar tiempos de ingeniería para poder atender más proyectos en paralelo; mantener costos operativos controlados. |
| Ingenieros AV (Pro AV) | Usuarios directos | Reducir la carga de trabajo repetitiva en la creación de interfaces; mantener control total sobre el resultado final en su herramienta nativa. |
| Tutora Universitaria | Evaluadora académica | Garantizar que el proyecto cumpla con los estándares metodológicos (RUP) y técnicos requeridos para la titulación del practicante. |
| Brayan Delgado Oblitas | Practicante / Desarrollador único | Aplicar conocimientos en IA y desarrollo de software para resolver un problema empresarial real, cumpliendo con los objetivos académicos. |

## 4. Objetivo Principal y Métricas de Éxito
| Objetivo | Métrica | Valor Objetivo |
|---|---|---|
| Eliminar el trabajo repetitivo de maquetación visual | Reducción de tiempo de maquetación inicial | 40–60% de ahorro (generación en < 10 seg vs ~45 min manual) |
| Generar archivos compatibles con el IDE oficial | Tasa de apertura sin errores en Crestron Construct | 100% de compatibilidad |
| Mantener costo cero de licencias | Presupuesto del proyecto | S/. 0 (Capa gratuita y open source) |

## 5. Alcance
| In-Scope (Dentro del alcance) | Out-of-Scope (Fuera del alcance) |
|---|---|
| Generación de archivos nativos `.cuig` mediante ensamblaje programático. | Programación de la lógica de procesadores (SIMPL Windows, C#). |
| Posicionamiento espacial calculado en CSS y asignación de atributos `ccid_*`. | Asignación automática de Joins de control a hardware físico. |
| Actualización del proyecto maestro (`.cuib`). | Despliegue en los paneles táctiles físicos. |
| Interfaz web en Streamlit para lenguaje natural y temas Pro AV. | Interfaz para Extron o herramientas fuera del ecosistema Crestron. |

## 6. Restricciones No Negociables
| Restricción | Tipo | Impacto |
|---|---|---|
| Hardware del practicante | Técnica | Máximo 16GB RAM compartida. Obliga al uso de modelos IA ligeros o APIs en la nube. |
| Costo cero en licencias | Presupuestaria | Stack 100% open source y capas gratuitas (ej. Gemini Free Tier). |
| Uso exclusivo en Frontend (CH5) | Académica | Todo el backend de procesadores físicos queda excluido del análisis. |
| Límite de API (1,000 req/día) | Técnica | Arquitectura debe minimizar tamaño del payload (Patrón Compilador MCP). |
