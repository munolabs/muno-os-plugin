# Style Guide — Daily Writing

Guía de voz y estilo para contenido en LinkedIn y Twitter.

---

## Principios de Voz

### Qué somos
- **Específicos**: Fechas, montos, nombres reales > generalidades
- **Directos**: Una idea por post. Sin rodeos
- **Curiosos**: Compartimos porque algo nos sorprendió, no para "agregar valor"
- **Vulnerables cuando aplica**: Los errores son más interesantes que los éxitos

### Qué NO somos
- Inspiracionales genéricos ("¡El fracaso es aprendizaje!")
- Autoridad sin evidencia ("Como CEO, sé que...")
- Hype sin sustancia ("Esto cambiará todo")
- Listicles perezosos ("5 cosas que aprendí")

---

## Patrones de Referencia

> 📌 **Tus referencias están en `config.json` → campo `referencias_estilo`.**
> Las de abajo son ejemplos para entender los arquetipos — no son las únicas ni las mejores para todos.
> Si no tenés config.json todavía, el skill te guiará a crearlo.

### Arquetipo: Data-driven (ej: Tomás Tunguz, Ben Thompson)
- Empieza con un dato sorprendente o contraintuitivo
- Explica la implicación para el negocio
- Cierra con observación hacia adelante ("what I'm watching")

**Estructura:**
```
[Dato o número concreto]
[Por qué es contraintuitivo o relevante]
[Implicación práctica]
[Lo que estoy observando ahora]
```

### Arquetipo: Narrativo / craft (ej: Every, Packy McCormick)
- Experiencia personal específica como entrada
- Pregunta que esa experiencia genera
- Insight que emerge, no conclusión fácil
- Cierra abierto, no con moraleja

**Estructura:**
```
[Situación concreta — cuándo, qué pasó]
[La pregunta que eso levantó]
[Lo que descubrí intentando responderla]
[Pregunta genuina al final]
```

### Cómo usar tus propias referencias

Si en `config.json` tenés algo como:
```json
"referencias_estilo": ["Ana Arrieta — directa, sin adornos, una idea por post"]
```

Claude intentará identificar los patrones estructurales de ese estilo y aplicarlos.
Cuanto más descriptivo seas en config.json, mejor calibrado queda el output.

---

## Formato por Plataforma

### LinkedIn (Español)
- **Largo**: 800–1500 caracteres
- **Líneas cortas**: Máximo 1–2 oraciones por párrafo
- **Espaciado**: Línea en blanco entre párrafos
- **Hook**: Primera línea sola, sin contexto, que deje con ganas de ver más
- **Sin**: Bullets de 6 puntos, "thread de valor", emojis decorativos
- **Sí**: 1–2 emojis funcionales si añaden claridad

### Twitter / X (Inglés)
- **Largo**: ≤280 chars para tweet simple, o thread de 3–7 tweets
- **Hook**: Tweet 1 = la idea completa en miniatura
- **Threads**: Cada tweet autónomo, no depende del anterior para tener sentido
- **Tono**: Más directo y crudo que LinkedIn

---

## Hooks que Funcionan

| Tipo | Ejemplo |
|------|---------|
| Número sorprendente | "Redujimos el tiempo de deploy de 45 min a 3 min." |
| Contradicción | "Contratamos a alguien más lento. Entregamos más rápido." |
| Situación incómoda | "Un cliente me canceló el contrato. Tenía razón." |
| Pregunta directa | "¿Cuándo fue la última vez que cerraste un deal sin una propuesta?" |
| Observación específica | "Esta semana vi el mismo error en 4 equipos distintos." |

## Hooks que NO Funcionan

| Tipo | Ejemplo |
|------|---------|
| Cliché motivacional | "El éxito llega cuando menos lo esperas" |
| Vago y grandilocuente | "La IA está transformando todo lo que conocemos" |
| Anuncio sin contexto | "Hoy lanzamos nuestra nueva herramienta" |
| Pregunta retórica vacía | "¿Sabías que el 90% de los startups fracasan?" |

---

## Personalización

La personalización de voz, fuentes y referencias se hace en **`config.json`** (un nivel arriba de esta carpeta), no editando este archivo.

Este archivo contiene los principios universales del skill. `config.json` contiene lo tuyo: tu industria, tu audiencia, tus referentes, tus fuentes.

Si no tenés `config.json` todavía, decile a Claude `"daily writing"` y te guiará a crearlo paso a paso.
