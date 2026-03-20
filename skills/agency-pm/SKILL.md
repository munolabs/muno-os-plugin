---
name: agency-pm
description: Gestion de proyectos para agencias de software. Onboarding de proyectos nuevos, weekly reports, seguimiento de owners, status updates. Trigger en "nuevo proyecto", "weekly report", "status del proyecto", "onboarding cliente", "crear estructura proyecto".
---

# Agency PM - Project Management

Framework de gestion de proyectos para agencias de software. Incluye onboarding, clasificacion por tiers, weekly reports y seguimiento.

Originalmente desarrollado por Muno Labs para gestionar sus proyectos de clientes.
Adaptable a cualquier agencia o equipo de desarrollo.

## Archivos en este Skill

```
agency-pm/
├── SKILL.md
├── config.json              # Tu configuración (crear desde config.example.json)
├── config.example.json      # Template de configuración
├── references/
│   ├── way-of-working.md    # Estructura, tiers, tipos de proyecto
│   ├── owner-checklist.md   # Responsabilidades del owner
│   └── tools-integration.md # Linear, Notion, Meet
└── templates/
    ├── weekly-notes.md      # Template notas semanales
    └── weekly-report.md     # Template reporte al cliente
```

## ⚙️ Setup — Primera Vez

**Al iniciar, verificar si existe `config.json`.**

### Si NO existe `config.json`:

Hacer estas preguntas antes de arrancar:

```
1. "¿Cómo se llama tu agencia?"
2. "¿Cuál es el umbral de revenue para considerar un proyecto Tier 1?
    (ej: +$5K USD/mes, +$3M COP/mes — usá la moneda que manejás)"
3. "¿Quiénes son los socios o directores que hacen de Owner en Tier 1?"
4. "¿Usás Linear para gestionar issues?" (sí/no)
5. "¿Usás Notion para documentación?" (sí/no)
```

Crear `config.json` con las respuestas y confirmar:
*"Guardé tu configuración. Podés editarla en config.json cuando cambie algo."*

### Si SÍ existe `config.json`:

Leerlo y usar `tier1_revenue_threshold` para clasificar proyectos en vez de valores hardcodeados.

## Flujo: Onboarding Nuevo Proyecto

### 1. Clasificar el Proyecto
Preguntar o determinar:

| Pregunta | Opciones |
|----------|----------|
| ¿Quién es el Owner? | Nombre (socio o delegado) |
| ¿Es Tier 1 o Tier 2? | Ver `references/way-of-working.md` |
| ¿Tipo de proyecto? | Project Based / Service Based / Product Based |

### 2. Crear Estructura de Carpetas

**Para Project Based (entrega finita):**
```
[cliente]/activo/[proyecto]/
├── README.md           # Del template
└── meetings.md         # Opcional
```

**Para Service/Product Based (ongoing):**
```
[cliente]/activo/[proyecto]/
├── README.md
├── Soporte.md          # OBLIGATORIO
├── meetings.md
└── weekly-notes.md
```

### 3. Configurar Herramientas
- [ ] Crear proyecto en Linear (team correcto)
- [ ] Crear espacio en Notion
- [ ] Crear canal Slack si aplica
- [ ] Agregar al directorio de clientes

## Flujo: Weekly Report

### 1. Recolectar Información
Leer de estas fuentes:
- `weekly-notes.md` del proyecto
- Linear: tickets completados/en progreso
- Notion: notas de reuniones recientes

### 2. Generar Reporte
Usar `templates/weekly-report.md`:
- Resumen ejecutivo (3 bullets)
- Completado esta semana
- En progreso
- Próximos pasos
- Blockers (si hay)

### 3. Entregar
- Formato: Markdown o adaptado a Notion/email
- Frecuencia: Semanal (antes del weekly con cliente)

## Flujo: Status Check

Verificar para cada proyecto activo:
- [ ] ¿Tiene owner definido?
- [ ] ¿Weekly interno esta semana?
- [ ] ¿Weekly con cliente programado?
- [ ] ¿Linear actualizado?
- [ ] ¿Documentación al día?

Ver `references/owner-checklist.md` para lista completa.

## Gotchas

1. **Tier no es fijo**: Un proyecto puede cambiar de Tier 2 a Tier 1 si crece en importancia estratégica.

2. **Project Based NO necesita Soporte.md**: El proyecto termina, no hay soporte ongoing.

3. **Owner ≠ quien hace el trabajo**: El owner coordina y es punto de contacto, puede delegar ejecución.

4. **Weekly report ≠ Weekly notes**:
   - `weekly-notes.md` = interno, input crudo
   - `weekly-report.md` = para cliente, curado

5. **Linear es la fuente de verdad** para tareas. No duplicar tracking en otros lugares.

6. **Notion para docs, no para tareas**: Documentación y notas van a Notion. Tareas van a Linear.

## Clasificación de Tiers

### Tier 1 - Alta Prioridad
- Owner: Socio / Director
- Revenue alto O estratégicamente importante
- Reuniones semanales obligatorias

### Tier 2 - Delegable
- Owner: Puede ser miembro del equipo
- Revenue menor, más operativo
- Supervisión quincenal de socios

## Tipos de Proyecto

| Tipo | Duración | Facturación | Ejemplo |
|------|----------|-------------|---------|
| Project Based | Finita | Milestones | App nueva, migración |
| Service Based | Ongoing | Retainer mensual | Fractional CTO |
| Product Based | Ongoing | Por consumo/mes | SaaS, plataforma |

## Integraciones

Ver `references/tools-integration.md` para:
- Crear tickets con `/linear` en Slack
- Sincronizar Notion ↔ Linear
- Generar transcripts de Meet
