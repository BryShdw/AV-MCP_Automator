# Diagrama de Flujo — Builder_Tool
**RUP Fase:** Elaboración — IT-2 (Semana 4) | **Va al informe:** ✅ Sí

## Flujo de ensamblaje del .cuig

```
ENTRADA: dict (JSON validado por Pydantic)
    │
    ▼
[1] Generar ID único por elemento
    uuid4()[:4] → formato Crestron (ej. "i1l4")
    │
    ▼
[2] Construir bloque {FileMetadata}
    metadata_template.py → versión, fecha, nombre de página
    │
    ▼
[3] Construir bloque {Html}
    Para cada elemento:
    button_template / slider_template / video_template
    → Inyectar: id único, atributos ccid_*, label
    │
    ▼
[4] Construir bloque {Css}
    Para cada elemento:
    f"#{id} { position:absolute; left:{x}px; top:{y}px; width:{w}px; height:{h}px; }"
    │
    ▼
[5] Construir bloque {PageAttributes}
    page_attributes_template.py → índice TOML/INI
    │
    ▼
[6] Escribir archivo en disco
    output_path / {page_name}.cuig
    (output_path = carpeta seleccionada desde la UI)
    │
    ▼
SALIDA: ruta absoluta del .cuig generado
```

## Invariantes garantizados
- Cada ID generado es único dentro del .cuig
- El mismo ID aparece en {Html}, {Css} y {PageAttributes} sin excepción
- x, y, w, h siempre se mapean a left, top, width, height en píxeles
- El .cuig siempre abre sin errores en Crestron Construct
