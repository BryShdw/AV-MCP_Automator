# Reporte de Resultados de Pruebas
**Código:** REPORTE-PRUEBAS-001
**Fecha de ejecución:** 14 de junio de 2026
**Referencia:** PLAN-PRUEBAS-001

## Resumen ejecutivo
- Total de casos ejecutados: 14
- Casos exitosos: 14
- Casos fallidos: 0
- Cobertura: 100% de la capa de ensamblaje Python

## Resultados por caso de prueba
| ID | Descripción | Resultado | Observaciones |
|---|---|---|---|
| CP-01 | Generación de archivo .cuig | PASA | Archivo creado exitosamente en la ruta destino |
| CP-02 | 4 bloques obligatorios | PASA | Sintaxis de bloques perfecta |
| CP-03 | Unicidad de IDs | PASA | Función `_scan_existing_ids` evita colisiones |
| CP-04 | Mapeo de coordenadas | PASA | Reglas CSS aplicadas en posicionamiento absoluto |
| CP-05 | Color de tema base | PASA | Color base `background_color` mapeado |
| CP-06 | Doble bloque `@media` | PASA | Cumple la restricción estructural de Construct |
| CP-07 | Labels en HTML | PASA | Asignación en atributos `ccid_label` correcta |
| CP-08 | Labels en PageAttributes | PASA | Consistencia en índice de panel derecho |
| CP-09 | Div de fondo | PASA | Fondo renderizado en la capa inferior |
| CP-10 | Componente ch5-button | PASA | Componente base operando |
| CP-11 | Componente ch5-dpad | PASA | Estructura compleja renderiza sin error |
| CP-12 | Componente ch5-keypad | PASA | Estructura compleja renderiza sin error |
| CP-13 | Anidación de containers | PASA | Elementos anidados correctamente reflejados |
| CP-14 | Validación Pydantic | PASA | Filtra intentos de alucinación del LLM |

## Evidencia
- Suite ejecutada con: `pytest tests/test_builder.py -v`
- Fecha de ejecución: 14/06/2026
- Resultado de consola: `14 passed in 0.85s`

## Pruebas de integración manual
| Escenario probado | Panel destino | Tema visual | Resultado |
|---|---|---|---|
| Sala de Conferencias | TSW-770 | Dark Pro | PASA — .cuig abre sin errores |
| Aula Educativa | TSW-1070 | Corporate Blue | PASA — .cuig abre sin errores |
| Auditorio Principal | TST-1080 | Slate Dark | PASA — .cuig abre sin errores |

## Limitaciones identificadas
1. Las pruebas cubren la capa de ensamblaje Python pero no incluyen pruebas de integración automatizadas con Crestron Construct real. La validación en IDE fue manual.
2. `button_template.py` usa `labelInnerHTML` en PascalCase dentro del HTML, lo cual es interpretado de forma irregular por Crestron Construct en algunas vistas (reportado en bugs menores y solucionado durante S12).

## Conclusión
El sistema ha demostrado generar archivos con los estándares matemáticos y sintácticos exactos requeridos, cumpliendo el RNF-04 del 100% de compatibilidad en la apertura de los archivos generados en Crestron Construct sin emitir excepciones en el IDE.

## Firma del responsable
_________________________
Brayan Delgado Oblitas — Practicante
Fecha: 14/06/2026
