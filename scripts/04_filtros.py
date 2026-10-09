"""
Reto — Filtrar por metadatos.

Cada documento en /data tiene un archivo <nombre>.metadata.json con atributos
como "area" (personas, finanzas, ti) y "anio". Con un filtro, la búsqueda solo
considera los chunks que cumplen la condición.

Uso:
    python3 04_filtros.py finanzas "¿Qué gastos no se reembolsan?"
    python3 04_filtros.py ti       "¿Qué gastos no se reembolsan?"   ← compara
"""

import sys

from config import kb_runtime, require_kb_id, source_name

area = sys.argv[1] if len(sys.argv) > 1 else "finanzas"
question = sys.argv[2] if len(sys.argv) > 2 else "¿Qué gastos no se reembolsan?"
kb_id = require_kb_id()

response = kb_runtime().retrieve(
    knowledgeBaseId=kb_id,
    retrievalQuery={"text": question},
    retrievalConfiguration={
        "vectorSearchConfiguration": {
            "numberOfResults": 3,
            "filter": {"equals": {"key": "area", "value": area}},
        }
    },
)

print(f"\n🔎 Pregunta: {question}")
print(f"🏷️  Filtro:   area = {area}\n")

results = response["retrievalResults"]
if not results:
    print("   (ningún chunk cumple el filtro)")

for i, result in enumerate(results, start=1):
    text = result["content"]["text"].strip().replace("\n", " ")
    meta = result.get("metadata", {})
    print(f"── {i} · score {result.get('score', 0):.3f} · {source_name(result)} · area={meta.get('area')}")
    print(f"   {text[:200]}{'…' if len(text) > 200 else ''}\n")
