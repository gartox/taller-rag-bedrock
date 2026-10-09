# 🏠 Configuración con tu propia cuenta

Usa esta ruta si haces el taller por tu cuenta o si no tienes código de evento.

## 1. Necesitas una cuenta de AWS

Si no tienes una, créala en **https://aws.amazon.com/** → *Create an AWS Account*. Te pedirá una tarjeta, pero este taller cuesta **centavos de dólar** si sigues la limpieza al final.

## 2. No uses el usuario raíz (root)

AWS no permite crear Knowledge Bases con el usuario raíz. Entra con un **usuario de IAM** o con **IAM Identity Center** que tenga permisos de administrador.

¿Solo tienes el usuario raíz? Crea un usuario administrador así:

1. Ve a **IAM** → **Users** → **Create user**.
2. Nombre: `taller-rag`. Marca **Provide user access to the AWS Management Console**.
3. En permisos, elige **Attach policies directly** → `AdministratorAccess`.
4. Termina el asistente, guarda la URL de inicio de sesión y entra con ese usuario.

> 🔐 Activa MFA en tu usuario raíz y en el nuevo usuario. Es la medida de seguridad más importante en AWS.

## 3. Configura una alerta de presupuesto (recomendado)

Así recibes un correo si algo empieza a cobrar más de lo esperado:

1. Ve a **Billing and Cost Management** → **Budgets** → **Create budget**.
2. Elige la plantilla **Zero spend budget** (o *Monthly cost budget* de 5 USD).
3. Escribe tu correo y crea el presupuesto.

## 4. ¿Cuánto cuesta este taller?

| Recurso | Costo aproximado |
|---|---|
| Embeddings con Titan V2 (≈ 10,000 tokens) | < 0.01 USD |
| Amazon S3 Vectors (unos cientos de vectores) | < 0.01 USD |
| Respuestas con Nova 2 Lite (≈ 50 preguntas) | < 0.10 USD |
| Amazon S3 (5 archivos pequeños) | < 0.01 USD |
| **Total estimado** | **< 1 USD** |

> ⚠️ Usamos **S3 Vectors** como base de datos vectorial porque se cobra por uso. Si eliges **OpenSearch Serverless** en lugar de S3 Vectors, se cobra **por hora** aunque no lo uses y puede costar **cientos de dólares al mes**. Sigue la guía tal cual.

Los precios cambian. Revisa la [página de precios de Amazon Bedrock](https://aws.amazon.com/bedrock/pricing/) si tienes dudas.

## 5. Anthropic (opcional)

Este taller usa **Amazon Nova**, que no requiere ningún formulario. Si más adelante quieres usar modelos de **Anthropic Claude**, la primera vez Bedrock te pedirá llenar un breve formulario de caso de uso (*First Time Use*).

---

**[← Volver a Prerrequisitos](README.md)** para la verificación final.
