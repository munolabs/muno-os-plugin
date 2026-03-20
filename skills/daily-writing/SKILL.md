---
name: daily-writing
description: Genera contenido para LinkedIn (español) y Twitter (inglés) evitando AI slop. Usa experiencias reales, datos concretos, fuentes y estilo personalizados. Trigger en "daily writing", "contenido linkedin", "draft twitter", "content creation", "generar post".
---

# Daily Writing

Genera drafts de contenido para redes sociales con estilo auténtico, evitando AI slop.

## Archivos en este Skill

```
daily-writing/
├── SKILL.md
├── config.json             # Tu configuración personal (crear desde config.example.json)
├── config.example.json     # Template de configuración
└── references/
    ├── style-guide.md      # Guía de estilo (patrones, formatos, hooks)
    ├── anti-slop.md        # Palabras y patrones prohibidos
    └── content-types.md    # Tipos de contenido y estructuras
```

## ⚙️ Setup — Primera Vez

**Antes de empezar, verificar si existe `config.json`.**

### Si NO existe `config.json`:

Guiar al usuario a crearlo con estas preguntas (de a una, conversacional):

```
1. "¿Cuál es tu industria y rol? (ej: CEO de una agencia de software)"
2. "¿A quién le escribís en LinkedIn? (ej: founders latinoamericanos, CTOs, etc.)"
3. "¿Qué newsletters o fuentes leés regularmente para mantenerte al día?"
4. "¿Hay algún escritor o creador de contenido cuyo estilo te gusta? ¿Qué tiene de especial?"
5. "¿Hay temas que preferís evitar en tus redes?"
```

Con las respuestas, crear `config.json` basado en `config.example.json` y confirmar:
*"Guardé tu configuración en config.json. Podés editarla cuando quieras para ajustar tus fuentes o estilo."*

### Si SÍ existe `config.json`:

Leerlo al inicio y usarlo para:
- Calibrar el tono y voz según `referencias_estilo`
- Priorizar las `fuentes` del usuario al buscar trending
- Respetar `temas_off_limits`
- Adaptar la audiencia según `audiencia.linkedin` y `audiencia.twitter`

## Arquitectura

```
┌──────────────┐
│   USUARIO    │
└──────┬───────┘
       │ "daily writing"
       ▼
┌──────────────┐
│  SUPERVISOR  │ ← Lee style-guide.md, anti-slop.md
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  GENERACIÓN  │ ← Cruza fuentes + trending + experiencia
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   EDITOR     │ ← Valida contra checklist anti-slop
└──────┬───────┘
       │
       ▼
   Draft curado
```

## Flujo de Trabajo

### 1. Recolectar Fuentes

Buscar en orden:
1. **Journal reciente**: Qué se hizo esta semana, learnings
2. **Proyectos activos**: Casos, problemas resueltos, insights
3. **Inbox de contenido**: Ideas capturadas pendientes
4. **Trending**: HN, Twitter, lanzamientos relevantes

> **Si no encontrás journal ni archivos de proyectos:**
> No fallar — preguntar directamente al usuario:
> *"No encontré tu journal ni proyectos activos. Contame brevemente:
> ¿qué hiciste esta semana que valga la pena compartir? Puede ser
> una decisión, un problema que resolviste, algo que te sorprendió,
> o una observación sobre tu industria."*
>
> Con esa respuesta se genera el contenido igual.
> Si el usuario quiere tener journal, ofrecerle crearlo:
> *"¿Querés que te ayude a crear un journal.md para capturar esto
> de ahora en más?"*

### 2. Cruzar Trending + Experiencia

**La regla de oro:** El contenido NO es "contar lo que hiciste". Es usar tu experiencia para iluminar algo que importa a la audiencia.

```
❌ "Ayer mandé una propuesta por $5.9M"
✅ "Un cliente me pidió cotizar. Le di un número fijo. Su respuesta cambió cómo pienso sobre pricing."
```

### 3. Generar Draft

Seguir patrones de `references/content-types.md`:

| Tipo | Hook | Cierre |
|------|------|--------|
| Dato → Implicación | Número sorprendente | What I'm watching |
| Anécdota → Insight | Situación concreta | Pregunta genuina |
| Vibe Check | Announcement | Your move |
| Contrarian take | Lo que "todos" creen | Acknowledge otro lado |

### 4. Validar (Editor)

Checklist obligatorio:

```
[ ] Hook específico (dato, anécdota, pregunta)
[ ] Cero palabras/frases prohibidas (ver anti-slop.md)
[ ] Al menos 1 número o ejemplo concreto
[ ] Cierre con "what I'm watching", pregunta, o insight
[ ] LinkedIn en español, Twitter en inglés
[ ] Conecta con experiencia real
[ ] Suena auténtico, no como ChatGPT
```

**Si NO pasa:** Reescribir o descartar. NO entregar slop.

## Gotchas

1. **El primer draft casi nunca sirve**: Siempre pasar por editor. No entregar output crudo.

2. **Datos > Opiniones**: "92% de developers" es mejor que "muchos developers".

3. **Trending sin conexión = vacío**: No postear sobre algo trending si no hay experiencia real que conectar.

4. **Slop es contagioso**: Una frase genérica arruina todo el post. Ser implacable.

5. **LinkedIn ≠ Twitter**: Diferentes idiomas, diferentes estructuras, diferentes audiencias.

## Plataformas

| Plataforma | Idioma | Largo | Formato |
|------------|--------|-------|---------|
| **LinkedIn** | Español | 800-1500 chars | Líneas cortas, espaciado |
| **Twitter/X** | Inglés | 280 chars o thread | Ultra conciso |

## Anti-Slop (Resumen)

### Palabras PROHIBIDAS

```
❌ "In today's fast-paced world..."
❌ "It's important to note..."
❌ "Delve into" / "Dive deep"
❌ "Game-changer" / "Revolutionary"
❌ "Leveraging" / "Harnessing"
❌ "At the end of the day"
❌ "I hope this helps"
❌ "Quiero compartir..."
❌ "Es importante destacar..."
```

### Correcciones

```
❌ "En el mundo actual de la IA..."
✅ "La semana pasada implementamos..."

❌ "Esta herramienta revolucionaria..."
✅ "Con esto redujimos el tiempo de X a Y."
```

## Output

Guardar drafts aprobados en:
- `drafts/linkedin/YYYY-MM-DD.md`
- `drafts/twitter/YYYY-MM-DD.md`

## Parámetros

| Param | Valores | Default |
|-------|---------|---------|
| platform | `linkedin`, `twitter`, `both` | `both` |
| tone | `analytical`, `conversational` | `analytical` |
| source | `journal`, `inbox`, `trending` | todas |
