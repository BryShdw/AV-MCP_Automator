"""
Modelos Pydantic para validar el JSON devuelto por Gemini.
Si el JSON no cumple el esquema, se lanza ValidationError antes de llegar al Builder_Tool.

RUP Fase: Construcción — Iteración 3 (Semana 8, junto con el Router)
"""
from typing import Literal, Optional
from pydantic import BaseModel, Field, model_validator


class CH5Element(BaseModel):
    type: Literal[
        "ch5-button", "ch5-slider", "ch5-video", "ch5-text", "ch5-toggle",
        "ch5-gauge", "ch5-dpad", "ch5-keypad", "ch5-image",
        "ch5-tab-button", "ch5-video-switcher", "container", "ch5-header",
    ]
    label: str = Field(default="", description="Texto visible en el componente")
    x: int = Field(ge=0, description="Posición horizontal en píxeles")
    y: int = Field(ge=0, description="Posición vertical en píxeles")
    w: int = Field(gt=0, description="Ancho en píxeles")
    h: int = Field(gt=0, description="Alto en píxeles")
    color: Optional[Literal["success", "danger", "warning", "info", "default"]] = "default"
    join_digital: Optional[int] = Field(default=None, ge=1, le=65535)
    join_analog:  Optional[int] = Field(default=None, ge=1, le=65535)

    # Solo aplican a ch5-tab-button — ignorados por el resto de tipos
    tab_count: Optional[int] = Field(
        default=None, ge=2, le=6,
        description="Cantidad de pestañas. Solo para ch5-tab-button.",
    )
    tab_items: Optional[list[str]] = Field(
        default=None,
        description=(
            "Nombres internos opcionales de cada pestaña (solo para "
            "ch5-tab-button). No hay garantía de que el texto sea visible "
            "en el touch panel sin configuración manual en Construct."
        ),
    )

    # Solo aplican a ch5-video-switcher — ignorados por el resto de tipos
    source_count: Optional[int] = Field(
        default=None, ge=1, le=8,
        description="Cantidad de fuentes. Solo para ch5-video-switcher.",
    )
    screen_count: Optional[int] = Field(
        default=None, ge=1, le=4,
        description="Cantidad de pantallas. Solo para ch5-video-switcher.",
    )

    # Solo aplica a type="container"
    panel_background_color: Optional[str] = Field(
        default=None,
        description="Color de fondo del panel (hex). Solo para type='container'. Si no se especifica, queda transparente.",
    )
    border_color: Optional[str] = Field(
        default=None,
        description="Color de borde del panel (hex). Solo para type='container'.",
    )
    border_width: Optional[int] = Field(
        default=None, ge=0, le=10,
        description="Grosor de borde en px. Solo para type='container'.",
    )
    border_radius: Optional[int] = Field(
        default=None, ge=0, le=40,
        description="Radio de esquina en px. Solo para type='container'.",
    )

    # Aplica a ch5-button, ch5-text y ch5-header — color del texto del label
    text_color: Optional[str] = Field(
        default=None,
        description="Color del texto del label (hex). Si no se especifica, usa el color por defecto del componente.",
    )

    # --- Tipografía (solo ch5-text) ---
    font_size: Optional[int] = Field(
        default=None, ge=8, le=200,
        description=(
            "Tamaño de fuente en px. Solo para ch5-text. "
            "Úsalo para jerarquía tipográfica: 64-120px para elemento "
            "dominante (reloj, número grande), 28-48px para títulos "
            "de zona, 14-20px para etiquetas secundarias."
        ),
    )
    font_weight: Optional[Literal["300", "400", "600", "700"]] = Field(
        default=None,
        description="Peso de fuente. '300' ligero, '400' normal, '600' semibold, '700' bold.",
    )
    letter_spacing: Optional[int] = Field(
        default=None, ge=-5, le=20,
        description="Espaciado entre letras en px. Solo para ch5-text.",
    )

    # --- Forma y sombra (ch5-button y container) ---
    shape: Optional[Literal["circle", "rounded-rectangle", "rectangle"]] = Field(
        default=None,
        description=(
            "Forma del botón. 'circle' requiere w == h (cuadrado perfecto). "
            "Por defecto 'rounded-rectangle'. Solo para ch5-button."
        ),
    )
    box_shadow: Optional[str] = Field(
        default=None,
        description=(
            "Box shadow CSS (ej. '0 4px 24px rgba(0,0,0,0.5)'). "
            "Aplica a ch5-button y container. Añade profundidad visual."
        ),
    )
    opacity: Optional[float] = Field(
        default=None, ge=0.1, le=1.0,
        description="Opacidad del elemento (0.1-1.0). Aplica a container.",
    )

    # --- Gradiente (solo container) ---
    background_gradient: Optional[str] = Field(
        default=None,
        description=(
            "Gradiente CSS para el fondo del container, en lugar de "
            "panel_background_color sólido. "
            "Ejemplo: 'linear-gradient(135deg, #1a2035 0%, #0d1117 100%)'. "
            "Si se especifica, tiene prioridad sobre panel_background_color."
        ),
    )


class LayoutSchema(BaseModel):
    page_name: str = Field(min_length=1, description="Nombre de la página (.cuig)")
    canvas_width:  int = Field(default=1280, gt=0)
    canvas_height: int = Field(default=800,  gt=0)
    
    # Colores del tema generados por la IA
    theme_background_color: Optional[str] = Field(default=None, description="Color de fondo principal (hex). Ej: #121212")
    theme_primary_color: Optional[str] = Field(default=None, description="Color primario de acento (hex). Ej: #A8C5E6")
    theme_text_color: Optional[str] = Field(default=None, description="Color del texto principal (hex). Ej: #E0E0E0")
    theme_border_color: Optional[str] = Field(default=None, description="Color de bordes suaves (hex). Ej: #2A2A2A")
    theme_panel_background_color: Optional[str] = Field(default=None, description="Color de fondo de los paneles (hex). Ej: #1E1E1E")

    elements: list[CH5Element] = Field(min_length=1)

    @model_validator(mode='after')
    def validate_elements_fit_canvas(self):
        """
        Verifica que ningun elemento se salga del area del canvas.
        Se ejecuta despues de validar cada campo individual.
        """
        for el in self.elements:
            if el.x + el.w > self.canvas_width:
                raise ValueError(
                    f"Elemento '{el.label}' (x={el.x}, w={el.w}) se sale del canvas "
                    f"horizontalmente (canvas_width={self.canvas_width})"
                )
            if el.y + el.h > self.canvas_height:
                raise ValueError(
                    f"Elemento '{el.label}' (y={el.y}, h={el.h}) se sale del canvas "
                    f"verticalmente (canvas_height={self.canvas_height})"
                )
        return self
