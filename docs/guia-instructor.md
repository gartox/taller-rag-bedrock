# 👩‍🏫 Guía del instructor

Notas para quien imparte el taller **"Habla con tus documentos"** (2 horas, hands-on).

## Filosofía

**Haz más que hablar.** Máximo 25 minutos de teoría en total. El resto es manos en el teclado. Las slides solo acompañan; el material vive en este repositorio.

## Agenda sugerida (120 min)

| Hora | Bloque | Material | Notas |
|---|---|---|---|
| 0:00 | Bienvenida + setup | Slides 1-4 · Módulo 0 | Proyecta el código del evento desde el minuto 0. |
| 0:10 | ¿Qué es RAG? | Slides 5-12 · Módulo 1 | Haz la demo "sin RAG" en vivo antes de explicar. |
| 0:25 | Datos en S3 | Módulo 2 | Copiar y pegar. |
| 0:35 | Crear Knowledge Base | Slides 13-14 · Módulo 3 | El paso con más dudas: ve tú adelante en pantalla. |
| 0:55 | Probar en consola | Módulo 4 | Pide que compartan la pregunta trampa más divertida. |
| 1:10 | Python | Slides 15-16 · Módulo 5 | Lee el código en voz alta, línea por línea. |
| 1:35 | Retos | Slide 17 · Módulo 6 | Reto 1 para todos; el resto, libre. |
| 1:50 | Limpieza + cierre | Slides 18-20 · Módulos 7-8 | Encuesta, foto grupal y anuncio del siguiente evento. |

## Antes del evento

### Una semana antes

- [ ] Haz el taller completo en una cuenta limpia. La consola de AWS cambia seguido; actualiza capturas y nombres de botones.
- [ ] Confirma que `us.amazon.nova-2-lite-v1:0` funciona en Knowledge Bases. Si no, cambia el valor por defecto en `scripts/config.py`.
- [ ] **Ruta evento:** pide a tu community manager regional un evento de Workshop Studio con cuentas temporales. Pide permisos para Bedrock, Bedrock Knowledge Bases, S3, S3 Vectors, IAM (crear el service role) y CloudShell en `us-east-1`.
- [ ] Publica el repositorio en GitHub y reemplaza `<ORG>` en `docs/00-prerrequisitos/README.md`.

### El día del evento

- [ ] Wi-Fi probado con al menos 30 dispositivos.
- [ ] Código de acceso del evento visible en una slide.
- [ ] Una cuenta de respaldo con la Knowledge Base **ya creada**, por si alguien se atora en el módulo 3. Comparte el `KB_ID` para que pueda seguir con el módulo 5.
- [ ] Mentores: 1 por cada 10 o 15 asistentes.

## Puntos donde se atora la gente

| Módulo | Problema típico | Solución rápida |
|---|---|---|
| 0 | Región equivocada | Pide que todos levanten la mano cuando vean "N. Virginia". |
| 2 | Bucket con nombre repetido | El nombre usa el ID de la cuenta, así que no debería pasar. Si pasa, agrega un sufijo. |
| 3 | Eligen OpenSearch Serverless | Revisa en pantalla que digan **S3 Vectors** antes de hacer clic en Next. |
| 3 | Olvidan el Sync | Es el paso más olvidado. Repítelo dos veces. |
| 5 | Pierden `KB_ID` | Pon el `export` en una slide fija. |
| 5 | Error de modelo | `export MODEL_ID="us.amazon.nova-lite-v1:0"` |

## Demo "sin RAG" (gancho de apertura)

Antes de explicar nada, ejecuta en vivo:

```bash
python3 05_sin_rag.py "¿Cuántos días de vacaciones da Cacao Labs el primer año?"
```

Luego pregunta al público: *"¿Le creerían a esta respuesta?"*. Al final del módulo 5 repite la misma pregunta con `02_rag.py`. Así cierras el círculo.

## Después del evento

- Comparte el enlace del repositorio y la encuesta.
- Recuerda a quienes usaron su propia cuenta que hagan la **limpieza**.
- Registra asistencia y aprendizajes para Builder Center.
