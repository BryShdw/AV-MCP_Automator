# Guía de Despliegue — AV-MCP Automator
**RUP Fase:** Transición | **Artefacto:** Guía de Despliegue | **Va al informe:** ✅ Sí
**Destinatario:** Equipo técnico de DACER S.A.C.

---
> ⚠️ Este documento se redacta en la **Semana 13** (Fase de Transición).

## 1. Requisitos del sistema

| Componente | Mínimo recomendado |
|---|---|
| SO | Windows 10/11 (donde corre Crestron Construct) |
| Python | 3.11+ |
| RAM | 8 GB (sin Ollama) / 16 GB (con Ollama activo) |
| Almacenamiento | 5 GB libres (incluye modelo Llama 3.2 3B) |
| GPU | Opcional — AMD/NVIDIA con soporte ROCm/CUDA para acelerar Ollama |

## 2. Variables de entorno requeridas

Ver `.env.example` en la raíz del proyecto.

## 3. Instalación de Ollama (modo offline)

```bash
# Descargar e instalar Ollama desde https://ollama.com
# Descargar el modelo de fallback:
ollama pull llama3.2:3b-instruct-q4_K_M
```

## 4. Inicialización de la base vectorial

```bash
# Ejecutar una sola vez (o cuando se agreguen nuevos componentes CH5 a raw_docs/)
python src/data_layer/ingest.py
```

## 5. Verificación de instalación

```bash
pytest tests/test_builder.py -v
```
