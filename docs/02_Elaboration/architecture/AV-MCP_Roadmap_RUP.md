# Roadmap — Metodología RUP Adaptada (Desarrollador Único)
## Proyecto: AV-MCP Automator | DACER S.A.C. | 14 Semanas

---

## Marco Metodológico

Se aplica el **Proceso Unificado Racional (RUP)** en su estructura de 4 fases canónicas
(**Inicio → Elaboración → Construcción → Transición**), adaptado a un equipo de un solo
desarrollador que asume todos los roles: Analista, Diseñador, Desarrollador y Tester.

Las iteraciones dentro de cada fase son acotadas para mantener el foco en el entregable
principal: el **compilador MCP** que genera archivos `.cuig` / `.cuib` válidos para
Crestron Construct™.

### Roles asumidos por el desarrollador

| Rol RUP | Responsabilidad en este proyecto |
|---|---|
| Gestor de Proyecto | Planifica semanas, controla avance, registra riesgos |
| Analista | Levanta requerimientos, define casos de uso, modela arquitectura |
| Diseñador | Define la arquitectura MCP, esquemas JSON, estructura `.cuig` |
| Desarrollador | Implementa FastMCP, Builder_Tool, UI Streamlit |
| Tester | Pruebas de integración, validación WYSIWYG en Crestron Construct |

### Artefactos RUP utilizados

| Artefacto | Descripción breve | ¿Va al informe? |
|---|---|---|
| Visión del Proyecto | Alcance, objetivos y stakeholders | ✅ Sí |
| Modelo de Casos de Uso | UC del sistema desde la perspectiva del especialista AV | ✅ Sí |
| Especificación de Requisitos | Requisitos funcionales y no funcionales | ✅ Sí |
| Documento de Arquitectura del Software (DAS) | Capas, componentes, patrón Compilador MCP | ✅ Sí |
| Plan de Iteración | Tareas y metas de cada iteración | ✅ Sí |
| Prototipo de Interfaz | UI Streamlit operativa | ✅ Sí |
| Código fuente versionado | Repositorio del servidor MCP + Builder_Tool | ⬜ No (se referencia) |
| Plan de Pruebas | Casos de prueba de integración y WYSIWYG | ✅ Sí |
| Reporte de Pruebas | Resultados de validación en Crestron Construct | ✅ Sí |
| Manual de Usuario | Guía operativa para el ingeniero AV del proyecto | ✅ Sí |

---

## Distribución de Fases en 14 Semanas

```
Sem  1   2   3   4   5   6   7   8   9  10  11  12  13  14
     |-------|   |-----------|   |---------------|   |-------|
       INICIO     ELABORACIÓN       CONSTRUCCIÓN    TRANSICIÓN
      2 semanas   3 semanas          7 semanas       2 semanas
```

| Fase | Semanas | Duración | Iteraciones |
|---|---|---|---|
| **Inicio** | 1 – 2 | 2 semanas | 1 iteración |
| **Elaboración** | 3 – 5 | 3 semanas | 1 iteración |
| **Construcción** | 6 – 12 | 7 semanas | 2 iteraciones |
| **Transición** | 13 – 14 | 2 semanas | 1 iteración |

---

## FASE 1 — INICIO (Semanas 1–2)

**Objetivo de la fase:** Establecer el alcance del proyecto, identificar los riesgos
principales y lograr el acuerdo de los stakeholders (ingenieros AV de DACER + tutora universitaria)
sobre qué se va a construir y por qué.

**Hito de salida:** *Lifecycle Objective Milestone* — Visión aprobada + arquitectura
candidata identificada.

### Iteración 1 (Semanas 1–2)

#### Semana 1 — Definición y Análisis

| Tarea | Descripción | Artefacto generado | ¿Al informe? |
|---|---|---|---|
| Levantamiento de requerimientos | Observación del flujo de trabajo actual de los ingenieros AV de DACER: tipos de sala, componentes CH5 más usados, flujo actual de maquetación | Acta de reunión + lista de requerimientos | ✅ Sí |
| Redacción del documento Visión | Define el problema, la solución propuesta, stakeholders, objetivos y métricas de éxito (40–60% reducción de tiempo) | Documento de Visión | ✅ Sí |
| Análisis forense de archivos `.cuig` / `.cuib` | Ingeniería inversa de archivos .cuig de referencia (documentación oficial de Crestron): identificar bloques `{FileMetadata}`, `{Html}`, `{Css}`, `{PageAttributes}`, atributos `ccid_*` e IDs únicos | Informe de análisis forense | ✅ Sí |

#### Semana 2 — Modelado Inicial y Riesgos

| Tarea | Descripción | Artefacto generado | ¿Al informe? |
|---|---|---|---|
| Modelo de Casos de Uso (nivel alto) | Identificar los 4–5 casos de uso principales del sistema: *Generar página*, *Actualizar proyecto*, *Consultar plantilla*, *Validar archivo*, *Previsualizar resultado* | Diagrama de Casos de Uso UML | ✅ Sí |
| Especificación de Requisitos | Documentar requisitos funcionales (RF) y no funcionales (RNF): RF01 Generar `.cuig`, RF02 Actualizar `.cuib`, RNF01 Tiempo de respuesta < 10 s, RNF02 Presupuesto S/.0, etc. | Documento de Especificación de Requisitos | ✅ Sí |
| Lista de Riesgos | Identificar riesgos técnicos (alucinaciones de IA, límite de tokens, compatibilidad `.cuig`) y mitigaciones | Lista de Riesgos con Plan de Mitigación | ✅ Sí |

> **Dependencia crítica:** Los archivos .cuig de referencia deben estar disponibles antes del inicio del Sprint 1.
> reales en la **Semana 1**. Sin estos archivos el análisis forense no es posible y la
> la Fase de Elaboración queda bloqueada.

---

## FASE 2 — ELABORACIÓN (Semanas 3–5)

**Objetivo de la fase:** Definir la arquitectura del sistema de forma completa y
validada, eliminar los riesgos técnicos de alto impacto y establecer la base estable
sobre la que se construirá el compilador.

**Hito de salida:** *Lifecycle Architecture Milestone* — Documento de Arquitectura del
Software (DAS) completo + prototipo de arquitectura ejecutable (servidor MCP levantado
con una herramienta de prueba).

### Iteración 2 (Semanas 3–5)

#### Semana 3 — Arquitectura del Software

| Tarea | Descripción | Artefacto generado | ¿Al informe? |
|---|---|---|---|
| Documento de Arquitectura del Software (DAS) | Formalizar el patrón "Compilador MCP": capas, responsabilidades, protocolo JSON-RPC 2.0 (stdio), flujo de datos de extremo a extremo, decisiones de diseño y su justificación | DAS con diagramas de Componentes y Secuencia UML | ✅ Sí |
| Diseño del esquema JSON del compilador | Definir el contrato exacto entre Gemini y el Builder_Tool: campos obligatorios, tipos, valores permitidos por componente (`ch5-button`, `ch5-slider`, `ch5-video`, etc.) | Esquema JSON documentado (con ejemplos) | ✅ Sí |

#### Semana 4 — Diseño de Componentes y Base de Datos

| Tarea | Descripción | Artefacto generado | ¿Al informe? |
|---|---|---|---|
| Diseño del Builder_Tool | Especificar en pseudocódigo / diagrama de flujo cómo Python genera cada bloque del `.cuig`: generación de IDs únicos, mapeo de coordenadas a CSS absoluto, inyección de atributos `ccid_*` | Diagrama de flujo del Builder_Tool | ✅ Sí |
| Diseño del esquema LanceDB | Definir la estructura de las colecciones vectoriales: campos, tipos de embedding, esquemas JSON indexados por componente CH5 | Modelo de datos LanceDB | ✅ Sí |

#### Semana 5 — Prototipo Ejecutable de Arquitectura

| Tarea | Descripción | Artefacto generado | ¿Al informe? |
|---|---|---|---|
| Servidor FastMCP base operativo | Levantar el servidor MCP con una herramienta de prueba (`ping_tool`) que confirme comunicación JSON-RPC 2.0 con Streamlit via stdio | Servidor MCP funcional (código) | ⬜ No |
| LanceDB inicializado con datos semilla | Indexar al menos 3 esquemas JSON de componentes CH5 (`ch5-button`, `ch5-slider`, `ch5-video`) para validar la recuperación semántica | Script de inicialización LanceDB | ⬜ No |
| Validación del prototipo arquitectónico | Ejecutar una consulta completa: Streamlit → MCP → LanceDB → respuesta. Documentar que la arquitectura es viable | Registro de validación (capturas + log) | ✅ Sí |

---

## FASE 3 — CONSTRUCCIÓN (Semanas 6–12)

**Objetivo de la fase:** Implementar el sistema completo de forma iterativa, priorizando
el componente central (Builder_Tool) en la primera iteración y la interfaz + integración
completa en la segunda.

**Hito de salida:** *Initial Operational Capability Milestone* — Sistema funcional
end-to-end: prompt en Streamlit → archivo `.cuig` válido que abre sin errores en
Crestron Construct™.

### Iteración 3 — Núcleo del Compilador (Semanas 6–9)

**Meta de iteración:** El Builder_Tool genera archivos `.cuig` correctos a partir de un
JSON de entrada manual (sin Gemini aún). El archivo abre en Crestron Construct sin
errores de formato.

#### Semana 6 — Implementación del Builder_Tool

| Tarea | Descripción | Artefacto generado | ¿Al informe? |
|---|---|---|---|
| Plantillas Python por componente | Implementar las plantillas base para `ch5-button` y `ch5-slider`: generación de ID único, bloque `{Html}` con atributos `ccid_*`, bloque `{Css}` con posicionamiento absoluto | Código: `templates/button.py`, `templates/slider.py` | ⬜ No |
| Generador del bloque `{FileMetadata}` | Función Python que escribe la cabecera del `.cuig` con versiones y fecha de creación | Código: `builders/metadata.py` | ⬜ No |
| Generador del bloque `{PageAttributes}` | Función Python que genera el índice TOML/INI de componentes de la página | Código: `builders/page_attributes.py` | ⬜ No |

#### Semana 7 — Integración del Compilador Completo

| Tarea | Descripción | Artefacto generado | ¿Al informe? |
|---|---|---|---|
| Builder_Tool completo (ensamblador `.cuig`) | Función principal que orquesta las 4 secciones del `.cuig` a partir de un JSON de entrada y escribe el archivo en disco | Código: `tools/builder_tool.py` | ⬜ No |
| Cuig_Tool (actualizador `.cuib`) | Función que parsea el archivo `.cuib` del proyecto Crestron y registra la nueva página generada | Código: `tools/cuig_tool.py` | ⬜ No |

#### Semana 8 — Integración con IA (Gemini + Fallback)

| Tarea | Descripción | Artefacto generado | ¿Al informe? |
|---|---|---|---|
| Enrutador de IA (Router Layer) | Implementar la lógica de conmutación: llamada primaria a Gemini 2.5 Flash-Lite vía API| Código: `router/ai_router.py` | ⬜ No |
| Prompts del sistema para Gemini | Escribir y ajustar el system prompt que restringe a Gemini a emitir **únicamente** el JSON espacial/semántico del esquema definido (sin texto libre, sin código CH5 crudo) | Archivo: `prompts/system_prompt.txt` | ✅ Sí |

#### Semana 9 — Search_Tool y Primera Validación

| Tarea | Descripción | Artefacto generado | ¿Al informe? |
|---|---|---|---|
| Search_Tool (consulta LanceDB) | Implementar la herramienta MCP que recibe el tipo de componente solicitado y devuelve el esquema JSON correspondiente desde LanceDB | Código: `tools/search_tool.py` | ⬜ No |
| Prueba de integración Iteración 3 | Ejecutar el flujo completo: JSON manual → Builder_Tool → `.cuig` → abrir en Crestron Construct y verificar renderización WYSIWYG. Documentar resultado | Reporte de prueba de Iteración 3 | ✅ Sí |

---

### Iteración 4 — UI, Integración Completa y Pruebas (Semanas 10–12)

**Meta de iteración:** El flujo completo funciona end-to-end desde Streamlit: el usuario
escribe un prompt en lenguaje natural y el sistema genera el archivo `.cuig` listo para
abrir en Crestron Construct.

#### Semana 10 — Interfaz de Usuario (Streamlit)

| Tarea | Descripción | Artefacto generado | ¿Al informe? |
|---|---|---|---|
| UI Streamlit operativa | Implementar la interfaz: campo de entrada en lenguaje natural, selector de tipo de sala/panel, botón de generación, área de log del proceso y enlace al archivo generado | Código: `ui/app.py` | ⬜ No |
| Integración Streamlit → servidor MCP | Conectar la UI con el servidor FastMCP vía stdio (JSON-RPC 2.0) y verificar el envío/recepción de mensajes | Código de integración | ⬜ No |

#### Semana 11 — Pruebas de Integración Completas

| Tarea | Descripción | Artefacto generado | ¿Al informe? |
|---|---|---|---|
| Plan de Pruebas | Definir los casos de prueba: CP01 Generación de botón, CP02 Generación de slider, CP03 Generación de página completa (3+ componentes), CP04 Validación WYSIWYG en Construct, CP05 Prueba de failover Gemini | Plan de Pruebas | ✅ Sí |
| Ejecución del Plan de Pruebas | Ejecutar cada caso de prueba, registrar resultado (Pasa / Falla), capturar evidencias (screenshots de Crestron Construct con la página renderizada) | Reporte de Pruebas con evidencias | ✅ Sí |

#### Semana 12 — Corrección y Estabilización

| Tarea | Descripción | Artefacto generado | ¿Al informe? |
|---|---|---|---|
| Corrección de defectos | Resolver los fallos identificados en el Plan de Pruebas. Priorizar defectos que impidan abrir el `.cuig` en Crestron Construct | Log de defectos corregidos | ✅ Sí |
| Re-ejecución de pruebas fallidas | Confirmar que los defectos corregidos pasan. Actualizar el Reporte de Pruebas | Reporte de Pruebas final (actualizado) | ✅ Sí |

---

## FASE 4 — TRANSICIÓN (Semanas 13–14)

**Objetivo de la fase:** Entregar el sistema operativo a DACER S.A.C., capacitar al
especialista AV que lo usará y documentar todo lo necesario para que la empresa pueda
operarlo sin el desarrollador presente.

**Hito de salida:** *Product Release Milestone* — Sistema instalado en el entorno de
DACER + Manual de Usuario entregado y validado por la empresa.

### Iteración 5 (Semanas 13–14)

#### Semana 13 — Documentación y Manual de Usuario

| Tarea | Descripción | Artefacto generado | ¿Al informe? |
|---|---|---|---|
| Manual de Usuario | Guía operativa para el ingeniero AV: cómo iniciar el servidor, cómo ingresar un prompt, cómo abrir el `.cuig` generado en Crestron Construct, solución de problemas frecuentes | Manual de Usuario (PDF) | ✅ Sí |
| Guía de Despliegue | Instrucciones para instalar el sistema en cualquier equipo con Crestron Construct: dependencias Python, clave de API de Gemini, variables de entorno | Guía de Despliegue (PDF) | ✅ Sí |

#### Semana 14 — Entrega, Capacitación y Cierre

| Tarea | Descripción | Artefacto generado | ¿Al informe? |
|---|---|---|---|
| Capacitación al ingeniero AV | Sesión práctica: el especialista genera al menos 2 páginas completas usando el sistema. Se registran observaciones y ajustes menores | Acta de capacitación | ✅ Sí |
| Entrega formal a DACER S.A.C. | Firma del acta de conformidad del sistema por parte de DACER. Entrega del código fuente, manuales y guías | Acta de conformidad / Carta de aceptación | ✅ Sí |
| Medición de la métrica de éxito | Comparar el tiempo de maquetación manual (baseline registrado en Semana 1) vs. tiempo con el sistema AV-MCP. Documentar el porcentaje de reducción alcanzado | Informe de resultados (métrica 40–60%) | ✅ Sí |

---

## Resumen de Artefactos por Fase

| Fase | Artefactos que van al informe |
|---|---|
| **Inicio** | Documento de Visión, Modelo de Casos de Uso, Especificación de Requisitos, Lista de Riesgos, Informe de Análisis Forense `.cuig` |
| **Elaboración** | DAS (con diagramas UML de Componentes y Secuencia), Esquema JSON del compilador, Diagrama de flujo del Builder_Tool, Modelo de datos LanceDB, Registro de validación del prototipo |
| **Construcción** | System prompt de Gemini, Reporte de prueba Iteración 3, Plan de Pruebas, Reporte de Pruebas final (con evidencias WYSIWYG), Log de defectos |
| **Transición** | Manual de Usuario, Guía de Despliegue, Acta de capacitación, Acta de conformidad del proyecto, Informe de resultados |

---

## Vista Consolidada de 14 Semanas

```
SEM  FASE          ITERACIÓN   FOCO PRINCIPAL
───  ────────────  ──────────  ─────────────────────────────────────────────
 1   Inicio        IT-1        Requerimientos + análisis forense .cuig
 2   Inicio        IT-1        Casos de uso + especificación + riesgos
 3   Elaboración   IT-2        Documento de Arquitectura (DAS) + esquema JSON
 4   Elaboración   IT-2        Diseño Builder_Tool + modelo LanceDB
 5   Elaboración   IT-2        Prototipo ejecutable de arquitectura
 6   Construcción  IT-3        Plantillas Python por componente CH5
 7   Construcción  IT-3        Builder_Tool completo + Cuig_Tool
 8   Construcción  IT-3        Router IA (Gemini + Ollama fallback)
 9   Construcción  IT-3        Search_Tool + prueba de integración IT-3
10   Construcción  IT-4        UI Streamlit + integración con servidor MCP
11   Construcción  IT-4        Plan de Pruebas + ejecución
12   Construcción  IT-4        Corrección de defectos + re-pruebas
13   Transición    IT-5        Manual de Usuario + Guía de Despliegue
14   Transición    IT-5        Capacitación ingeniero AV + entrega + métrica final
```
