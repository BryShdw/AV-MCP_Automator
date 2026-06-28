"""
Modelos Pydantic para validar el JSON devuelto por Gemini (o Llama).
Si el JSON no cumple el esquema, se lanza ValidationError antes de llegar al Builder_Tool.

RUP Fase: Construcción — Iteración 3 (Semana 8, junto con el Router)
"""
from typing import Literal, Optional
from pydantic import BaseModel, Field


class CH5Element(BaseModel):
    type: Literal["ch5-button", "ch5-slider", "ch5-video", "ch5-text"]
    label: str = Field(default="", description="Texto visible en el componente")
    x: int = Field(ge=0, description="Posición horizontal en píxeles")
    y: int = Field(ge=0, description="Posición vertical en píxeles")
    w: int = Field(gt=0, description="Ancho en píxeles")
    h: int = Field(gt=0, description="Alto en píxeles")
    color: Optional[Literal["success", "danger", "warning", "info", "default"]] = "default"
    join_digital: Optional[int] = Field(default=None, ge=1, le=65535)
    join_analog:  Optional[int] = Field(default=None, ge=1, le=65535)


class LayoutSchema(BaseModel):
    page_name: str = Field(min_length=1, description="Nombre de la página (.cuig)")
    canvas_width:  int = Field(default=1280, gt=0)
    canvas_height: int = Field(default=800,  gt=0)
    elements: list[CH5Element] = Field(min_length=1)
