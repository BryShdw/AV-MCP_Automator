# Plan de Pruebas — AV-MCP Automator
**Código:** PLAN-PRUEBAS-001
**Versión:** 1.0
**Fase RUP:** Construcción — Iteración 4

## 1. Objetivo
Asegurar que el sistema AV-MCP Automator genere correctamente los archivos `.cuig` garantizando su apertura sin errores en el IDE oficial Crestron Construct, mediante la validación estructural y semántica de sus cuatro bloques principales.

## 2. Alcance de las pruebas
El alcance comprende las pruebas de la capa de ensamblaje Python (`builder_tool.py`), incluyendo la correcta aplicación del formato CSS absoluto, la generación de los bloques `{FileMetadata}`, `{Html}`, `{Css}` y `{PageAttributes}`, y la garantía de unicidad en la generación de IDs.

## 3. Estrategia
  - 3.1 Pruebas unitarias automatizadas (pytest)
  - 3.2 Pruebas de integración manual (validación en Crestron Construct)

## 4. Casos de prueba planificados
| ID | Descripción | Tipo | Entrada | Resultado esperado |
|---|---|---|---|---|
| CP-01 | Generación de archivo .cuig | Unitaria | layout_simple | Archivo .cuig en disco con ruta correcta |
| CP-02 | 4 bloques obligatorios | Unitaria | layout_simple | Contiene `{FileMetadata}`, `{Html}`, `{Css}`, `{PageAttributes}` |
| CP-03 | Unicidad de IDs | Unitaria | Múltiples layouts | Los IDs generados no se repiten entre páginas |
| CP-04 | Mapeo de coordenadas | Unitaria | layout_con_coordenadas | CSS generado refleja `x`, `y`, `w`, `h` como `left`, `top`, `width`, `height` |
| CP-05 | Color de tema base | Unitaria | layout_con_color | El div de fondo (`ibedd`) aplica el color especificado |
| CP-06 | Doble bloque `@media` | Unitaria | layout_simple | CSS contiene sintaxis doble `@media` requerida |
| CP-07 | Labels en HTML | Unitaria | layout_con_labels | Bloque `{Html}` contiene `ccid_label` correctamente asignado |
| CP-08 | Labels en PageAttributes | Unitaria | layout_con_labels | Bloque `{PageAttributes}` refleja los labels asignados |
| CP-09 | Div de fondo | Unitaria | layout_simple | El componente `Background` (div `ibedd`) es el primer elemento |
| CP-10 | Componente ch5-button | Unitaria | layout_con_boton | Mapeo correcto de atributos de botón |
| CP-11 | Componente ch5-dpad | Unitaria | layout_con_dpad | Generación estructural correcta del dpad |
| CP-12 | Componente ch5-keypad | Unitaria | layout_con_keypad | Generación estructural correcta del keypad |
| CP-13 | Anidación de containers | Unitaria | layout_con_container | Jerarquía correcta en HTML y CSS para componentes anidados |
| CP-14 | Validación Pydantic | Unitaria | JSON_invalido | Error capturado y manejado correctamente antes del ensamblaje |

## 5. Criterios de aceptación
Todos los casos de prueba unitarios deben pasar al 100%. Las validaciones manuales en Crestron Construct no deben arrojar errores de parseo de archivos.

## 6. Herramientas
- pytest 8.x
- Python 3.11+
- Crestron Construct (para validación manual)

## 7. Responsable
Brayan Delgado Oblitas
