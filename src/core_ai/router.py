"""
Capa 3 — Enrutador IA
Modelo: Gemini Pro (sin fallback local — Ollama fue eliminado del proyecto)
RUP: Construcción IT-3 (Semana 8)
"""
import os
import json
import re
from pathlib import Path
import google.generativeai as genai
from dotenv import load_dotenv
from src.core_ai.schemas.layout_schema import LayoutSchema
from pydantic import ValidationError

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL   = os.getenv("GEMINI_MODEL", "gemini-2.0-pro-exp")

genai.configure(api_key=GEMINI_API_KEY)


def _parse_and_validate(raw_text: str) -> dict:
    """Extrae y valida el JSON. Lanza ValueError si algo falla."""
    clean = raw_text.strip()
    # Extraer el bloque JSON ignorando texto adicional (conversacional o markdown)
    start = clean.find('{')
    end = clean.rfind('}')
    
    if start != -1 and end != -1 and end > start:
        clean = clean[start:end+1]
    else:
        # Fallback para array
        start_arr = clean.find('[')
        end_arr = clean.rfind(']')
        if start_arr != -1 and end_arr != -1 and end_arr > start_arr:
            clean = clean[start_arr:end_arr+1]
        else:
            raise ValueError(
                "La respuesta de Gemini no contiene un objeto JSON válido. "
                "Intenta simplificar el prompt."
            )

    try:
        data = json.loads(clean)
    except json.JSONDecodeError as e:
        raise ValueError(
            f"La respuesta de Gemini parece estar truncada o mal formada ({e}). "
            "Esto suele pasar cuando el prompt pide demasiados elementos. "
            "Intenta reducir la cantidad de componentes o el nivel de detalle."
        )

    try:
        validated = LayoutSchema(**data)
        return validated.model_dump()
    except ValidationError as e:
        raise ValueError(f"JSON no cumple el esquema Pydantic: {e}")


def get_layout_from_ai(system_prompt: str, user_prompt: str) -> dict:
    """
    Llama a Gemini y retorna el layout JSON validado.
    Si la respuesta viene mal formateada, reintenta UNA vez con instrucción correctiva.
    Lanza RuntimeError con el mensaje completo si todo falla.
    """
    if not GEMINI_API_KEY:
        raise RuntimeError("GEMINI_API_KEY no está configurada en el archivo .env")

    model = genai.GenerativeModel(
        model_name=GEMINI_MODEL,
        system_instruction=system_prompt,
    )

    errors = []  # Acumular todos los errores para el mensaje final

    # --- Intento 1: llamada normal ---
    try:
        response = model.generate_content(
            user_prompt,
            generation_config=genai.GenerationConfig(
                temperature=0.3,
                max_output_tokens=8192,
                response_mime_type="application/json",
            ),
        )
        return _parse_and_validate(response.text)

    except (ValueError, json.JSONDecodeError) as e:
        # JSON mal formado o no válido según Pydantic — registrar y reintentar
        errors.append(f"Intento 1 (parse/validación): {e}")

    except Exception as e:
        # Error de API (red, cuota, autenticación) — no tiene sentido reintentar
        raise RuntimeError(
            f"Error de API en Gemini ({GEMINI_MODEL}): {type(e).__name__}: {e}"
        )

    # --- Intento 2: reintento con instrucción correctiva ---
    corrective_prompt = (
        f"{user_prompt}\n\n"
        f"IMPORTANTE: Tu respuesta anterior no fue JSON válido. "
        f"Devuelve ÚNICAMENTE el objeto JSON, sin texto adicional, "
        f"sin bloques de código markdown, sin explicaciones."
    )
    try:
        response = model.generate_content(
            corrective_prompt,
            generation_config=genai.GenerationConfig(
                temperature=0.1,        # Temperatura más baja en el reintento
                max_output_tokens=8192,
                response_mime_type="application/json",
            ),
        )
        return _parse_and_validate(response.text)

    except (ValueError, json.JSONDecodeError) as e:
        errors.append(f"Intento 2 (reintento correctivo): {e}")

    except Exception as e:
        errors.append(f"Intento 2 (error de API): {type(e).__name__}: {e}")

    # --- Ambos intentos fallaron: lanzar error completo ---
    error_detail = "\n".join(f"  • {err}" for err in errors)
    raise RuntimeError(
        f"Gemini no pudo generar un layout válido tras 2 intentos "
        f"con el modelo '{GEMINI_MODEL}':\n{error_detail}"
    )


# ─── FUNCIONES DE AYUDA DE PROMPTS PARA EL CLIENTE ─────────────────────────────

def load_system_prompt() -> str:
    """
    Lee el system prompt desde el archivo system_prompt.md.
    """
    _PROMPTS_DIR = Path(__file__).parent / "prompts"
    _SYSTEM_PROMPT_PATH = _PROMPTS_DIR / "system_prompt.md"
    if not _SYSTEM_PROMPT_PATH.exists():
        raise FileNotFoundError(
            f"System prompt no encontrado: {_SYSTEM_PROMPT_PATH}\n"
            "Asegúrate de que el archivo existe en src/core_ai/prompts/system_prompt.md"
        )
    return _SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")


def get_panel_constraints(canvas_w: int, canvas_h: int) -> dict:
    """
    Retorna restricciones de diseño según el tamaño del panel.
    """
    area = canvas_w * canvas_h

    if area <= 800 * 480:  # 5" y menor
        return {
            "min_button_w": 80, "min_button_h": 60,
            "min_font_size": 14,
            "note": "Panel pequeño: botones grandes para facilidad táctil",
        }
    elif area <= 1280 * 800:  # 7"
        return {
            "min_button_w": 100, "min_button_h": 50,
            "min_font_size": 12,
            "note": "Panel mediano: equilibrio entre densidad y táctil",
        }
    else:  # 10" y mayor
        return {
            "min_button_w": 120, "min_button_h": 50,
            "min_font_size": 12,
            "note": "Panel grande: mayor densidad de información posible",
        }


def format_panel_constraints(canvas_w: int, canvas_h: int) -> str:
    """
    Genera el texto de restricciones de panel para inyectar en el system prompt.
    """
    constraints = get_panel_constraints(canvas_w, canvas_h)
    return (
        f"Restricciones tactiles del panel ({constraints['note']}):\n"
        f"- Ancho minimo de botones: {constraints['min_button_w']}px\n"
        f"- Alto minimo de botones: {constraints['min_button_h']}px\n"
        f"- Tamaño minimo de fuente: {constraints['min_font_size']}px\n"
        f"- Todos los elementos deben ser suficientemente grandes para interaccion tactil."
    )


def build_user_prompt(user_input: str, component_schemas: str = "") -> str:
    """
    Construye el prompt de usuario combinando la descripción con los esquemas de LanceDB.
    """
    prompt = (
        "Crea el layout JSON para la siguiente pantalla de control AV:\n\n"
        "DESCRIPCION DEL USUARIO:\n"
        f"{user_input}\n"
    )

    if component_schemas:
        prompt += (
            "\nESQUEMAS DE COMPONENTES DISPONIBLES (recuperados de LanceDB):\n"
            f"{component_schemas}\n"
        )

    prompt += "\nRecuerda: devuelve SOLO el objeto JSON, sin texto adicional."
    return prompt
