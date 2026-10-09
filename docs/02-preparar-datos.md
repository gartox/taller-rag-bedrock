# 2 · Prepara tus datos en S3

⏱️ **10 minutos** · 🛠️ Hands-on

## Objetivo

Subir los documentos de **Cacao Labs** a un bucket de Amazon S3. Ese bucket será la **fuente de datos** de tu Knowledge Base.

## Conoce los documentos

En la carpeta `data/` hay cuatro documentos de una empresa ficticia:

| Archivo | Contenido | Área |
|---|---|---|
| `reglamento-interno.md` | Horario, trabajo remoto, vacaciones, capacitación | personas |
| `politica-gastos-y-viajes.md` | Viáticos, transporte y reembolsos | finanzas |
| `guia-seguridad-ti.md` | Laptops, contraseñas, uso de IA, Wi-Fi | ti |
| `faq-onboarding.md` | Primer día, nómina y prestaciones | personas |

Cada documento tiene un archivo hermano `.metadata.json` con **metadatos** (área y año). Los usaremos en los retos.

```bash
cat data/reglamento-interno.md.metadata.json
```

```json
{
  "metadataAttributes": {
    "area": "personas",
    "anio": 2026
  }
}
```

> 📁 La carpeta `data/extra/` tiene un documento que **no** vamos a subir todavía. Lo usaremos en el reto de re-sincronización.

## Paso 1 · Crea el bucket

En **CloudShell**, desde la carpeta `taller-rag-bedrock`:

```bash
# Guardamos el ID de tu cuenta para que el nombre del bucket sea único en el mundo
export ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
export BUCKET="taller-rag-${ACCOUNT_ID}"

aws s3 mb "s3://${BUCKET}" --region us-east-1
```

Resultado esperado:

```
make_bucket: taller-rag-123456789012
```

## Paso 2 · Sube los documentos (sin la carpeta `extra`)

```bash
aws s3 cp data/ "s3://${BUCKET}/docs/" --recursive --exclude "extra/*"
```

Debes ver 8 líneas `upload:` (4 documentos + 4 archivos de metadatos).

## Paso 3 · Verifica

```bash
aws s3 ls "s3://${BUCKET}/docs/"
```

También puedes verlo en la consola: **S3** → **Buckets** → `taller-rag-<tu-cuenta>` → `docs/`.

## 💡 ¿Qué formatos acepta Bedrock Knowledge Bases?

Entre otros: `.txt`, `.md`, `.html`, `.doc/.docx`, `.csv`, `.xls/.xlsx` y `.pdf`. También puede conectarse a fuentes como sitios web, Confluence, SharePoint o Salesforce.

## ✅ Checkpoint

- [ ] Tengo un bucket llamado `taller-rag-<mi-cuenta>`.
- [ ] Dentro de `docs/` hay 4 archivos `.md` y 4 archivos `.metadata.json`.
- [ ] **No** subí la carpeta `extra/`.

> 📝 Anota el nombre de tu bucket. Lo necesitas en el siguiente módulo.

---

**[← Conceptos](01-conceptos.md)** · **[Siguiente: Crea tu Knowledge Base →](03-crear-knowledge-base.md)**
