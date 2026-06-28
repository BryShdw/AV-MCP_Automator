"""
Pruebas de integración end-to-end — Flujo completo del sistema.
Verifica el pipeline: prompt en lenguaje natural → archivo .cuig válido en disco.

RUP Fase: Construcción — Iteración 4 (Semana 11)
Va al informe: ✅ Sí (evidencia principal del Reporte de Pruebas con capturas WYSIWYG)
"""
import pytest


def test_flujo_completo_genera_cuig(tmp_path):
    """
    CP-03 (integración): Prompt → Search_Tool → Router IA → Builder_Tool → .cuig en disco.
    Requiere: API de Gemini configurada en .env o Ollama corriendo localmente.
    """
    pytest.skip("Requiere stack completo operativo (Semana 11)")


def test_failover_gemini_a_ollama(tmp_path):
    """
    CP-05: Cuando Gemini falla, el sistema conmuta a Ollama y genera el .cuig igualmente.
    """
    pytest.skip("Requiere Ollama corriendo localmente (Semana 11)")


def test_cuig_abre_en_crestron_construct(tmp_path):
    """
    CP-04 (validación WYSIWYG): El .cuig generado se abre sin errores de formato.
    NOTA: Este test es manual — se documenta aquí como registro formal de la prueba.
    Evidencia: captura de pantalla en Crestron Construct adjunta al Reporte de Pruebas.
    """
    pytest.skip("Prueba manual — ver evidencia en deploy/manuals/reporte_pruebas.md")
