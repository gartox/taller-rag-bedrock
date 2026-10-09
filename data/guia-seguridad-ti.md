# Guía de Seguridad de TI — Cacao Labs

*Versión 1.4 — Documento ficticio para fines educativos.*

## 1. Equipo de cómputo

Cada colaborador recibe una laptop de la empresa. Es responsabilidad de cada persona:

- Mantener el sistema operativo actualizado (las actualizaciones se aplican automáticamente los miércoles a las 13:00).
- No instalar software sin licencia.
- Usar el disco cifrado que viene configurado de fábrica. **No se debe desactivar el cifrado**.

## 2. Si pierdes tu laptop o te la roban

Actúa rápido. Sigue estos pasos **en la primera hora**:

1. Repórtalo al canal **#seguridad** en el chat interno o al correo seguridad@cacaolabs.example.
2. Llama a la línea de guardia de TI: **993 000 0000** (número ficticio), disponible 24/7.
3. TI bloqueará el equipo de forma remota y cerrará todas tus sesiones activas.
4. Si fue un robo, levanta una denuncia ante el Ministerio Público y envía una copia a TI en un plazo de 72 horas.

La primera pérdida no tiene costo para el colaborador. A partir de la segunda pérdida en un periodo de 24 meses, se descuenta el 30 % del valor del equipo.

## 3. Contraseñas y accesos

- Todas las cuentas usan inicio de sesión único (SSO) y **autenticación multifactor (MFA)** obligatoria.
- Usa el gestor de contraseñas que proporciona la empresa. Está prohibido guardar contraseñas en archivos de texto u hojas de cálculo.
- **Nunca** compartas llaves de acceso de AWS en el chat, el correo ni en repositorios de código. Si una llave se filtra, avisa de inmediato a #seguridad para rotarla.

## 4. Uso de IA generativa

Se permite usar asistentes de IA para el trabajo diario con estas reglas:

- Solo se pueden usar las herramientas aprobadas en el catálogo interno de TI.
- No se deben pegar datos personales de clientes ni código propiedad de clientes en herramientas de IA públicas.
- Los modelos que se usan con datos de clientes deben ejecutarse dentro de la cuenta de AWS del proyecto (por ejemplo, con Amazon Bedrock).

## 5. Wi-Fi y redes

- En la oficina usa la red **CacaoLabs-Staff**. La red **CacaoLabs-Visitas** es solo para invitados.
- En redes públicas (cafeterías, aeropuertos) se debe activar la VPN de la empresa antes de abrir cualquier sistema interno.
