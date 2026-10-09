# 0 · Prerrequisitos y entorno

⏱️ **10 minutos**

Antes de empezar necesitas una cuenta de AWS y una terminal en la nube. Elige **una** de estas dos rutas:

| | 🎟️ En el evento | 🏠 Por tu cuenta |
|---|---|---|
| ¿Quién lo usa? | Asistentes presenciales que recibieron un código | Cualquier persona, en cualquier momento |
| Cuenta de AWS | Temporal, la da el instructor | La tuya |
| Costo | $0 | Menos de 1 USD si haces la limpieza |
| Guía | [Configuración en el evento](evento-aws.md) | [Configuración con tu cuenta](cuenta-propia.md) |

Cuando termines tu ruta, regresa aquí y haz la verificación final.

---

## ✅ Verificación final (las dos rutas)

### 1. Confirma la región

Arriba a la derecha de la consola de AWS, selecciona **US East (N. Virginia) `us-east-1`**.

> 💡 Usa la misma región durante **todo** el taller. La mayoría de los errores de "no encuentro mi recurso" vienen de cambiar de región sin darte cuenta.

### 2. Abre AWS CloudShell

1. En la barra superior de la consola, haz clic en el ícono de terminal **`>_`** (CloudShell).
2. Espera a que cargue (la primera vez tarda ~1 minuto).

CloudShell es una terminal Linux dentro del navegador que ya trae **Python 3**, **boto3** y la **AWS CLI** configurados con tus credenciales. No tienes que instalar nada.

### 3. Descarga el material del taller

En CloudShell, ejecuta:

```bash
git clone https://github.com/<ORG>/taller-rag-bedrock.git
cd taller-rag-bedrock
ls
```

Debes ver las carpetas `data/`, `docs/` y `scripts/`.

### 4. Verifica que tienes acceso a los modelos

```bash
aws bedrock list-foundation-models \
  --region us-east-1 \
  --query "modelSummaries[?modelId=='amazon.titan-embed-text-v2:0' || modelId=='amazon.nova-2-lite-v1:0'].modelId" \
  --output table
```

Debes ver los dos modelos en la tabla:

- `amazon.titan-embed-text-v2:0` → convierte texto en vectores (embeddings).
- `amazon.nova-2-lite-v1:0` → genera las respuestas.

> 💡 En Amazon Bedrock, los modelos serverless se habilitan automáticamente la primera vez que los usas. Ya no hay que pedir acceso modelo por modelo, salvo en casos especiales (ver [Solución de problemas](../troubleshooting.md)).

---

**[← Inicio](../../README.md)** · **[Siguiente: Conceptos →](../01-conceptos.md)**
