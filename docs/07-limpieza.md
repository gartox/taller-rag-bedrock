# 7 · Limpieza de recursos

⏱️ **5 minutos** · ⚠️ **Obligatorio si usaste tu propia cuenta**

> 🎟️ Si usaste una **cuenta de evento**, se borra sola al terminar. Puedes saltarte este módulo.

Borra los recursos **en este orden**.

## Paso 1 · Borra la Knowledge Base

1. Ve a **Amazon Bedrock** → **Knowledge Bases**.
2. Selecciona `kb-cacao-labs` → **Delete**.
3. Escribe `delete` para confirmar.

> 💡 La fuente de datos tiene la política de borrado **Delete** por defecto, así que los vectores se eliminan junto con la Knowledge Base.

## Paso 2 · Borra el bucket de vectores (S3 Vectors)

La opción *Quick create* creó un **vector bucket** que también hay que eliminar.

1. Ve a **Amazon S3** → en el menú izquierdo, **Vector buckets**.
2. Abre el vector bucket que creó Bedrock (su nombre empieza con `bedrock-knowledge-base-…`).
3. Selecciona el **índice vectorial** dentro → **Delete**.
4. Regresa a **Vector buckets**, selecciona el bucket → **Delete**.

<details>
<summary>⚙️ Alternativa: desde CloudShell</summary>

```bash
# Lista tus vector buckets
aws s3vectors list-vector-buckets --region us-east-1

# Reemplaza <VECTOR_BUCKET> con el nombre que viste arriba
aws s3vectors list-indexes --vector-bucket-name <VECTOR_BUCKET> --region us-east-1
aws s3vectors delete-index --vector-bucket-name <VECTOR_BUCKET> --index-name <INDEX> --region us-east-1
aws s3vectors delete-vector-bucket --vector-bucket-name <VECTOR_BUCKET> --region us-east-1
```
</details>

## Paso 3 · Borra el bucket de documentos

En CloudShell:

```bash
export ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
aws s3 rb "s3://taller-rag-${ACCOUNT_ID}" --force
```

## Paso 4 · Borra el rol de IAM (opcional)

Los roles de IAM no cuestan dinero, pero es buena práctica no dejar permisos sueltos.

1. Ve a **IAM** → **Roles**.
2. Busca `AmazonBedrockExecutionRoleForKnowledgeBase`.
3. Selecciónalo → **Delete**.

## ✅ Checkpoint final

- [ ] No aparece ninguna Knowledge Base en Bedrock.
- [ ] No hay vector buckets en S3.
- [ ] Ya no existe el bucket `taller-rag-<mi-cuenta>`.

¡Listo! Tu cuenta quedó limpia. 🧹

---

**[← Retos](06-retos.md)** · **[Siguiente: ¿Qué sigue? →](08-que-sigue.md)**
