# Guía de Diapositivas — Exposición del Proyecto AV-MCP Automator
### Middleware basado en Model Context Protocol para la optimización del diseño de interfaces audiovisuales — DACER S.A.C.

**Enfoque de la exposición (20 min):** Empresa (general) → Problema → Objetivos → Ejecución del sistema/proyecto.
**Uso de esta guía:** cada bloque describe qué contenido debe llevar la diapositiva (texto, datos, tablas, figuras). No incluye el discurso del expositor.

---

## BLOQUE 0 — Portada (1 diapositiva | ~0:30 min)

**Diapositiva 1: Portada**
- Título del proyecto: "Implementación de un middleware basado en Model Context Protocol para la optimización del diseño de interfaces audiovisuales en una empresa privada del distrito de Miraflores 2026"
- Nombre corto del sistema: **AV-MCP Automator**
- Empresa: DACER S.A.C.
- Nombre del practicante
- Curso: Práctica Preprofesional I — Ingeniería de Sistemas
- Fecha/periodo

---

## BLOQUE 1 — La Empresa (2 diapositivas | ~3:00 min)

**Diapositiva 2: DACER S.A.C. — Perfil de la empresa**
- Rubro: integración Pro AV / TI (audiovisual + tecnologías de información)
- Más de 25 años de trayectoria en el mercado peruano
- Servicios: consultoría, diseño de ingeniería, suministro, instalación, soporte post-venta
- Certificaciones del personal: AVIXA, Extron
- Alianzas con fabricantes: Samsung, Cisco, Polycom
- Ubicación: Miraflores, Lima
- Área donde se realizaron las prácticas: **Departamento de Ingeniería → subárea de Programación**

**Diapositiva 3: FODA de la empresa (contexto para el proyecto)**
- Tabla FODA (usar Figura 2 del informe):

  | FODA | Descripción |
  |---|---|
  | Fortaleza | +25 años de experiencia, personal certificado, alianzas con marcas líderes |
  | Oportunidad | IA generativa para reducir tiempos de programación; demanda de trabajo híbrido |
  | Debilidad | Procesos de programación manual que generan pérdida de tiempo |
  | Amenaza | Competencia tecnológica agresiva; dependencia de APIs externas de IA |

- Resaltar visualmente la fila **"Debilidad"** (es el gancho hacia la siguiente sección: el problema)

---

## BLOQUE 2 — El Problema (3 diapositivas | ~5:00 min)

**Diapositiva 4: Contexto tecnológico del problema**
- Transición de la industria: interfaces propietarias y cerradas → tecnologías web estándar (HTML5, CSS, JavaScript)
- Framework adoptado por Crestron: **CH5 (Crestron HTML5 User Interface)**
- Consecuencia en DACER: los ingenieros deben maquetar manualmente o dominar desarrollo web avanzado para usar CH5

**Diapositiva 5: Realidad problemática — Diagrama causa-efecto**
- Insertar **Figura 6** del informe (diagrama de causa y efecto)
- Puntos clave en viñetas de apoyo (texto en pantalla):
  - Alta carga cognitiva en la codificación manual
  - Ausencia de herramientas automatizadas para código de dominio específico
  - Falta de un canal estandarizado entre el entorno de desarrollo y modelos de IA

**Diapositiva 6: Definición del problema y alcance**
- **Problema central** (recuadro destacado):
  > Baja productividad y altos tiempos de desarrollo en la codificación, maquetación y estructuración manual de interfaces web para sistemas Crestron CH5, por falta de herramientas de asistencia automatizada y contextual.
- Alcance del proyecto — **sí incluye**:
  - Integración de un LLM (Gemini) vía protocolo MCP
  - Base de datos vectorial local con documentación técnica CH5
  - Generación automatizada de código Frontend (HTML5, CSS, JS, directivas CH5)
- Límites del proyecto — **no incluye**:
  - Programación de procesadores de control (SIMPL Windows, C#)
  - Diseño gráfico desde cero (logos, ilustraciones)

---

## BLOQUE 3 — Objetivos (1 diapositiva | ~1:30 min)

**Diapositiva 7: Objetivo general y específicos**
- **Objetivo general** (recuadro destacado):
  > Desarrollar e implementar el AV-MCP Automator mediante LLM y el estándar MCP, para optimizar la eficiencia operativa y reducir los tiempos de codificación de interfaces CH5 en DACER S.A.C.
- **Objetivos específicos** (lista numerada, 5 puntos, texto corto cada uno):
  1. Determinar requerimientos funcionales y no funcionales
  2. Diseñar la arquitectura del sistema y los flujos de interacción
  3. Implementar la base de datos vectorial (LanceDB)
  4. Desarrollar el servidor de contexto (FastMCP) y la interfaz gráfica (Streamlit)
  5. Validar el rendimiento y la usabilidad mediante pruebas funcionales

---

## BLOQUE 4 — Ejecución del Sistema / Proyecto (11 diapositivas | ~9:30 min)

**Diapositiva 8: Metodología de trabajo**
- Metodología: **RUP (Proceso Unificado Racional)** adaptado a un desarrollador único
- Insertar **Tabla 1** (Fases RUP del proyecto):

  | Fase | Semanas | Meta principal |
  |---|---|---|
  | Inicio | S1–S2 | Definir problema, casos de uso y riesgos |
  | Elaboración | S3–S5 | Arquitectura "Compilador MCP", esquema JSON y base LanceDB |
  | Construcción | S6–S12 | Builder_Tool, Router IA, UI Streamlit, pruebas |
  | Transición | S13–S14 | Documentación operativa y entrega |

- Dato resumen: 4 fases, 5 iteraciones, 14 semanas

**Diapositiva 9: Requerimientos del sistema**
- Tabla de **Requerimientos Funcionales** (resumir los 3-4 más relevantes de la Tabla 3):

  | ID | Requisito | Prioridad |
  |---|---|---|
  | RF-01 | Generar archivos .cuig válidos desde prompt en lenguaje natural | Alta |
  | RF-02 | Recuperar esquema JSON del componente CH5 desde LanceDB | Alta |
  | RF-03 | Validar JSON generado por IA con esquema Pydantic | Alta |
  | RF-04 | Reintentar generación ante JSON mal formado | Media |

- Tabla de **Requerimientos No Funcionales** (Tabla 4, completa):

  | ID | Requisito | Valor objetivo |
  |---|---|---|
  | RNF-01 | Tiempo de respuesta (prompt → archivo generado) | < 10 segundos |
  | RNF-02 | Presupuesto de licencias del stack | S/. 0 |
  | RNF-03 | Consumo de RAM en operación | < 4 GB |
  | RNF-04 | Apertura sin errores en Crestron Construct | 100% |

**Diapositiva 10: Casos de uso**
- Insertar **Figura 7** (Diagrama de casos de uso del sistema)
- Actor principal: Ingeniero AV
- Caso de uso central: generación de interfaz desde descripción en lenguaje natural

**Diapositiva 11: Proceso de negocio — AS-IS vs. TO-BE**
- Insertar **Figura 9** (Diagrama AS-IS vs. TO-BE), organizada en dos paneles:
  - **AS-IS (antes):** maquetado manual arrastrando elementos en el IDE — alto consumo de tiempo
  - **TO-BE (ahora):** el ingeniero describe la interfaz en lenguaje natural → el sistema genera los archivos .cuig → el ingeniero ajusta visualmente los detalles

**Diapositiva 12: Arquitectura del sistema — Contexto y componentes**
- Insertar **Figura 10** (Diagrama de contexto del sistema)
- Insertar **Figura 11** (Diagrama de componentes del sistema)
- Listar las 5 capas del sistema (leyenda de apoyo visual):
  1. Streamlit — UI Cliente
  2. Servidor FastMCP — Capa de Protocolo (MCP)
  3. Router IA — Gemini 2.5 Flash-Lite
  4. LanceDB — Datos Vectoriales
  5. Archivo .cuig — Salida final en disco

**Diapositiva 13: Flujo del sistema y patrón "Compilador MCP"**
- Insertar **Figura 12** (Diagrama de flujo del sistema — Caso de uso CU-01)
- Recuadro destacado con el concepto clave del diseño:
  > Patrón "Compilador MCP": Gemini genera únicamente un JSON simple (componentes y coordenadas); el módulo `builder_tool.py` ensambla el archivo `.cuig` real con plantillas deterministas en Python.
- Beneficio destacado: elimina el riesgo de alucinaciones de sintaxis Crestron

**Diapositiva 14: Arquitectura de datos**
- Insertar **Figura 13** (Esquema de la tabla vectorial `ch5_components` en LanceDB)
- Datos clave en viñetas:
  - Base de datos vectorial embebida (sin servidor externo)
  - 138 documentos de la documentación oficial Crestron CH5
  - Embeddings de 384 dimensiones (modelo `all-MiniLM-L6-v2`)
  - Búsqueda semántica con latencia menor a 100 ms
- Insertar **Figura 14** (Esquema JSON del compilador MCP) — indicar validación con Pydantic v2 (`LayoutSchema`)

**Diapositiva 15: Infraestructura tecnológica**
- Insertar **Figura 15** (Diagrama de infraestructura tecnológica)
- Datos clave:
  - Procesamiento local: Lenovo IdeaPad, Windows 11, 16 GB RAM
  - Conexión a internet vía HTTPS únicamente para inferencia del LLM en la nube
  - Garantiza privacidad de datos locales de DACER
  - Sin costos de licenciamiento recurrente

**Diapositiva 16: Prototipo — Interfaz Streamlit**
- Captura(s) de pantalla del prototipo (usar imágenes del Manual de Usuario/Anexos si están disponibles)
- Módulos funcionales listados:
  - Selector de proyecto (navegación a carpeta Crestron Construct)
  - Selección de panel de destino (modelos TSW-1070, TSW-770, TST-1080, dimensiones personalizadas)
  - 4 temas visuales predefinidos + modo personalizado
  - Log de generación en tiempo real
  - Panel de JSON generado (depuración)

**Diapositiva 17: Cronograma del proyecto**
- Insertar **Figura 16** (Cronograma Gantt — RUP 2026)
- Dato resumen: 14 semanas, 5 iteraciones, desarrollador único

**Diapositiva 18: Pruebas y validación**
- Tabla resumida de resultados de pruebas (Tabla 6):

  | Caso(s) de prueba | Objetivo / Cobertura | Resultado |
  |---|---|---|
  | CP-01 a CP-02 | Generación de .cuig con 4 bloques requeridos | PASA |
  | CP-03 | Unicidad de IDs entre páginas | PASA |
  | CP-04 | Mapeo de coordenadas a CSS (posición absoluta) | PASA |
  | CP-05 a CP-06 | Color de tema y doble @media CSS | PASA |
  | CP-07 a CP-10 | Labels reales y fondo | PASA |
  | CP-11 a CP-14 | Componentes complejos (dpad, keypad, container) | PASA |

- Dato resumen destacado: **14 casos de prueba automatizados con pytest — 100% de resultados positivos**

---

## BLOQUE 5 — Cierre (1 diapositiva | ~0:30 min)

**Diapositiva 19: Resultado esperado y cierre**
- Indicador de impacto proyectado (texto destacado en grande):
  > Reducción proyectada de 40% a 60% en el tiempo de creación de layouts visuales base
- Línea de cierre del proyecto (una sola frase, tipo conclusión general):
  > El AV-MCP Automator permite delegar la estructuración visual de interfaces AV a una IA contextualizada, sin comprometer la compatibilidad con Crestron Construct
- "Gracias" / "Preguntas"

---

## Resumen de distribución de tiempo (20 min)

| Bloque | Diapositivas | Tiempo aprox. |
|---|---|---|
| Portada | 1 | 0:30 |
| La Empresa | 2 | 3:00 |
| El Problema | 3 | 5:00 |
| Objetivos | 1 | 1:30 |
| Ejecución del Sistema | 11 | 9:30 |
| Cierre | 1 | 0:30 |
| **Total** | **19** | **~20:00** |

---

## Anexo — Tarjeta de datos duros (para responder preguntas del jurado, no es diapositiva)

| Dato | Valor |
|---|---|
| Empresa | DACER S.A.C. (Miraflores) |
| Framework objetivo | Crestron CH5 |
| LLM usado | Google Gemini 2.5 Flash-Lite |
| Protocolo | Model Context Protocol (MCP) vía FastMCP (Python) |
| Base de datos vectorial | LanceDB (138 documentos, embeddings 384 dim, modelo all-MiniLM-L6-v2) |
| Interfaz | Streamlit |
| Archivo de salida | `.cuig` (4 bloques: FileMetadata, Html, Css, PageAttributes) |
| Metodología | RUP adaptado — 4 fases, 5 iteraciones, 14 semanas |
| Pruebas | 14 casos (CP-01 a CP-14), 100% éxito |
| Tiempo de respuesta objetivo | < 10 segundos |
| Presupuesto de licencias | S/. 0 |
| RAM objetivo | < 4 GB |
| Reducción de tiempo proyectada | 40% – 60% en maquetación |