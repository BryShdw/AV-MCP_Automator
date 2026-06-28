"""
Capa 3 — Enrutador IA (Router Layer)
Lógica de conmutación: Gemini 2.5 Flash-Lite (principal) → Ollama Llama 3.2 3B (fallback).

RUP Fase: Construcción — Iteración 3 (Semana 8)
"""
import os
import json
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL   = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")
OLLAMA_URL     = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL   = os.getenv("OLLAMA_MODEL", "llama3.2:3b-instruct-q4_K_M")


def call_gemini(system_prompt: str, user_prompt: str) -> dict:
    """
    Llama a la API de Gemini 2.5 Flash-Lite y devuelve el JSON del layout.

    Returns:
        dict con el layout JSON validado

    Raises:
        Exception si la API falla o la cuota está agotada
    """
    # TODO (Semana 8): Implementar con google-generativeai SDK
    raise NotImplementedError("Semana 8 — call_gemini pendiente de implementación")


def call_ollama(system_prompt: str, user_prompt: str) -> dict:
    """
    Llama a Ollama (Llama 3.2 3B local en GPU Radeon 780M) como fallback.

    Returns:
        dict con el layout JSON validado
    """
    # TODO (Semana 8): Implementar con ollama SDK
    raise NotImplementedError("Semana 8 — call_ollama pendiente de implementación")


def get_layout_from_ai(system_prompt: str, user_prompt: str) -> dict:
    """
    Punto de entrada principal del enrutador.
    Intenta Gemini primero; ante cualquier error conmuta a Ollama.

    Returns:
        dict con el layout JSON (schema: ver docs/02_Elaboration/schemas/)
    """
    try:
        return call_gemini(system_prompt, user_prompt)
    except Exception as gemini_error:
        print(f"[Router] Gemini falló ({gemini_error}). Conmutando a Ollama...")
        return call_ollama(system_prompt, user_prompt)
