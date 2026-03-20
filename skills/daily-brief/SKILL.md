---
name: daily-brief
description: Genera un brief matutino personalizado en HTML. Primera vez configura preferencias del usuario. Despues ejecuta automaticamente. Trigger en "daily brief", "brief del dia", "morning brief", "mi brief", "empezar el dia".
---

# Daily Brief

Genera un brief matutino visual (HTML) personalizado para el usuario. El brief consolida informacion del dia en una sola pantalla: fecha, tareas, indicadores, quote, y cualquier fuente de datos que el usuario configure.

## Filosofia

El valor no es solo "leer archivos". Es:
1. **Consolidacion visual** -- todo en una pantalla bonita, no 5 archivos separados
2. **Datos en vivo** -- quote, indicadores, issues, emails (segun configuracion)
3. **El ritual** -- abrir el navegador con tu brief es un momento de "empiezo el dia"
4. **Progressive enhancement** -- empieza simple, crece conforme el usuario conecta fuentes

## Archivos

```
daily-brief/
  SKILL.md              # Este archivo
  template.html         # Design system y template HTML
  generate.sh           # JSON -> HTML generator
  config.example.json   # Ejemplo de configuracion (copiar a config.json)
  references/
    components.md       # Catalogo de componentes HTML disponibles
```

## Flujo Completo

### Primera ejecucion (Setup)

Si NO existe `config.json` en este directorio, entrar en modo setup conversacional:

```
1. Preguntar nombre del usuario -> greeting personalizado
2. Preguntar timezone (ej: America/Bogota, America/Mexico_City, Europe/Madrid)
3. Preguntar idioma preferido (es/en) -- default: es
4. Mostrar menu de secciones disponibles y preguntar cuales quiere:

   SECCIONES DISPONIBLES:
   =====================
   [Sin dependencias - funcionan siempre]
   - greeting     : Saludo + fecha/hora (siempre activo)
   - quote        : Quote inspiracional del dia (zenquotes.io)
   - tasks        : Tareas pendientes desde un archivo .md
   - journal      : Resumen de actividad reciente desde un archivo .md

   [Requieren Python]
   - finance      : Indicadores financieros (TRM, stocks)

   [Requieren MCP]
   - projects     : Resumen de proyectos activos (Linear MCP)
   - email        : Emails prioritarios (Gmail MCP)
   - calendar     : Reuniones del dia (Google Calendar MCP)

   [Custom]
   - custom       : Seccion libre con prompt personalizado

   Ejemplos de secciones custom:
   - "Top 5 de Hacker News" (usa WebFetch para scrapear)
   - "Clima en Medellin" (usa WebFetch a wttr.in o similar)
   - "Precio de BTC y ETH" (usa API publica de CoinGecko)

5. Para cada seccion habilitada, preguntar configuracion especifica:
   - tasks: "Donde guardas tus tareas?" -> path al archivo .md
   - journal: "Donde guardas tu journal/diario?" -> path al archivo .md
   - finance: "Que indicadores?" -> trm, stocks, etc.
   - custom: "Que quieres ver?" -> prompt libre

6. Preguntar si quiere personalizar colores (opcional):
   - Color primario (hex) -- default: #8DEDCF (teal)
   - Color secundario (hex) -- default: #4D9EFF (blue)
   - O decir "usa los defaults"

7. Preguntar donde guardar los reportes HTML:
   - Default: daily-reports/ (relativo al workspace)
```

Guardar resultado en `config.json`:

```json
{
  "name": "Maria",
  "timezone": "America/Mexico_City",
  "locale": "es",
  "brand": {
    "primary": "#8DEDCF",
    "secondary": "#4D9EFF",
    "logo": null
  },
  "sections": {
    "greeting": { "enabled": true },
    "quote": { "enabled": true, "source": "zenquotes" },
    "tasks": { "enabled": true, "path": "brain/to-do.md" },
    "journal": { "enabled": false },
    "finance": { "enabled": true, "indicators": ["trm"] },
    "projects": { "enabled": false },
    "email": { "enabled": false },
    "calendar": { "enabled": false },
    "custom": { "enabled": false }
  },
  "output": {
    "dir": "daily-reports",
    "open_browser": true
  }
}
```

### Ejecuciones posteriores

Cuando `config.json` existe:

```
1. Leer config.json
2. Obtener fecha/hora con timezone del config
3. Para cada seccion habilitada, recolectar datos:

   greeting  -> nombre + fecha + hora + dia de la semana
   quote     -> fetch https://zenquotes.io/api/today/ (si falla, omitir)
   tasks     -> leer archivo .md del path configurado, extraer tareas pendientes
   journal   -> leer archivo .md, extraer entradas recientes
   finance   -> ejecutar scripts Python de /scripts/trm/ (si disponibles)
   projects  -> Linear MCP: listar issues activos (si MCP disponible)
   email     -> Gmail MCP: buscar emails no leidos importantes (si MCP disponible)
   calendar  -> Google Calendar MCP: reuniones de hoy (si MCP disponible)
   custom    -> resolver creativamente segun el prompt del usuario

4. IMPORTANTE: Si una seccion falla (MCP no disponible, archivo no existe,
   API no responde), OMITIR esa seccion silenciosamente. No interrumpir el brief.
   Registrar en la seccion "Fuentes" cuales funcionaron y cuales no.

5. Escribir _workspace/daily-data.json con todos los datos recolectados.
   SIEMPRE usar _workspace/ como directorio temporal para este archivo.

6. Ejecutar generate.sh. La ruta del script es relativa al skill:
   bash skills/daily-brief/generate.sh _workspace/daily-data.json
   (Si el plugin esta en otra ubicacion, usar la ruta absoluta del skill directory)

7. Abrir el HTML generado en el navegador:
   - macOS: open <ruta-al-html>
   - Linux: xdg-open <ruta-al-html>
   - Windows/WSL: wslview <ruta-al-html> o explorer.exe <ruta-al-html>
   Solo abrir si open_browser: true en config (default: true).
```

## Schema del JSON de datos (daily-data.json)

El JSON que el agente genera y pasa a generate.sh:

```json
{
  "name": "Maria",
  "locale": "es",
  "dia_semana": "Jueves",
  "fecha_larga": "20 de marzo de 2026",
  "hora": "08:45",
  "timezone_label": "CST",

  "quote_text": "The only way to do great work...",
  "quote_author": "Steve Jobs",

  "stats": [
    { "label": "Tareas hoy", "value": "5", "color": "teal" },
    { "label": "TRM", "value": "$4.250,30", "color": "teal", "delta": "+$12,50 vs ayer", "delta_class": "up" }
  ],

  "alerts": [
    { "type": "warning", "title": "Factura vencida", "desc": "Cliente X - 15 dias" }
  ],

  "sections": [
    {
      "id": "tasks",
      "title": "Tareas pendientes",
      "badge": "5 pendientes",
      "content_html": "<div class=\"item\">..."
    },
    {
      "id": "finance",
      "title": "Indicadores",
      "content_html": "..."
    }
  ],

  "sources": [
    { "name": "to-do.md", "status": "ok" },
    { "name": "zenquotes.io", "status": "ok" },
    { "name": "TRM (SDMX)", "status": "ok" },
    { "name": "Linear", "status": "skip", "reason": "MCP no disponible" }
  ]
}
```

## Generacion de HTML

El HTML se genera via `generate.sh` que:
1. Lee el JSON con python3
2. Inyecta valores en el template HTML
3. Las secciones son modulares: solo se renderizan las que tienen datos
4. Los colores del brand se inyectan como CSS variables

Ver `references/components.md` para el catalogo completo de componentes HTML disponibles.

## Personalizar despues del setup

El usuario puede decir:
- "agrega la seccion de email a mi brief" -> actualizar config.json
- "cambia los colores de mi brief" -> actualizar brand en config.json
- "quita la seccion de projects" -> deshabilitar en config.json
- "resetea mi brief" -> borrar config.json y correr setup de nuevo

## Evolucion adaptativa

El brief NO es estatico. Debe evolucionar con el usuario a traves de dos mecanismos:

### 1. Sugerencias proactivas

Al final de cada brief, EVALUAR si hay secciones deshabilitadas que podrian
activarse con el entorno actual del usuario. Si las hay, agregar un bloque
de sugerencias al final del HTML (antes del footer):

```
Reglas para sugerir:
- Si Gmail MCP esta disponible pero email esta deshabilitado:
  -> "Tienes Gmail conectado. Quieres agregar emails prioritarios a tu brief?"
- Si Linear MCP esta disponible pero projects esta deshabilitado:
  -> "Detecte Linear MCP. Puedo incluir un resumen de issues activos."
- Si Google Calendar MCP esta disponible pero calendar esta deshabilitado:
  -> "Tienes Google Calendar. Quiero agregar tu agenda de hoy?"
- Si Python esta disponible pero finance esta deshabilitado:
  -> "Puedo incluir la TRM y otros indicadores financieros."
- Si el usuario tiene archivos .md en el workspace pero tasks/journal no apuntan a ellos:
  -> "Vi que tienes brain/to-do.md. Quieres que lo incluya en tu brief?"
```

Mostrar MAXIMO 1 sugerencia por ejecucion. No repetir una sugerencia que el
usuario ya rechazo (guardar rechazos en config.json bajo `dismissed_suggestions`).

Formato en HTML:
```html
<div class="alert info">
  <span class="alert-icon">+</span>
  <div class="alert-body">
    <div class="alert-title">Detecte Gmail conectado</div>
    <div class="alert-desc">Puedo agregar tus emails prioritarios al brief.
    Dime "agrega email a mi brief" para activarlo.</div>
  </div>
</div>
```

### 2. Aprendizaje de preferencias

A medida que el usuario interactua, el skill debe ir refinando el config.json:

**Ajustes automaticos (sin preguntar):**
- Si el usuario consistentemente ignora una seccion (nunca la menciona, no
  interactua con ella), bajarla de prioridad en el orden de secciones
- Si el usuario pide informacion extra en conversacion ("y como va la cartera?"),
  sugerir agregarla como seccion en la proxima ejecucion

**Ajustes que requieren confirmacion:**
- Habilitar/deshabilitar secciones
- Cambiar paths de archivos
- Modificar colores o branding
- Agregar secciones custom nuevas

**Que guardar en config.json:**
```json
{
  "dismissed_suggestions": ["email", "calendar"],
  "section_order": ["greeting", "quote", "tasks", "finance", "projects"],
  "last_suggestion_date": "2026-03-20",
  "usage_count": 15
}
```

### 3. Deteccion de entorno

En cada ejecucion, antes de recolectar datos, hacer un scan rapido del entorno:

```
1. Verificar que MCPs estan disponibles (intentar una operacion minima)
2. Verificar que Python esta disponible (python3 --version)
3. Buscar archivos comunes que podrian ser fuentes de datos:
   - **/to-do.md, **/todo.md, **/tasks.md
   - **/journal.md, **/diary.md, **/log.md
   - **/CLAUDE.md (puede tener contexto util sobre el usuario)
4. Comparar con lo que hay en config.json
5. Si hay nuevas capacidades disponibles, preparar sugerencia
```

Este scan NO debe ser lento. Si un MCP no responde en 2 segundos, marcarlo como
no disponible y seguir.

## Degradacion elegante

El brief funciona en CUALQUIER entorno. Lo minimo viable es:

```
Sin nada:           Greeting + fecha + quote
+ archivo to-do:    + seccion de tareas
+ Python:           + indicadores financieros (TRM)
+ Linear MCP:       + resumen de proyectos
+ Gmail MCP:        + emails prioritarios
+ Todo configurado: Brief completo
```

> **Nota Cowork/Web:** En entornos sin shell (Claude Cowork, web), NO ejecutar
> generate.sh. En su lugar, generar el brief como Markdown directamente en el chat.
> Las secciones que requieren Python o MCP se omiten automaticamente.
>
> Ejemplo de output en modo texto:
> ```
> # Daily Brief — Jueves 20 de marzo de 2026
> Buenos dias, Maria.
>
> ---
> > "The only way to do great work is to love what you do." — Steve Jobs
> ---
>
> ## Tareas pendientes (5)
> - [ ] Revisar propuesta cliente X
> - [ ] Enviar factura mensual
> - [ ] Code review PR #42
> - [x] Actualizar documentacion
> - [ ] Preparar agenda reunion viernes
>
> ## Fuentes
> to-do.md (ok) · zenquotes.io (ok) · Linear (no disponible)
> ```

## Historial (history.log)

Despues de generar cada brief, agregar una linea al archivo `history.log` en el
directorio de output (ej: `daily-reports/history.log`). Formato CSV:

```
fecha,tareas_pendientes,tareas_completadas,alertas,stats_extra
2026-03-20,5,2,1,trm:4250.30
2026-03-19,6,3,0,trm:4237.80
```

Esto permite comparaciones dia a dia en el brief:
- "Ayer tenias 6 tareas pendientes, hoy 5 (-1)"
- "TRM subio +$12,50 vs ayer"

Si history.log no existe, crearlo. Si existe, leer la ultima linea para
calcular deltas y mostrarlos en los stat cards.

## Gotchas

1. **No hardcodear nada**: Todo viene del config.json. Nombre, timezone, paths, secciones.
2. **Quote puede fallar**: zenquotes.io tiene rate limits. Si falla, omitir sin error.
3. **Encoding archivos**: Si lees .md del usuario, usar UTF-8. Si procesas CSVs bancarios, ver skill de conciliacion.
4. **Timezone**: Siempre usar TZ del config para fecha/hora. No asumir timezone del sistema.
5. **El JSON es el contrato**: El agente genera el JSON, generate.sh genera el HTML. No generar HTML directamente.
