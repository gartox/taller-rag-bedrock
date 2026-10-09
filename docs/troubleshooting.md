# 🛟 Solución de problemas

## "Falta la variable KB_ID"

CloudShell perdió tus variables (pasa si estuvo inactivo o se reinició). Vuelve a ejecutar:

```bash
export KB_ID="TU_ID"
cd ~/taller-rag-bedrock/scripts
```

## `AccessDeniedException` al usar un modelo

- **Espera 2 minutos y reintenta.** La primera vez que usas un modelo, Bedrock activa la suscripción en segundo plano.
- Si usas **tu propia cuenta**, verifica que tenga un **método de pago válido**. AWS Marketplace lo requiere para activar algunos modelos.
- Si usas **Anthropic Claude**, primero llena el formulario de caso de uso (*First Time Use*) en la consola de Bedrock.
- Si sigue fallando, cambia el modelo:
  ```bash
  export MODEL_ID="us.amazon.nova-lite-v1:0"
  ```

## `ValidationException: ... model identifier is invalid` o `on-demand throughput isn't supported`

Estás usando el ID del modelo base en lugar del **perfil de inferencia**. Usa el prefijo `us.`:

```bash
export MODEL_ID="us.amazon.nova-2-lite-v1:0"   # ✅
# no: amazon.nova-2-lite-v1:0                   # ❌ en us-east-1
```

## `ResourceNotFoundException` con la Knowledge Base

- Revisa que el `KB_ID` sea correcto (10 caracteres, sin espacios).
- Revisa que CloudShell y la consola estén en la **misma región** (`us-east-1`).

## El Sync dice "Completed" pero 0 documentos indexados

- Revisa que el **S3 URI** de la fuente de datos apunte a la carpeta `docs/` correcta.
- Revisa que los archivos estén en el bucket: `aws s3 ls s3://taller-rag-<cuenta>/docs/`.

## El Sync marca documentos con error de metadatos

El archivo `.metadata.json` debe llamarse **exactamente** como el documento más `.metadata.json` (por ejemplo, `faq-onboarding.md.metadata.json`) y tener JSON válido.

## No puedo crear la Knowledge Base: "root user"

Bedrock no permite crear Knowledge Bases con el usuario raíz. Crea un usuario de IAM (ver [Configuración con tu cuenta](00-prerrequisitos/cuenta-propia.md)).

## No aparece la opción "Amazon S3 Vectors"

- Confirma que estás en `us-east-1`.
- Busca la opción dentro de **Quick create a new vector store**, en el selector del tipo de base de datos.

## La respuesta no tiene citas

- Si usas un prompt personalizado, asegúrate de incluir `$output_format_instructions$`.
- Si la pregunta no tiene relación con los documentos, es normal que no haya citas.

## La respuesta sale en inglés

Agrega al prompt: `Responde SIEMPRE en español.` (ver `03_chat.py`).
