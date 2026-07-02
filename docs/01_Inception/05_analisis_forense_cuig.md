# Análisis Forense — Archivos Nativos de Crestron Construct™
**RUP Fase:** Inicio — IT-1 (Semana 1) | **Va al informe:** ✅ Sí
**Fuente:** Proyecto "Exercise 1" analizado el 27/06/2026
**Versión de Crestron Construct:** 1.4601.12.0 (ProjectApp) / 2.1101.2.0 (AppHost)

---

## 1. Estructura de Carpetas del Proyecto

```
Solutions/
└── Exercise 1/                          ← Carpeta raíz del proyecto
    ├── Exercise 1.cse                   ← Estado del explorador (JSON) — IGNORAR
    └── Exercise 1/                      ← Carpeta interna con los archivos reales
        ├── Exercise 1.cse               ← Estado del explorador (JSON) — IGNORAR
        ├── Exercise 1                   ← Archivo "Crestron Construct Solution"
        ├── Exercise 1                   ← Archivo "Crestron Construct UI Project"
        ├── Exercise 1.cuib              ← Configuración del proyecto (JSON)
        ├── Home.cuig                    ← Página "Home" de la interfaz
        └── Page 3.cuig                  ← Página "Page 3" de la interfaz
```

**Conclusión clave:** Cada página de la interfaz = un archivo `.cuig` independiente.
El archivo `.cuib` registra el proyecto pero NO contiene páginas — solo metadatos.

---

## 2. Anatomía del Archivo .cuib (Exercise 1.cuib)

Formato: **JSON puro**

```json
{
  "FileMetadata": {
    "_createdByProjectApp": "1.4601.12.0",
    "_lastModifiedByProjectApp": "1.4601.12.0",
    "_schema": "1.0.0.0",
    "_createdByAppHost": "2.1101.2.0",
    "_created": "2026-06-09T14:35:48.2930451-05:00",
    "_lastModifiedByAppHost": "2.1101.2.0",
    "_minimumAppHost": "2.901.0",
    "_modified": "2026-06-09T14:35:48.2930143-05:00"
  },
  "HardButtons": []
}
```

**Conclusión clave para el Cuig_Tool:**
- El `.cuib` es JSON simple. Para agregar una página basta con actualizar `_modified`.
- Las páginas NO se registran en el `.cuib` — Crestron Construct las detecta
  automáticamente por presencia de archivos `.cuig` en la misma carpeta.
- El `Cuig_Tool` solo necesita **escribir el `.cuig` en la carpeta correcta**.
  No necesita modificar el `.cuib`. Esto simplifica enormemente la arquitectura.

---

## 3. Anatomía del Archivo .cuig — Los 4 Bloques

### Bloque 1: {FileMetadata}

```
{FileMetadata}
Schema = "1.0.0.0"
CreatedByAppHost = "2.1101.2.0"
Created = 2026-06-23 20:49:03.017511-05:00
LastModifiedByAppHost = "2.1101.2.0"
Modified = 2026-06-23 20:49:03.017503-05:00
CreatedByProjectApp = "1.4601.12.0"
LastModifiedByProjectApp = "1.4601.12.0"
MinimumProjectApp = "1.2600.1"
MinimumAppHost = "2.901.0"
```

**Campos y valores a usar en el Builder_Tool:**
| Campo | Valor fijo a usar |
|---|---|
| Schema | "1.0.0.0" |
| CreatedByAppHost | "2.1101.2.0" |
| LastModifiedByAppHost | "2.1101.2.0" |
| CreatedByProjectApp | "1.4601.12.0" |
| LastModifiedByProjectApp | "1.4601.12.0" |
| MinimumProjectApp | "1.2600.1" |
| MinimumAppHost | "2.901.0" |
| Created / Modified | `datetime.now()` con formato `%Y-%m-%d %H:%M:%S.%f%z` |

---

### Bloque 2: {Html}

Contiene los componentes CH5 como HTML. Patrón universal detectado:

```html
<ch5-COMPONENT atributos... id="XXXX" componentname="Nombre"
  ccid_linksendreceive="True" ccid_componenttype="Tipo"
  devicesvisited="[&quot;TST-1080 (Landscape)&quot;]">
              </ch5-COMPONENT>
```

**Formato de ID único:**
- Patrón observado: `i` + 3-4 caracteres alfanuméricos en minúscula
- Ejemplos reales: `i1l4`, `iw5g`, `iec5`, `i2e3i`, `ih6z`, `ihlc`, `iwiy`
- Generación: `"i" + uuid4().hex[:3]` es suficiente (colisión despreciable)

**Atributos OBLIGATORIOS en TODOS los componentes CH5:**
| Atributo | Valor |
|---|---|
| `id` | ID único generado (ej. `i1l4`) |
| `componentname` | Nombre legible (ej. `"Button"`, `"Slider"`) |
| `ccid_linksendreceive` | `"True"` (siempre) |
| `ccid_componenttype` | Tipo del componente (ej. `"Button"`, `"Slider"`) |
| `devicesvisited` | `"[&quot;TST-1080 (Landscape)&quot;]"` (hardcoded) |

---

### Bloque 3: {Css}

Posicionamiento **absoluto** para TODOS los elementos. Patrón exacto:

```css
@media (max-width: 99999px){
  #CANVAS_ID { background-color: #ffffff; }
  #ELEMENT_ID {
    display: block;
    left: Xpx;
    top: Ypx;
    position: absolute;
    width: Wpx;
    height: Hpx;
  }
  /* ...más elementos... */
}
@media (orientation: landscape) and (max-width: 1281px) and (max-height: 801px),
       (orientation: landscape) and (max-width: 1279px) {
  /* Mismas reglas repetidas para responsive landscape */
}
```

**Conclusión crítica para el Builder_Tool:**
- Hay **DOS bloques `@media`**: el primero universal (`max-width: 99999px`) y
  el segundo para landscape específico. Ambos contienen las **mismas reglas CSS**.
- El ID del canvas/fondo de página es diferente al de los elementos (ej. `#infy`).
- `display: block` es obligatorio en todos los elementos.
- El CSS específico por componente se agrega DESPUÉS de las propiedades base:
  - Slider: `#i2e3i .noUi-touch-area { slidertouchareapadding_padding: 0px; }`
  - Font: `#XXXX :not(i):not(svg) { font-family: 'Roboto'; }`

---

### Bloque 4: {PageAttributes}

Formato **TOML personalizado** de Crestron. Estructura exacta:

```toml
[Attributes]
Name = "Nombre de la página"
PageMode = "absolute"
Id = "uuid4-completo-aqui"
StartPage = "False"
PreloadPage = "False"
CachePage = "False"
VisibilityJoin = "0"
DisplayBackgroundColor = "False"

[[Elements]]
Type = "Ch5 Button"          ← Nombre tipo Crestron (NO el tag HTML)
Editable = true

[[Elements.Components]]
Type = "textnode"
Content = "\n              "

[Elements.Attributes]
id = "i1l4"                  ← Mismo ID que en {Html} y {Css}
componentName = "Button"
ccid_linkSendReceive = "True"
ccid_ComponentType = "Button"
devicesVisited = "[\"TST-1080 (Landscape)\"]"
... (atributos específicos del componente)
```

**Mapeo de Type en PageAttributes vs tag HTML:**
| Tag HTML | Type en PageAttributes |
|---|---|
| `ch5-button` | `Ch5 Button` |
| `ch5-slider` | `Ch5 Slider` |
| `ch5-video` | `Ch5 Video` |
| `ch5-text` | `Ch5 Text` |
| `ch5-toggle` | `Ch5 Toggle` |
| `ch5-tab-button` | `Ch5 Tab Button` |
| `ch5-datetime` | `Ch5 Date Time` |
| `ch5-textinput` | `Ch5 Textinput` |
| `ch5-image` | `Ch5 Image` |
| `ch5-dpad` | `Ch5 Dpad` |
| `ch5-keypad` | `Ch5 Keypad` |

---

## 4. Catálogo de Componentes CH5 Detectados

### ch5-button (PRIORITARIO — componente más común)

**HTML mínimo funcional:**
```html
<ch5-button
  orientation="horizontal" size="regular" shape="rounded-rectangle"
  type="default" halignlabel="center" valignlabel="middle"
  checkboxshow="false" checkboxposition="left" disabled="false"
  clearlabel="false" iconposition="first" tagname="ch5-button"
  ccid_imageicontype="iconclass" ccid_linksendreceive="True"
  iconurlfilltype="initial" customclass="ccid-custom"
  affectedbypreviewstate="True" ccid_syncproperties="syncEnabled"
  ccid_lastsizeselected="regular" customvstheme="custom"
  id="XXXX" componentname="Button"
  ccid_activefont="'Roboto'" ccid_label="label" labelinnerhtml="TEXTO_LABEL"
  assetid="0" pageflip="0"
  ccid_componenttype="Button"
  devicesvisited="[&quot;TST-1080 (Landscape)&quot;]">
</ch5-button>
```

**CSS mínimo:**
```css
#XXXX { display:block; left:Xpx; top:Ypx; position:absolute; width:Wpx; height:Hpx; }
```

**PageAttributes mínimo:**
```toml
[[Elements]]
Type = "Ch5 Button"
Editable = true
[[Elements.Components]]
Type = "textnode"
Content = "\n              "
[Elements.Attributes]
id = "XXXX"
componentName = "Button"
ccid_linkSendReceive = "True"
ccid_ComponentType = "Button"
devicesVisited = "[\"TST-1080 (Landscape)\"]"
```

---

### ch5-slider (PRIORITARIO — control de volumen/brillo)

**HTML mínimo funcional:**
```html
<ch5-slider
  nohandle="false" size="regular" orientation="horizontal"
  tapsettable="false" handleshape="rounded-rectangle" handlesize="regular"
  tooltipshowtype="off" tooltipdisplaytype="%" value="50"
  slidertype="fader" customvstheme="custom"
  min="0" max="100" step="1"
  id="XXXX" componentname="Slider"
  ccid_linksendreceive="True" ccid_componenttype="Slider"
  devicesvisited="[&quot;TST-1080 (Landscape)&quot;]">
</ch5-slider>
```

**CSS mínimo:**
```css
#XXXX { width:Wpx; height:Hpx; display:block; left:Xpx; top:Ypx; position:absolute; }
#XXXX .noUi-touch-area { slidertouchareapadding_padding: 0px; }
#XXXX .ch5-slider :not(i):not(svg) { font-family: Roboto; }
```

**PageAttributes mínimo:**
```toml
[[Elements]]
Type = "Ch5 Slider"
Editable = true
[[Elements.Components]]
Type = "textnode"
Content = "\n              "
[Elements.Attributes]
nohandle = "false"
size = "regular"
orientation = "horizontal"
value = "50"
min = "0"
max = "100"
step = "1"
id = "XXXX"
componentName = "Slider"
ccid_linkSendReceive = "True"
ccid_ComponentType = "Slider"
devicesVisited = "[\"TST-1080 (Landscape)\"]"
```

---

### ch5-video

**HTML mínimo:**
```html
<ch5-video aspectratio="16:9" sourcetype="Network" snapshotrefreshrate="5"
  size="regular" id="XXXX" componentname="Video"
  ccid_linksendreceive="True" ccid_componenttype="Video"
  devicesvisited="[&quot;TST-1080 (Landscape)&quot;]">
</ch5-video>
```

**CSS:** `#XXXX { display:block; left:Xpx; top:Ypx; position:absolute; width:Wpx; height:auto; }`
`#XXXX .ch5-video { display:block; }`

---

### ch5-text

**HTML mínimo:**
```html
<ch5-text clearlabel="false" labelmodeadvncomponent="simple"
  horizontalalignment="center" verticalalignment="middle"
  multilinesupport="false" truncatetext="false"
  id="XXXX" componentname="Formatted-Text"
  ccid_activefont="'Roboto'" ccid_label="label" labelinnerhtml="label"
  ccid_linksendreceive="True" ccid_componenttype="Formatted-Text"
  devicesvisited="[&quot;TST-1080 (Landscape)&quot;]" ccid_themecssset="true">
</ch5-text>
```

---

### ch5-toggle

**HTML mínimo:**
```html
<ch5-toggle handleshape="circle" orientation="horizontal" size="regular"
  value="false" customvstheme="custom"
  id="XXXX" componentname="Toggle"
  ccid_activefont="'Roboto'" ccid_label=""
  ccid_linksendreceive="True" ccid_componenttype="Toggle"
  devicesvisited="[&quot;TST-1080 (Landscape)&quot;]">
</ch5-toggle>
```

---

## 5. Reglas Críticas para el Builder_Tool

### Regla 1: IDs únicos
```python
import uuid
def generate_cuig_id() -> str:
    return "i" + uuid.uuid4().hex[:4]
# Ejemplos: i1l4, iw5g, iec5, i2e3i
```

### Regla 2: Canvas ID de página
Cada página tiene un ID de fondo (ej. `infy`) que aparece en el CSS:
`#infy { background-color: #ffffff; }`
Este también se genera con `generate_cuig_id()`.

### Regla 3: Timestamp exacto
```python
from datetime import datetime, timezone, timedelta
def get_cuig_timestamp() -> str:
    # Formato: "2026-06-23 20:49:03.017511-05:00"
    tz = timezone(timedelta(hours=-5))  # Zona horaria Lima (UTC-5)
    return datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S.%f")[:-0] + "-05:00"
```

### Regla 4: El .cuib NO necesita modificarse
Las páginas se detectan automáticamente por presencia de `.cuig` en la carpeta.
El `Cuig_Tool` = simplemente escribir el archivo `.cuig` en la ruta correcta.

### Regla 5: Doble bloque @media en CSS
```python
css_block = f"""@media (max-width: 99999px){{{css_rules}}}
@media (orientation: landscape) and (max-width: 1281px) and (max-height: 801px), (orientation: landscape) and (max-width: 1279px){{{css_rules}}}"""
```
Las reglas CSS van duplicadas en ambos bloques (exactamente iguales).

### Regla 6: Page ID en PageAttributes
Cada página tiene un UUID completo (no el ID corto de 4 chars):
```python
import uuid
page_id = str(uuid.uuid4())  # "1e0c8935-4589-4826-90d1-a1660e9a58c5"
```

---

## 6. Simplificación Arquitectónica Descubierta

**Lo que creíamos que haría el Cuig_Tool:** Parsear y modificar el `.cuib`.
**Lo que realmente hace:** Solo escribe el `.cuig` en la carpeta del proyecto.

Esto elimina el `Cuig_Tool` como herramienta MCP separada.
El `Builder_Tool` hace todo: genera el contenido Y escribe el archivo en disco.
La arquitectura queda más simple y robusta.

**Nueva arquitectura de herramientas MCP:**
| Tool | Responsabilidad |
|---|---|
| `Search_Tool` | Recupera esquemas JSON de componentes CH5 desde LanceDB |
| `Builder_Tool` | Genera el `.cuig` completo Y lo escribe en disco |

El `Cuig_Tool` se elimina — no es necesario.
