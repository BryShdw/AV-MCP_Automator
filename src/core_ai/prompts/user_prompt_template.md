# Plantilla de Prompt de Usuario
**Archivo:** `user_prompt_template.md`

---

Este archivo documenta cómo se construye el prompt de usuario que se envía a Gemini.
El prompt se genera dinámicamente en `router.py` combinando:

1. El input del especialista AV desde Streamlit
2. El esquema JSON del componente recuperado de LanceDB (vía Search_Tool)

## Formato del prompt de usuario

```
Crea el layout JSON para la siguiente pantalla de control AV:

DESCRIPCIÓN DEL USUARIO:
{user_input}

ESQUEMAS DE COMPONENTES DISPONIBLES (recuperados de LanceDB):
{component_schemas}

Recuerda: devuelve SOLO el objeto JSON, sin texto adicional.
```
