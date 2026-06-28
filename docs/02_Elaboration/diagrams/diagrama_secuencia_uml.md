# Diagrama de Secuencia UML — Flujo Completo (CU-01)
**RUP Fase:** Elaboración — IT-2 (Semana 5) | **Va al informe:** ✅ Sí

## Flujo principal: Generar página

```
Ingeniero AV    Streamlit     Servidor MCP    LanceDB    Router IA    Gemini    Disco
     │              │               │              │           │           │        │
     │─ prompt ────>│               │              │           │           │        │
     │              │─ JSON-RPC ───>│              │           │           │        │
     │              │               │─ search ────>│           │           │        │
     │              │               │<─ esquema ───│           │           │        │
     │              │               │─ prompt ────────────────>│           │        │
     │              │               │              │           │─ API ─────────────>│(Gemini)
     │              │               │              │           │<─ JSON layout ─────│
     │              │               │<─ JSON ──────────────────│           │        │
     │              │               │─ build .cuig ──────────────────────────────>│(disco)
     │              │               │─ update .cuib ─────────────────────────────>│
     │              │<─ ruta ───────│              │           │           │        │
     │<─ "Listo" ───│               │              │           │           │        │
```
