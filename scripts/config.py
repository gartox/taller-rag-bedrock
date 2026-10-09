"""
Configuración compartida para todos los scripts del taller.

Lee los valores de variables de entorno para que no tengas que editar código:

    export KB_ID="ABCDEFGHIJ"                        # ID de tu Knowledge Base (obligatorio)
    export AWS_REGION="us-east-1"                    # Región donde creaste la KB (opcional)
    export MODEL_ID="us.amazon.nova-2-lite-v1:0"     # Modelo generador (opcional)
"""

import os
import sys

import boto3

REGION = os.environ.get("AWS_REGION", "us-east-1")
KB_ID = os.environ.get("KB_ID", "").strip()

# Amazon Nova 2 Lite a través de un perfil de inferencia (cross-region) de EE. UU.
# Si este modelo no está disponible en tu cuenta, prueba con:
#   us.amazon.nova-lite-v1:0   o   us.amazon.nova-pro-v1:0
MODEL_ID = os.environ.get("MODEL_ID", "us.amazon.nova-2-lite-v1:0")


def require_kb_id() -> str:
    """Detiene el script con un mensaje claro si falta KB_ID."""
    if not KB_ID:
        print("❌ Falta la variable KB_ID.")
        print('   Ejecuta primero:  export KB_ID="<ID de tu Knowledge Base>"')
        print("   Encuentras el ID en la consola de Bedrock > Knowledge Bases > tu KB.")
        sys.exit(1)
    return KB_ID


def model_arn(model_id: str = MODEL_ID) -> str:
    """
    Convierte un model ID en el ARN que pide RetrieveAndGenerate.

    - Los perfiles de inferencia (us., eu., apac., global.) son recursos de TU
      cuenta, así que su ARN lleva el número de cuenta.
    - Los modelos base (foundation models) no llevan número de cuenta.
    """
    if model_id.startswith("arn:"):
        return model_id

    prefixes = ("us.", "eu.", "apac.", "jp.", "global.")
    if model_id.startswith(prefixes):
        account = boto3.client("sts", region_name=REGION).get_caller_identity()["Account"]
        return f"arn:aws:bedrock:{REGION}:{account}:inference-profile/{model_id}"

    return f"arn:aws:bedrock:{REGION}::foundation-model/{model_id}"


def kb_runtime():
    """Cliente de 'bedrock-agent-runtime': el que expone Retrieve y RetrieveAndGenerate."""
    return boto3.client("bedrock-agent-runtime", region_name=REGION)


def source_name(reference: dict) -> str:
    """Saca un nombre corto y legible del documento fuente de una referencia."""
    uri = reference.get("location", {}).get("s3Location", {}).get("uri", "")
    return uri.rsplit("/", 1)[-1] if uri else "(fuente desconocida)"
