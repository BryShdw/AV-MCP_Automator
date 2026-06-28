# Análisis Forense de Archivos .cuig / .cuib
**RUP Fase:** Inicio — IT-1 (Semana 1) | **Va al informe:** ✅ Sí

## Objetivo
Documentar la estructura interna de archivos .cuig y .cuib obtenidos de
la documentación oficial de Crestron o proyectos de ejemplo públicos,
para diseñar las plantillas Python del Builder_Tool.

## Fuentes de archivos de referencia
- Documentación oficial de Crestron Construct™
- Proyectos de ejemplo en el portal de desarrolladores de Crestron
- Proyectos generados por el practicante durante la Fase de Inicio

## Estructura de un archivo .cuig

### Bloque {FileMetadata}
```
<!-- Pegar ejemplo real aquí tras el análisis -->
```

### Bloque {Html}
```html
<!-- Pegar ejemplo real aquí -->
<!-- Anotar: atributos ccid_*, formato de id único (ej. i1l4), componentes CH5 -->
```

### Bloque {Css}
```css
/* Pegar ejemplo real aquí */
/* Confirmar: position:absolute, unidades en px */
```

### Bloque {PageAttributes}
```
<!-- Pegar ejemplo real aquí -->
<!-- Anotar: formato TOML/INI, campos requeridos por componente -->
```

## Atributos ccid_* encontrados
| Atributo | Valor observado | Función inferida |
|---|---|---|
| ccid_syncproperties | | |
| devicesvisited | | |

## Componentes CH5 presentes
| Componente | Atributos propios observados |
|---|---|
| `<ch5-button>` | |
| `<ch5-slider>` | |

## Conclusiones para el Builder_Tool
<!-- Qué plantillas son necesarias, qué campos son dinámicos vs estáticos -->
