---
name: quick-start
description: Bienvenida al plugin y setup guiado. Explica el framework de capas, detecta el nivel del usuario y recomienda por dónde empezar. Trigger en "quick start", "por dónde empiezo", "setup", "configurar plugin", "empezar", "ayuda con el plugin".
---

# Quick Start — Muno OS Plugin

Bienvenida al plugin. Este skill te explica cómo funciona todo, detecta qué tenés disponible en tu entorno y te dice exactamente por dónde empezar.

---

## El Framework: 4 Capas para Pensar tu Asistente

> Este framework es de **Muno Labs** — una forma de entender cómo se construye un asistente de IA realmente útil.

```
┌─────────────────────────────────────────────────────┐
│  INTERFAZ          dónde interactúas                │
│  Chat · Cowork · Code                               │
├─────────────────────────────────────────────────────┤
│  INTEGRACIONES     conexión con el mundo externo    │
│  Conectores · MCPs · APIs · CLI                     │
├─────────────────────────────────────────────────────┤
│  PERSONALIZACIÓN   cómo querés que Claude trabaje   │  ← Este plugin vive acá
│  Skills · Plugins · Memory & Context                │
├─────────────────────────────────────────────────────┤
│  EJECUCIÓN         los que hacen el trabajo solos   │
│  Modelo · Agentes · Sub-agentes                     │
└─────────────────────────────────────────────────────┘
```

**Este plugin actúa en la capa de Personalización** — le enseña a Claude cómo trabajar con vos, con tu contexto, con tus herramientas. Algunos skills también tocan Integraciones (cuando conectan con Linear, Gmail, APIs externas).

La idea es simple:
- **Más personalización** → Claude entiende mejor tu contexto y trabaja como vos
- **Más integraciones** → Claude tiene acceso a más de tu mundo real
- No necesitás las 4 capas para empezar. Cada nivel que agregás suma — ninguno es obligatorio

---

## Diagnóstico Rápido

Antes de recomendar por dónde empezar, hacer estas 3 preguntas:

```
1. "¿Qué interfaz usás principalmente?"
   a) Claude.ai (web) o Claude Cowork (app)
   b) Claude Code (terminal)
   c) Ambas

2. "¿Qué tenés disponible en tu entorno?" (seleccionar todo lo que aplique)
   a) Terminal / línea de comandos con Python instalado
   b) Linear conectado (MCP)
   c) Gmail conectado (MCP)
   d) Google Calendar (MCP)
   e) Solo la interfaz web, sin terminales ni MCPs

3. "¿Cuál es tu objetivo principal con este plugin?"
   a) Crear contenido para redes (LinkedIn, Twitter)
   b) Organizar mi día y mis tareas
   c) Gestionar proyectos de clientes
   d) Automatizar trabajo repetitivo
   e) Todo lo anterior
```

---

## Caminos según el Diagnóstico

### 🟢 Solo interfaz web (sin terminal ni MCPs)

Dos skills funcionan perfectamente para vos:

| Skill | Qué hace | Cómo empezar |
|-------|----------|--------------|
| **daily-writing** | Drafts de LinkedIn y Twitter con voz auténtica | `"daily writing"` |
| **document-style** | Da estilo corporativo a propuestas y contratos | `"document style"` |

> 💡 **Tip de personalización**: Con solo un `CLAUDE.md` en tu proyecto podés darle a Claude memoria de quién sos, cómo trabajás y qué preferís. No requiere nada técnico — es un archivo de texto.

---

### 🔵 Tenés terminal + Python

Sumás estos skills:

| Skill | Qué hace | Requisito |
|-------|----------|-----------|
| **indicadores** | TRM, stocks, indicadores financieros en tiempo real | Python 3 |
| **conciliacion** | Concilia extractos bancarios con facturas | Python 3 + CSV del banco |
| **daily-brief** | Brief matutino visual (HTML) con tus datos del día | Python 3 |
| **document-ocr** | Extrae texto de PDFs e imágenes | Python 3 + AWS (opcional) |

> 💡 **Tip de integración**: Con Python disponible ya podés conectar Claude a APIs externas, procesar archivos y generar reportes. Es el primer paso hacia Integraciones reales.

---

### 🟣 Tenés MCPs configurados (Linear, Gmail, Calendar)

El plugin completo está disponible para vos:

| Skill | MCP requerido |
|-------|--------------|
| **agency-pm** | Linear |
| **daily-brief** (completo) | Linear + Gmail + Calendar |
| **pencil-design** | Pencil MCP |

> 💡 **Tip de ejecución**: Con MCPs conectados, Claude puede actuar en tu mundo — crear issues, leer emails, consultar el calendario. Estás un paso de tener agentes que trabajan solos.

---

## Setup Recomendado por Objetivo

### "Quiero crear mejor contenido"
→ Empezar con **daily-writing** + configurar tu `config.json` con tus fuentes y referencias

### "Quiero organizar mejor mi día"
→ Empezar con **daily-brief** en modo básico (solo tareas + quote) y agregar capas según necesitás

### "Gestiono proyectos de clientes"
→ **agency-pm** + configurar tus tiers y herramientas en `config.json`

### "Quiero automatizar lo repetitivo"
→ Primero configurar **daily-brief** para entender el patrón JSON → HTML, después explorar cómo adaptar ese mismo patrón a otros flujos

---

## El Primer Paso Siempre es el Mismo

Sin importar tu nivel, lo primero es dar contexto a Claude sobre vos:

```markdown
# Quién soy
- Nombre, rol, industria
- Herramientas que uso
- Cómo prefiero trabajar

# Mi contexto
- Proyectos activos
- Prioridades actuales
```

Esto va en un archivo `CLAUDE.md` en tu proyecto. Claude lo leerá automáticamente cada vez que arranques una sesión. Es la base de la **capa de Personalización** — y el retorno más alto por el menor esfuerzo.

Si querés, decime `"ayudame a crear mi CLAUDE.md"` y te guío.

---

## Skills Disponibles

| Skill | Nivel | Qué resuelve |
|-------|-------|-------------|
| `daily-writing` | ⚡ Básico | Contenido LinkedIn/Twitter sin AI slop |
| `document-style` | ⚡ Básico | Documentos con estilo corporativo |
| `daily-brief` | 🔧 Intermedio | Brief matutino visual personalizado |
| `indicadores` | 🔧 Intermedio | TRM y mercados en tiempo real |
| `conciliacion` | 🔧 Intermedio | Conciliación bancaria automática |
| `agency-pm` | 🔌 Avanzado | PM completo para agencias de software |
| `document-ocr` | 🔌 Avanzado | OCR de PDFs con AWS Textract |
| `pencil-design` | 🔌 Avanzado | Diseño de interfaces con IA |

⚡ Sin dependencias · 🔧 Requiere Python/terminal · 🔌 Requiere MCPs

---

*Framework de capas por [Muno Labs](https://munolabs.com) — agencia de software e IA.*
