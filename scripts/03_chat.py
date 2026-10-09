"""
Paso 3 — Chat con memoria de conversación.

RetrieveAndGenerate devuelve un 'sessionId'. Si lo mandas en la siguiente
pregunta, Bedrock recuerda el contexto y puedes hacer preguntas de seguimiento
como "¿y en el segundo año?".

Uso:
    python3 03_chat.py
    (escribe 'salir' para terminar, 'nuevo' para empezar otra conversación)
"""

from config import MODEL_ID, kb_runtime, model_arn, require_kb_id, source_name

kb_id = require_kb_id()
client = kb_runtime()
arn = model_arn()

# Plantilla de prompt personalizada.
# $search_results$ y $query$ se reemplazan automáticamente.
PROMPT = """Eres "Cacaobot", el asistente interno de Cacao Labs.
Responde SIEMPRE en español, de forma breve y amable.
Usa ÚNICAMENTE la información de los resultados de búsqueda.
Si la respuesta no está en los resultados, di: "No encontré eso en los documentos de Cacao Labs."

Resultados de búsqueda:
$search_results$

$output_format_instructions$

Pregunta: $query$"""

session_id = None
print(f"🍫 Cacaobot listo (modelo: {MODEL_ID}). Escribe 'salir' para terminar.\n")

while True:
    try:
        question = input("Tú › ").strip()
    except (EOFError, KeyboardInterrupt):
        break
    if not question:
        continue
    if question.lower() in {"salir", "exit", "quit"}:
        break
    if question.lower() == "nuevo":
        session_id = None
        print("🔄 Nueva conversación.\n")
        continue

    request = {
        "input": {"text": question},
        "retrieveAndGenerateConfiguration": {
            "type": "KNOWLEDGE_BASE",
            "knowledgeBaseConfiguration": {
                "knowledgeBaseId": kb_id,
                "modelArn": arn,
                "retrievalConfiguration": {
                    "vectorSearchConfiguration": {"numberOfResults": 5}
                },
                "generationConfiguration": {
                    "promptTemplate": {"textPromptTemplate": PROMPT}
                },
            },
        },
    }
    if session_id:
        request["sessionId"] = session_id

    response = client.retrieve_and_generate(**request)
    session_id = response["sessionId"]

    sources = sorted({
        source_name(ref)
        for c in response.get("citations", [])
        for ref in c.get("retrievedReferences", [])
    })
    print(f"\nCacaobot › {response['output']['text']}")
    if sources:
        print(f"           📚 {', '.join(sources)}")
    print()

print("👋 ¡Hasta luego!")
