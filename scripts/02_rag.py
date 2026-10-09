"""
Paso 2 — RECUPERAR + GENERAR (RAG completo) con citas.

Una sola llamada a RetrieveAndGenerate hace todo:
  1. Busca los chunks relevantes en la Knowledge Base.
  2. Se los pasa al modelo junto con tu pregunta.
  3. Devuelve la respuesta y las citas que la respaldan.

Uso:
    python3 02_rag.py "¿Cómo pido un reembolso de gastos?"
"""

import sys

from config import MODEL_ID, kb_runtime, model_arn, require_kb_id, source_name

question = sys.argv[1] if len(sys.argv) > 1 else "¿Cómo pido un reembolso de gastos de viaje?"
kb_id = require_kb_id()

response = kb_runtime().retrieve_and_generate(
    input={"text": question},
    retrieveAndGenerateConfiguration={
        "type": "KNOWLEDGE_BASE",
        "knowledgeBaseConfiguration": {
            "knowledgeBaseId": kb_id,
            "modelArn": model_arn(),
            "retrievalConfiguration": {
                "vectorSearchConfiguration": {"numberOfResults": 5}
            },
        },
    },
)

print(f"\n🙋 Pregunta: {question}")
print(f"🤖 Modelo:   {MODEL_ID}\n")
print("✅ Respuesta:\n")
print(response["output"]["text"])

# Cada cita une un fragmento de la respuesta con los chunks que lo respaldan.
sources = []
for citation in response.get("citations", []):
    for ref in citation.get("retrievedReferences", []):
        name = source_name(ref)
        if name not in sources:
            sources.append(name)

print("\n📚 Fuentes:")
if sources:
    for i, name in enumerate(sources, start=1):
        print(f"   [{i}] {name}")
else:
    print("   (sin citas: el modelo no encontró información en los documentos)")
