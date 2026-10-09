"""
Paso 1 — Solo RECUPERAR (la "R" de RAG).

Le preguntamos a la Knowledge Base qué fragmentos (chunks) se parecen más a la
pregunta. Aquí NO participa ningún modelo generativo: solo búsqueda semántica.

Uso:
    python3 01_retrieve.py "¿Cuántos días de vacaciones tengo?"
"""

import sys

from config import kb_runtime, require_kb_id, source_name

question = sys.argv[1] if len(sys.argv) > 1 else "¿Cuántos días de vacaciones tengo en mi primer año?"
kb_id = require_kb_id()

response = kb_runtime().retrieve(
    knowledgeBaseId=kb_id,
    retrievalQuery={"text": question},
    retrievalConfiguration={
        "vectorSearchConfiguration": {
            "numberOfResults": 3,  # 👈 prueba a cambiar este número
        }
    },
)

print(f"\n🔎 Pregunta: {question}\n")

for i, result in enumerate(response["retrievalResults"], start=1):
    score = result.get("score", 0)
    text = result["content"]["text"].strip().replace("\n", " ")
    print(f"── Resultado {i} · score {score:.3f} · {source_name(result)}")
    print(f"   {text[:300]}{'…' if len(text) > 300 else ''}\n")
