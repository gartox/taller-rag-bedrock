# 4 · Pruébala en la consola

⏱️ **15 minutos** · 🛠️ Hands-on

## Objetivo

Hacer preguntas a tu Knowledge Base desde la consola y entender la diferencia entre **solo recuperar** y **recuperar + generar**.

## Paso 1 · Abre el panel de pruebas

En la página de `kb-cacao-labs`, haz clic en **Test Knowledge Base**. Se abre un panel de chat a la derecha.

## Paso 2 · Primero, solo recuperar

1. En **Configurations**, **desactiva** la opción **Generate responses** (*Generate responses for your query*).
2. Pregunta:

   ```
   ¿Cuántos días de vacaciones tengo en mi primer año?
   ```

3. Observa el resultado: **no hay una respuesta redactada**, solo los **chunks** que la búsqueda semántica consideró relevantes, con su documento de origen.

> 🔎 Esto es la **R** de RAG: *Retrieval*. Ningún modelo generativo participó.

## Paso 3 · Ahora, recuperar + generar

1. **Activa** de nuevo **Generate responses**.
2. Haz clic en **Select model** y elige **Amazon** → **Nova 2 Lite** (si no aparece, elige *Nova Lite* o *Nova Pro*).
3. Haz la misma pregunta.

Ahora obtienes una **respuesta en lenguaje natural**. Haz clic en los números de cita (o en **Show source details**) para ver de qué chunk salió cada dato.

## Paso 4 · Prueba estas preguntas

Haz al menos 5 preguntas y anota qué pasa.

### 💬 Preguntas directas
```
¿Cuánto me reembolsan por kilómetro si uso mi auto?
¿Qué hago si me roban la laptop?
¿Cuándo pagan la nómina?
```

### 💬 Preguntas que combinan documentos
```
¿Cuánto dinero al año me da la empresa entre capacitación y apoyo de internet?
```
*(La respuesta correcta combina datos de dos documentos: 12,000 + 800 × 12 = 21,600 MXN.)*

### 💬 Preguntas con otras palabras
```
¿Puedo trabajar desde la playa en Cancún un miércoles?
¿Me pagan las chelas en un viaje de trabajo?
```
*Fíjate cómo la búsqueda semántica entiende "chelas" aunque el documento dice "bebidas alcohólicas".*

### 💬 Preguntas trampa
```
¿Puedo llevar a mi perro a la oficina?
¿Cuál es el salario de un desarrollador senior?
```
*Esa información **no** está en los documentos. Un buen sistema RAG debe decir que no la encontró en lugar de inventar.*

## 🧠 Para reflexionar

1. ¿Qué pasó con la pregunta que combinaba dos documentos? ¿Hizo bien la suma?
2. En la pregunta del perro, ¿el modelo admitió que no sabía o inventó algo?
3. ¿Qué ventaja tiene que cada respuesta traiga **citas**?

> 💡 Las preguntas trampa son la mejor prueba de un sistema RAG. Más adelante vas a **agregar** el documento que responde la pregunta del perro.

## ✅ Checkpoint

- [ ] Vi la diferencia entre solo recuperar y recuperar + generar.
- [ ] Revisé las citas de al menos una respuesta.
- [ ] Probé una pregunta trampa.

---

**[← Crea tu Knowledge Base](03-crear-knowledge-base.md)** · **[Siguiente: Consúltala con Python →](05-consultar-con-python.md)**
