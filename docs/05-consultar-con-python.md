# 5 · Consúltala con Python

⏱️ **25 minutos** · 🛠️ Hands-on

## Objetivo

Usar tu Knowledge Base desde código, como lo harías en una aplicación real: una web, un bot de Telegram o un backend.

Vas a usar **boto3**, el SDK de AWS para Python, con dos APIs del cliente `bedrock-agent-runtime`:

| API | ¿Qué hace? | ¿Usa modelo generativo? |
|---|---|---|
| `retrieve` | Devuelve los chunks más relevantes | ❌ No |
| `retrieve_and_generate` | Busca, genera la respuesta y devuelve citas | ✅ Sí |

## Preparación

En CloudShell:

```bash
cd ~/taller-rag-bedrock/scripts
export KB_ID="PEGA_AQUI_TU_ID"   # si no lo tienes ya
ls
```

Todos los scripts leen su configuración de `config.py`. Por defecto usan **us-east-1** y el modelo **`us.amazon.nova-2-lite-v1:0`**.

> 💡 El prefijo `us.` indica un **perfil de inferencia**: Bedrock puede atender tu petición en varias regiones de EE. UU. para tener más capacidad.

---

## Paso 1 · Solo recuperar (`01_retrieve.py`)

```bash
python3 01_retrieve.py "¿Cuántos días de vacaciones tengo en mi primer año?"
```

Salida esperada (similar):

```
🔎 Pregunta: ¿Cuántos días de vacaciones tengo en mi primer año?

── Resultado 1 · score 0.712 · reglamento-interno.md
   ## 3. Vacaciones Cacao Labs otorga más días de vacaciones que el mínimo…

── Resultado 2 · score 0.583 · reglamento-interno.md
   …
```

### Lee el código

```python
response = kb_runtime().retrieve(
    knowledgeBaseId=kb_id,
    retrievalQuery={"text": question},
    retrievalConfiguration={
        "vectorSearchConfiguration": {
            "numberOfResults": 3,  # 👈 top-k
        }
    },
)
```

### 🧪 Experimenta

- Haz una pregunta de otro tema: `python3 01_retrieve.py "¿Qué red Wi-Fi uso?"`
- Abre el archivo con `nano 01_retrieve.py`, cambia `numberOfResults` a `1` y luego a `8`. Guarda con `Ctrl+O`, `Enter` y sal con `Ctrl+X`.
- **Pregunta:** ¿qué pasa con los scores de los resultados más bajos?

---

## Paso 2 · RAG completo con citas (`02_rag.py`)

```bash
python3 02_rag.py "¿Cómo pido un reembolso de gastos de viaje?"
```

Salida esperada (similar):

```
🙋 Pregunta: ¿Cómo pido un reembolso de gastos de viaje?
🤖 Modelo:   us.amazon.nova-2-lite-v1:0

✅ Respuesta:

Para pedir un reembolso entra a "Jícara", crea un reporte de gastos, adjunta
la factura CFDI y envíalo a tu líder para aprobación. Finanzas paga los días
10 y 25 de cada mes. Tienes 30 días naturales para enviarlo.

📚 Fuentes:
   [1] politica-gastos-y-viajes.md
```

### Lee el código

```python
response = kb_runtime().retrieve_and_generate(
    input={"text": question},
    retrieveAndGenerateConfiguration={
        "type": "KNOWLEDGE_BASE",
        "knowledgeBaseConfiguration": {
            "knowledgeBaseId": kb_id,
            "modelArn": model_arn(),  # 👈 qué modelo redacta la respuesta
            "retrievalConfiguration": {
                "vectorSearchConfiguration": {"numberOfResults": 5}
            },
        },
    },
)
```

Una sola llamada hace **todo el flujo de RAG**. Las citas vienen en `response["citations"]`.

---

## Paso 3 · ¿Y sin RAG? (`05_sin_rag.py`)

Hagamos la misma pregunta **directo al modelo**, sin darle los documentos:

```bash
python3 05_sin_rag.py "¿Cuántos días de vacaciones da Cacao Labs en el primer año?"
```

Compara con la respuesta de `02_rag.py`. El modelo no conoce a Cacao Labs, así que dirá que no sabe o, peor, **inventará** una cifra.

> 🎯 Esta comparación es la razón de ser de RAG.

---

## Paso 4 · Chat con memoria (`03_chat.py`)

```bash
python3 03_chat.py
```

Prueba una conversación con preguntas de seguimiento:

```
Tú › ¿Cuántos días de vacaciones tengo el primer año?
Tú › ¿y en el tercero?
Tú › ¿con cuánta anticipación las pido?
Tú › salir
```

La segunda pregunta ("¿y en el tercero?") solo funciona porque mandamos el `sessionId` de la respuesta anterior:

```python
if session_id:
    request["sessionId"] = session_id
response = client.retrieve_and_generate(**request)
session_id = response["sessionId"]
```

### El prompt personalizado

Este script cambia las instrucciones que recibe el modelo con un **prompt template**:

```python
PROMPT = """Eres "Cacaobot", el asistente interno de Cacao Labs.
Responde SIEMPRE en español, de forma breve y amable.
Usa ÚNICAMENTE la información de los resultados de búsqueda.
Si la respuesta no está en los resultados, di: "No encontré eso en los documentos de Cacao Labs."

Resultados de búsqueda:
$search_results$

$output_format_instructions$

Pregunta: $query$"""
```

| Variable | Bedrock la reemplaza por… |
|---|---|
| `$search_results$` | Los chunks recuperados |
| `$query$` | La pregunta del usuario |
| `$output_format_instructions$` | Instrucciones para generar las citas |

### 🧪 Experimenta

- Pregunta `¿Puedo llevar a mi perro?`. ¿Usa la frase de "No encontré eso…"?
- Cambia la personalidad del bot en `PROMPT`. Por ejemplo, que responda como guía de turistas tabasqueño. 🌴

## ✅ Checkpoint

- [ ] Ejecuté `retrieve` y vi los chunks con su score.
- [ ] Ejecuté `retrieve_and_generate` y vi la respuesta con fuentes.
- [ ] Comparé con la respuesta del modelo sin RAG.
- [ ] Tuve una conversación de seguimiento con `03_chat.py`.

---

**[← Pruébala en la consola](04-probar-en-consola.md)** · **[Siguiente: Retos →](06-retos.md)**
