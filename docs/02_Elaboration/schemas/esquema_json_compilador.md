# Esquema JSON del Compilador — Contrato IA → Builder_Tool
**RUP Fase:** Elaboración — IT-2 (Semana 3) | **Va al informe:** ✅ Sí

## Descripción
Contrato exacto entre Gemini (o Llama) y el Builder_Tool.
La IA devuelve **únicamente** un objeto JSON que cumpla este esquema.
Validado por Pydantic en `src/core_ai/schemas/layout_schema.py`.

> **NOTA DE ARQUITECTURA (Una página por generación):**
> Este esquema asume una relación 1:1 entre el JSON generado y un archivo `.cuig` en Crestron Construct. Como cada archivo `.cuig` representa exactamente una página, la IA debe generar **una sola página por llamada**. Si se requieren múltiples pantallas, se deben procesar como prompts separados.

## Esquema

```json
{
  "page_name": "string — nombre de la página (.cuig)",
  "canvas_width": 1280,
  "canvas_height": 800,
  "elements": [
    {
      "type": "ch5-button | ch5-slider | ch5-video | ch5-text",
      "label": "string — texto visible",
      "x": "integer — píxeles desde la izquierda",
      "y": "integer — píxeles desde arriba",
      "w": "integer — ancho en píxeles",
      "h": "integer — alto en píxeles",
      "color": "success | danger | warning | info | default (opcional)"
    }
  ]
}
```

## Ejemplo válido

```json
{
  "page_name": "Proyector",
  "canvas_width": 1280,
  "canvas_height": 800,
  "elements": [
    { "type": "ch5-button", "label": "Encender", "x": 100, "y": 200, "w": 160, "h": 60, "color": "success" },
    { "type": "ch5-button", "label": "Apagar",   "x": 280, "y": 200, "w": 160, "h": 60, "color": "danger"  },
    { "type": "ch5-slider", "label": "Volumen",  "x": 100, "y": 320, "w": 400, "h": 40 }
  ]
}
```

## Componentes CH5 soportados

| Tipo | Uso típico |
|---|---|
| `ch5-button` | Encender/apagar dispositivos, cambiar fuente, ejecutar macro |
| `ch5-slider` | Volumen, brillo, nivel de iluminación |
| `ch5-video` | Ventana de fuente HDMI, NDI o streaming |
| `ch5-text` | Etiqueta estática o valor dinámico |
