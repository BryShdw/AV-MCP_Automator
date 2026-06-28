# AV-MCP Automator — Documento Maestro de Contexto del Proyecto
> **Versión:** 3.0 — Enfoque Construct Native (.cuig / .cuib) + RUP
> **Empresa:** DACER S.A.C. — Distrito de Miraflores, Lima, Perú
> **Practicante:** Brayan Delgado Oblitas
> **Período:** 06/04/2026 – 29/06/2026 (14 semanas)
> **Última actualización:** Junio 2026

---

## Índice

1. [Identificación del Proyecto](#1-identificación-del-proyecto)
2. [Problema y Solución](#2-problema-y-solución)
3. [Stack Tecnológico](#3-stack-tecnológico)
4. [Arquitectura del Sistema](#4-arquitectura-del-sistema)
5. [El Patrón "Compilador MCP" — Descubrimiento Clave](#5-el-patrón-compilador-mcp--descubrimiento-clave)
6. [Alcance del Sistema (Scope)](#6-alcance-del-sistema-scope)
7. [Restricciones No Negociables (Constraints)](#7-restricciones-no-negociables-constraints)
8. [Roadmap / Cronograma](#8-roadmap--cronograma)
9. [Registro de Decisiones Críticas (Decision Log)](#9-registro-de-decisiones-críticas-decision-log)
10. [Pendientes Abiertos](#10-pendientes-abiertos)
11. [Glosario Técnico](#11-glosario-técnico)

---

## 1. Identificación del Proyecto

| Campo | Valor |
|---|---|
| **Título largo (formato universidad)** | Implementación de un Middleware basado en Model Context Protocol para la Optimización del Diseño de Interfaces Audiovisuales en una Empresa Privada del Distrito de Miraflores, 2026 |
| **Título corto** | AV-MCP Automator (v2 — Construct Native) |
| **Empresa ejecutora** | DACER S.A.C. |
| **Área** | Proyectos e Ingeniería AV (Pro AV) |
| **Universidad** | César Vallejo |
| **Presupuesto de licencias** | S/. 0 — Herramientas 100% gratuitas y open source |

---

## 2. Problema y Solución

### 2.1 Problema

El desarrollo de interfaces gráficas en **Crestron Construct™** consume una parte desproporcionada del tiempo del departamento de ingeniería de DACER S.A.C. en tareas repetitivas: arrastrar, soltar y configurar parámetros estándar para cada sala nueva. Los especialistas AV deben maquetar manualmente cada pantalla táctil, lo que no escala bien ante múltiples proyectos simultáneos.

Un intento anterior de solución consistía en generar código HTML5/CH5 suelto mediante IA, pero **ese código crudo no es editable visualmente en Crestron Construct**. El ingeniero no puede abrir fragmentos HTML en el IDE oficial, lo que rompe el flujo de trabajo real de la empresa.

### 2.2 Solución

Un middleware (AV-MCP) que:

1. Recibe requerimientos en **lenguaje natural** desde una UI web local (Streamlit).
2. Usa IA (Gemini) para razonar la distribución espacial y semántica, devolviendo **únicamente un JSON simple** con componentes y coordenadas.
3. "Compila" ese JSON localmente en **archivos nativos de Crestron Construct** (`.cuig` para páginas, `.cuib` para la configuración del proyecto) mediante un script Python determinista.
4. El ingeniero abre Crestron Construct, ve la pantalla generada y puede editarla visualmente de inmediato.

### 2.3 Objetivo Principal y Métricas de Éxito

| Objetivo | Métrica |
|---|---|
| Eliminar el trabajo repetitivo de maquetación visual | Reducción del **40–60%** en el tiempo de maquetación inicial |
| Generar archivos compatibles con el IDE oficial | **100%** de apertura sin errores en Crestron Construct |
| Mantener costo cero de licencias | Presupuesto de **S/. 0** durante todo el proyecto |

---

## 3. Stack Tecnológico

| Capa | Tecnología | Justificación |
|---|---|---|
| **UI Cliente** | Streamlit (Python) | Framework web ágil para entrada en lenguaje natural; sin necesidad de frontend separado |
| **Servidor MCP / Compilador** | FastMCP (Python) | SDK de alto nivel para exponer herramientas MCP y ejecutar el ensamblaje de archivos `.cuig` |
| **IA Principal** | Gemini 2.5 Flash-Lite (API) | 1,000 llamadas gratuitas/día; maneja la lógica espacial/semántica (JSON), no sintaxis CH5 cruda |
| **Base Vectorial** | LanceDB | < 1 GB RAM; almacena esquemas JSON de componentes CH5 y documentación técnica de Crestron para recuperación semántica |
| **Ecosistema destino** | Crestron Construct™ | IDE visual donde el ingeniero abre, revisa y ajusta los archivos generados |

**Hardware de ejecución:** Lenovo IdeaPad — AMD Ryzen 7 8845HS con NPU Ryzen AI (16 TOPS) + Gráficos Radeon 780M — **16 GB RAM compartida** (restricción crítica de diseño).

---

## 4. Arquitectura del Sistema

### 4.1 Diagrama de Capas

```
+--------------------------------------------------------------------+
|                1. CAPA DE CLIENTE (UI): Streamlit                  |
+---------------------------------+----------------------------------+
                                  | JSON-RPC 2.0 (stdio)
+---------------------------------v----------------------------------+
|       2. SERVIDOR MCP & COMPILADOR: FastMCP (Python)               |
|    [ Herramientas: Search_Tool | Builder_Tool | Cuig_Tool ]        |
+---------------+----------------------------------+-----------------+
                |                                  |
  Llamadas API  |                  Consultas SQL /  |
  (HTTP/REST)   |                  Embeddings       |
+---------------v----------------+ +---------------v-----------------+
| 3. ENRUTADOR IA (Router Layer) | | 4. CAPA DE DATOS: LanceDB       |
|  Principal: Gemini Flash-Lite  | | Esquemas JSON + docs Crestron   |
+---------------------------------+ +--------------------------------+
        ↓ Devuelve JSON espacial/semántico
+--------------------------------------------------------------------+
|      5. CAPA DESTINO: Archivos .cuig / .cuib en disco              |
|         (Abre Crestron Construct™ y edita visualmente)             |
+--------------------------------------------------------------------+
```

### 4.2 Herramientas MCP del Servidor

| Tool | Responsabilidad |
|---|---|
| `Search_Tool` | Busca en LanceDB el esquema JSON estandarizado del componente solicitado |
| `Builder_Tool` | Toma el JSON de la IA y ensambla matemáticamente el archivo `.cuig` válido |
| `Cuig_Tool` | Actualiza el archivo maestro `.cuib` del proyecto para registrar nuevas páginas |

---

## 5. El Patrón "Compilador MCP" — Descubrimiento Clave

> **Este es el cambio arquitectónico más importante del proyecto.** Nació del análisis forense de archivos reales de Crestron Construct.

### 5.1 Anatomía de un Archivo `.cuig`

Un archivo `.cuig` es un **archivo de texto plano** con estructura propietaria dividida en 4 bloques:

- **`{FileMetadata}`** — Versiones, fechas de creación. Casi estático, fácil de replicar.
- **`{Html}`** — DOM de la página con componentes CH5 (`<ch5-button>`, `<ch5-video>`, etc.) a los que Crestron inyecta atributos internos (`ccid_*`) e IDs únicos (ej. `id="i1l4"`).
- **`{Css}`** — Posicionamiento **absoluto** de todos los elementos (`left`, `top`, `width`, `height` en píxeles). Crestron Construct es un editor WYSIWYG que **no usa Flexbox ni Grid**.
- **`{PageAttributes}`** — Formato tipo TOML/INI que Crestron usa para indexar componentes y poblar el panel de propiedades de su UI.

### 5.2 Por Qué la IA No Debe Escribir `.cuig` Directamente

Si Gemini intentara escribir un archivo `.cuig` completo desde cero, fallaría porque:

- Debe generar IDs únicos (ej. `i1l4`) que deben coincidir **exactamente** en los tres bloques: `{Html}`, `{Css}` y `{PageAttributes}`.
- Los atributos internos de Crestron (`ccid_syncproperties`, `devicesvisited`, etc.) son propensos a alucinaciones o errores de omisión.
- El costo en tokens sería enorme para un resultado frágil.

### 5.3 El Flujo del Compilador (Paso a Paso)

```
[1] Usuario en Streamlit
    "Crea una página de proyector con botón ON, OFF y control de volumen"
          |
          v
[2] Search_Tool consulta LanceDB
    → Recupera esquema JSON estandarizado para ch5-button y ch5-slider
          |
          v
[3] Gemini recibe prompt + esquema
    → Devuelve SOLO un JSON simple con lógica espacial/semántica:

    {
      "page_name": "Proyector",
      "elements": [
        { "type": "ch5-button", "label": "Encender",
          "x": 100, "y": 200, "w": 120, "h": 50, "color": "success" },
        { "type": "ch5-button", "label": "Apagar",
          "x": 240, "y": 200, "w": 120, "h": 50, "color": "danger" },
        { "type": "ch5-slider", "label": "Volumen",
          "x": 100, "y": 300, "w": 300, "h": 30 }
      ]
    }
          |
          v
[4] Builder_Tool (Python) ensambla el .cuig:
    - Genera IDs únicos aleatorios por componente
    - Escribe bloque {Html} con atributos ccid_ correctos
    - Escribe bloque {Css} mapeando x→left, y→top, w→width, h→height
    - Escribe bloque {PageAttributes}
    - Guarda Proyector.cuig en la carpeta del proyecto
          |
          v
[5] Cuig_Tool actualiza el archivo .cuib del proyecto
    → Registra la nueva página en el índice maestro
          |
          v
[6] Ingeniero abre Crestron Construct
    → Ve la página generada, puede arrastrar elementos,
      cambiar colores y asignar Joins (señales AV) visualmente
```

### 5.4 Ventajas del Patrón Compilador

- **Cero alucinaciones de sintaxis** — Python ensambla con plantillas predefinidas; el `.cuig` siempre es válido.
- **Ahorro masivo de tokens** — Gemini solo razona sobre un JSON pequeño; no procesa miles de líneas con atributos `ccid_` repetitivos.
- **Flujo de trabajo real** — El especialista AV trabaja directamente en Crestron Construct sin abandonar su IDE oficial.

---

## 6. Alcance del Sistema (Scope)

### 6.1 In-Scope — Lo que el sistema SÍ hace

- **Generación de archivos nativos `.cuig`** — Ensamblaje automatizado de los 4 bloques (`{FileMetadata}`, `{Html}`, `{Css}`, `{PageAttributes}`) exactamente como los lee Crestron Construct.
- **Posicionamiento espacial calculado** — Traducción de coordenadas abstractas del JSON a propiedades CSS absolutas (`top`, `left`, `width`, `height`).
- **Actualización del proyecto (`.cuib`)** — Inserción de referencias a las nuevas páginas creadas en el archivo maestro de configuración.
- **Aislamiento de complejidad sintáctica** — La IA no escribe código Crestron; solo estructura datos (JSON). El script Python hace la escritura cruda.
- **Validación de compatibilidad por tipo de panel** — El servidor MCP restringe o modifica componentes según el panel destino (ej. bloquea QR en paneles serie x60, desactiva Advanced Sliders en iOS).
- **Generación de temas y variables CSS** — Variables CSS configurables por el practicante, compatibles con el Theme Editor de Crestron, definidas durante el desarrollo del proyecto.
- **Biblioteca de plantillas con previsualización** — Plantillas por caso de uso (Salas Corporativas, Educación, Hospitalidad).

### 6.2 Out-of-Scope — Lo que el sistema NO hace

| Funcionalidad excluida | Motivo |
|---|---|
| Generación de HTML/CSS suelto (snippets) | Reemplazado por archivos `.cuig` completos y editables |
| Programación SIMPL Windows / SIMPL# Pro / C# | Restricción académica — fuera del dominio Frontend UI |
| Mapeos de red o direccionamiento IP | Fuera del ecosistema de software del proyecto |
| Instalación física, cableado o calibración | Fuera del alcance de software |
| Descarga automática de drivers de fabricante | No se conecta a portales externos con credenciales |
| Control de la aplicación Crestron Construct | El ingeniero abre la solución manualmente |
| Programación de lógica en Extron ControlScript | Descartado completamente del proyecto |

---

## 7. Restricciones No Negociables (Constraints)

| Restricción | Tipo | Impacto en el diseño | Origen |
|---|---|---|---|
| Solo diseño UI Frontend | Académica | Elimina todo el backend de procesadores del alcance | Tutora universitaria |
| 16 GB RAM compartida con GPU | Técnica | LanceDB e inferencia local deben mantenerse < 4 GB; procesamiento pesado en nube | Hardware (Lenovo IdeaPad) |
| Presupuesto S/. 0 en licencias | Presupuestaria | Stack 100% open source; IA vía cuota gratuita de Google AI Studio | Universidad / Practicante |
| 1,000 llamadas/día en Gemini Flash-Lite | Técnica | Limita la carga de trabajo diaria; justifica el modelo de JSON pequeño (ahorro de tokens) | Google AI Studio Free Tier |
| Ecosistema exclusivamente Crestron CH5 | Técnica/Académica | Descarte total de Extron y cualquier otro fabricante AV | Decisión conjunta tutora + practicante |

**Supuestos (Assumptions):**

- Los archivos `.cuig` y `.cuib` de referencia serán obtenidos por el practicante mediante la documentación oficial de Crestron y proyectos de ejemplo públicos, sin depender de insumos de DACER.
- Las variables CSS (colores, tipografías) del sistema serán definidas por el practicante durante la Fase de Elaboración, usando valores estándar de la librería CH5.
- La tutora universitaria aprobará el avance de la Fase de Inicio al finalizar la Semana 2.

---

## 8. Roadmap / Cronograma (RUP — 14 Semanas)

**Metodología:** RUP adaptado a desarrollador único. 4 fases, 5 iteraciones.

| Fase RUP | Semanas | Iteración | Foco principal |
|---|---|---|---|
| **Inicio** | 1–2 | IT-1 | Requerimientos, análisis forense `.cuig`, casos de uso, riesgos |
| **Elaboración** | 3–5 | IT-2 | DAS, esquema JSON compilador, prototipo ejecutable de arquitectura |
| **Construcción** | 6–9 | IT-3 | Builder_Tool, Router IA, Search_Tool, plantillas Python por componente |
| **Construcción** | 10–12 | IT-4 | UI Streamlit, integración end-to-end, pruebas, corrección de defectos |
| **Transición** | 13–14 | IT-5 | Manual de usuario, guía de despliegue, capacitación, entrega formal |

> Ver documento completo del Roadmap RUP en `AV-MCP_Roadmap_RUP.md`.

---

## 9. Registro de Decisiones Críticas (Decision Log)

| ID | Área | Decisión tomada | Alternativa descartada | Motivo del descarte | Quién decidió |
|---|---|---|---|---|---|
| DEC-001 | Stack IA | Gemini 2.5 Flash-Lite | Gemini Pro | Límite de 100 llamadas/día en capa gratuita vs. 1,000 de Flash-Lite | Practicante |
| DEC-002 | Alcance | Solo diseño Frontend CH5 | Frontend + Backend de procesadores | Restricción explícita de la tutora universitaria | Tutora |
| DEC-003 | Ecosistema | 100% Crestron CH5 | Crestron + Extron ControlScript | Extron involucra lógica de control (Python ControlScript), incompatible con restricción académica | Tutora + Practicante |
| DEC-004 | Arquitectura | Patrón "Compilador MCP" (Python ensambla `.cuig`) | IA genera `.cuig` crudo directamente | Riesgo altísimo de alucinaciones en IDs únicos y atributos `ccid_*` propietarios | Practicante (tras ingeniería inversa) |
| DEC-005 | Stack Base Vectorial | LanceDB | ChromaDB, Pinecone, Weaviate | LanceDB < 1 GB RAM; las alternativas son pesadas o de pago para producción | Practicante |
| DEC-006 | Middleware | FastMCP | Implementación MCP manual desde cero | FastMCP reduce el boilerplate a decoradores simples; acelera el desarrollo en 16 semanas | Practicante |
| DEC-007 | Salida del sistema | Archivos `.cuig` / `.cuib` completos | Snippets HTML/CSS sueltos | Los snippets no son editables visualmente en Crestron Construct; rompen el flujo AV real | Practicante (tras ingeniería inversa) |
| DEC-008 | Cronograma | Actividad final = Manuales de Despliegue | "Redacción del Informe Final" concentrada | El informe se escribe de forma incremental; la empresa necesita manuales operativos como entregable real | Practicante + Tutora |
| DEC-009 | Metodología | RUP adaptado (4 fases, 5 iteraciones, desarrollador único) | Metodología híbrida Cascada+Scrum | RUP cubre explícitamente todas las fases con artefactos formales exigidos por la universidad; Scrum puro no genera artefactos de arquitectura suficientes | Practicante + Tutora |

---

## 10. Pendientes Abiertos

| ID | Descripción | Bloqueador de | Responsable | Urgencia |
|---|---|---|---|---|
| PEN-001 | Obtener archivos `.cuig` y `.cuib` de referencia desde la documentación oficial de Crestron o proyectos de ejemplo públicos | Construcción IT-3 — análisis forense e indexación en LanceDB | Practicante | 🔴 ALTA |
| PEN-002 | Definir paleta de colores y tipografías estándar del sistema (valores CH5 por defecto) | Construcción IT-3 — variables CSS y temas | Practicante | 🟡 MEDIA |
| PEN-003 | Diagramas UML de flujo y secuencia del sistema (Mes 1, Actividad 2) | Entrega académica Semana 4 | Practicante | 🟡 MEDIA |
| PEN-004 | Definición del linter local para validar HTML CH5 antes de ensamblar `.cuig` | Sprint 4 — capa de pruebas | Practicante | 🟡 MEDIA |
| PEN-005 | Estructura de la capa de pruebas del servidor MCP (casos de prueba formales) | Sprint 4 | Practicante | 🟡 MEDIA |
| PEN-006 | Plantillas Python base (`button_template`, `slider_template`) para el Builder_Tool | Sprint 2 — inicio de desarrollo | Practicante | 🔴 ALTA |

---

## 11. Glosario Técnico

**Crestron CH5 (Crestron HTML5 User Interface)**
Framework JavaScript/HTML5 de Crestron para desarrollar interfaces táctiles avanzadas en sistemas de control AV profesional. Reemplaza la tecnología legada SmartGraphics (VT Pro-e). *En este proyecto:* es el ecosistema destino de todos los archivos generados.

**Crestron Construct™**
IDE visual multiplataforma de Crestron (WYSIWYG) para diseñar, empaquetar e importar soluciones de interfaz basadas en CH5. *En este proyecto:* es la herramienta donde el especialista AV abre y edita los archivos generados por el compilador.

**Archivo `.cuig`**
Archivo de texto plano con extensión propietaria de Crestron Construct que representa una **página de la interfaz**. Se divide en 4 bloques: `{FileMetadata}`, `{Html}`, `{Css}`, `{PageAttributes}`. *No confundir con:* archivos HTML estándar — no son intercambiables.

**Archivo `.cuib`**
Archivo maestro de configuración del **proyecto** en Crestron Construct. Indexa todas las páginas (`.cuig`), rutas, componentes y configuraciones globales de la solución. Equivalente al `project-config.json` mencionado en versiones anteriores del proyecto.

**Model Context Protocol (MCP)**
Estándar abierto promovido por Anthropic que define cómo una aplicación provee contexto local seguro (archivos, herramientas, documentación) a un LLM mediante JSON-RPC 2.0. *En este proyecto:* el servidor MCP (FastMCP) actúa como núcleo central que recibe peticiones de Streamlit, consulta LanceDB y enruta el prompt a Gemini o Llama. *No confundir con:* otros usos del acrónimo MCP en electrónica o gestión de proyectos.

**FastMCP**
SDK de Python de alto nivel para construir servidores MCP usando decoradores simples. *En este proyecto:* contiene las tres herramientas principales (`Search_Tool`, `Builder_Tool`, `Cuig_Tool`) y el ensamblador de archivos `.cuig`.

**Patrón "Compilador MCP"**
Arquitectura central del proyecto. La IA solo razona sobre un **JSON pequeño** (qué componentes, dónde y con qué atributos semánticos); el script Python en FastMCP ensambla deterministamente el archivo `.cuig` final. *No confundir con:* compiladores de lenguajes de programación — aquí "compilar" significa transformar JSON abstracto en formato propietario Crestron.

**LanceDB**
Base de datos vectorial local embebida (< 1 GB RAM). *En este proyecto:* almacena esquemas JSON estandarizados de componentes CH5 y documentación técnica de Crestron para recuperación semántica durante el ensamblaje de archivos `.cuig`.

**Joins / Contract Editor**
Sistema de asignación de señales digitales, analógicas o seriales en Crestron que vincula lógicamente un botón de la interfaz CH5 con el procesador físico de la sala. *En este proyecto:* los Joins se asignan manualmente por el especialista AV en Crestron Construct después de que el compilador genera el archivo — están **fuera del alcance del sistema**.

**Posicionamiento Absoluto CH5**
Crestron Construct posiciona todos los elementos mediante CSS absoluto (`position: absolute; left: Xpx; top: Ypx; width: Wpx; height: Hpx`). El Builder_Tool mapea las coordenadas del JSON de la IA directamente a estas propiedades.

**Atributos `ccid_*`**
Atributos internos propietarios que Crestron inyecta en los elementos HTML5 del bloque `{Html}` (ej. `ccid_syncproperties`, `devicesvisited`). Son gestionados por las plantillas Python del Builder_Tool, **no por la IA**.

**Web Xpanel**
Tecnología de Crestron que renderiza un proyecto CH5 en navegadores web (PC o tablet) como panel táctil virtual sin hardware dedicado. *En este proyecto:* puede usarse para previsualizar las páginas generadas sin necesitar un panel físico.

**SIMPL Windows / SIMPL# Pro / C#**
Entornos de programación para la lógica de control de procesadores Crestron. *En este proyecto:* completamente fuera del alcance por restricción académica.

**Extron ControlScript**
Lenguaje Python propietario de Extron para programar procesadores de control AV de esa marca. *En este proyecto:* descartado completamente — el proyecto se limita al ecosistema Crestron CH5.

**Gemini 2.5 Flash-Lite**
Modelo LLM de Google con 1,000 llamadas gratuitas/día en Google AI Studio (Free Tier). *En este proyecto:* motor principal de IA para razonar la distribución espacial/semántica y emitir el JSON del compilador. No genera código CH5 crudo.

---

*Fin del documento de contexto. Versión 3.0 — Junio 2026.*
