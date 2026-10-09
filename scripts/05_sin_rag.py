"""
Comparación — El mismo modelo SIN RAG.

Le hacemos la misma pregunta al modelo, pero sin darle los documentos.
Sirve para ver por qué RAG importa: el modelo no conoce a Cacao Labs,
así que va a decir que no sabe… o peor, va a inventar.

Uso:
    python3 05_sin_rag.py "¿Cuántos días de vacaciones da Cacao Labs el primer año?"
"""

import sys

import boto3

from config import MODEL_ID, REGION

question = sys.argv[1] if len(sys.argv) > 1 else "¿Cuántos días de vacaciones da Cacao Labs en el primer año?"

response = boto3.client("bedrock-runtime", region_name=REGION).converse(
    modelId=MODEL_ID,
    messages=[{"role": "user", "content": [{"text": question}]}],
    inferenceConfig={"maxTokens": 300},
)

print(f"\n🙋 Pregunta: {question}")
print(f"🤖 Modelo (sin documentos): {MODEL_ID}\n")
print(response["output"]["message"]["content"][0]["text"])
