# Tools Integration — Agency PM

Guía de integraciones entre herramientas de PM: Linear, Notion, y reuniones.

> ⚙️ **Setup requerido**: Este skill asume que tenés Linear y/o Notion configurados.
> Si no los tenés, ver la sección **"Setup desde cero"** al final de este archivo.

---

## Linear

### Crear tickets desde Claude

Con el MCP de Linear conectado, Claude puede crear issues directamente:

```
"Crear issue en Linear: Fix timeout en endpoint de pagos — proyecto [nombre], asignar a [persona], prioridad Alta"
```

Claude usará el MCP para:
1. Buscar el team y proyecto correcto
2. Crear el issue con título, descripción, asignado y prioridad
3. Confirmar el link del issue creado

### Consultar estado de issues

```
"¿Qué issues están en progreso para [cliente]?"
"Listar todos los blockers del sprint actual"
"¿Qué completó el equipo esta semana?"
```

### Mover issues de estado

```
"Mover MUN-234 a Done"
"Pasar todos los issues de revisión a In Progress"
```

### Convenciones recomendadas

| Campo | Convención |
|-------|-----------|
| Título | `[Verbo] [objeto] — [contexto]` Ej: `Fix login timeout — producción` |
| Labels | `bug`, `feature`, `support`, `infra`, `docs` |
| Prioridad | Urgent = blocker prod, High = sprint actual, Medium = backlog próximo |
| Ciclos | Sprint de 2 semanas, cierre los viernes |

---

## Notion

### Sincronización Notion ↔ Linear

Notion se usa para **documentación** (specs, decisiones, contratos).
Linear se usa para **tareas** (issues, sprints, tracking).

No duplicar — la regla es:
- **¿Hay que hacerlo?** → Linear
- **¿Hay que entenderlo o recordarlo?** → Notion

### Estructura recomendada en Notion por cliente

```
[Cliente]/
├── README            # Contexto, contactos, accesos
├── Contratos/        # PDFs firmados
├── Specs/            # Documentos técnicos y funcionales
└── Decisiones/       # Log de decisiones importantes con fecha y razón
```

### Crear documentos desde Claude

Con el MCP de Notion conectado:

```
"Crear página en Notion para el proyecto X con la spec de la feature Y"
"Buscar el contrato de [cliente] en Notion"
"Actualizar el README de [cliente] con los nuevos accesos"
```

---

## Reuniones (Google Meet / Zoom)

### Transcripts de Meet

Para generar transcripts útiles de reuniones:

**Opción A — Google Meet (automático):**
1. Activar "Transcripción" antes de iniciar
2. Al terminar, el transcript llega a Drive automáticamente
3. Compartir el link a Claude: `"Resumí esta reunión: [link]"`

**Opción B — Descarga manual:**
1. Exportar el transcript como `.txt` o `.vtt`
2. Pasarlo a Claude: `"Procesá este transcript y extraé action items"`

### Qué pedirle a Claude con un transcript

```
"Extraé los action items con responsable y fecha"
"Resumí los puntos de decisión"
"Creá issues en Linear por cada acción pendiente"
"Generá el weekly notes a partir de esta reunión"
```

---

## Setup desde cero

> ⚠️ Si acabas de instalar el plugin y no tenés estas herramientas configuradas,
> Claude te guiará. Simplemente decile qué herramientas usás y empezamos desde ahí.

### Si usás Linear (recomendado)

1. Instalar el MCP de Linear:
   ```bash
   # En tu claude_desktop_config.json o settings
   {
     "mcpServers": {
       "linear": {
         "command": "npx",
         "args": ["-y", "@linear/mcp-server"],
         "env": { "LINEAR_API_KEY": "tu-api-key" }
       }
     }
   }
   ```
2. Obtener API key: Linear → Settings → API → Personal API Keys
3. Verificar: `"listar mis issues de Linear"`

### Si usás Notion

1. Instalar el MCP de Notion (ver documentación oficial de Anthropic)
2. Crear integración en notion.so/my-integrations
3. Conectar las páginas que querés que Claude pueda ver

### Si usás otro PM (Jira, Asana, Trello, etc.)

Claude puede trabajar igual sin MCP — simplemente vas a tener que copiar/pegar la info en vez de que la consiga automáticamente. Las plantillas y el flujo del skill funcionan igual.

Decile a Claude: `"No tengo Linear, uso [herramienta]. Adaptá el flujo."`

---

## Sin ninguna herramienta de PM

El skill funciona igual usando solo archivos de texto:

```
proyectos/
└── [cliente]/
    ├── README.md
    ├── backlog.md      # Issues en texto plano
    └── weekly.md      # Notas semanales
```

Claude puede crear y mantener estos archivos sin MCPs.
