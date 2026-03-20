---
name: pencil-design
description: "(Advanced) Guia para disenar interfaces web y mobile usando Pencil MCP. Crear mockups, wireframes, landing pages, dashboards, componentes UI. Trigger en 'disenar', 'crear mockup', 'wireframe', 'landing page', 'UI', 'diseno de pantalla', 'archivo .pen'."
---

# Pencil Design (Advanced)

Framework para disenar interfaces usando Pencil MCP. Incluye guidelines, patrones de diseno y mejores practicas.

## Diagnostico inicial

**IMPORTANTE: Antes de hacer cualquier cosa, verificar si Pencil MCP esta disponible.**

Si el usuario pide disenar y Pencil MCP NO esta conectado, responder con:

> **Pencil MCP no esta disponible en tu sesion actual.**
>
> Este skill requiere el MCP de Pencil para crear y editar archivos `.pen`.
>
> **Para instalarlo:**
> 1. Agregar a tu `settings.json` (o configuracion de MCPs):
>    ```json
>    {
>      "mcpServers": {
>        "pencil": {
>          "command": "npx",
>          "args": ["-y", "@getpencil/mcp-server-pencil"]
>        }
>      }
>    }
>    ```
> 2. Reiniciar Claude Code / tu agente
> 3. Verificar que aparezca "pencil" en las herramientas disponibles
>
> **Nota:** Si estas usando Claude desde una interfaz web (Cowork, etc.) sin soporte para MCPs locales, este skill no funcionara. Considera usar Claude Code en terminal para acceder a esta funcionalidad.

Si Pencil MCP SI esta disponible, continuar con el flujo normal.

## Archivos en este Skill

```
pencil-design/
├── SKILL.md
├── references/
│   ├── tools-reference.md   # Referencia de herramientas Pencil MCP
│   └── design-patterns.md   # Patrones de diseno recomendados
```

## Prerequisitos

- Pencil MCP server conectado (ver diagnostico arriba)
- Archivo .pen abierto o crear uno nuevo

## Flujo de Trabajo

### 1. Entender el Contexto
Antes de diseñar, obtener:
- Tipo de diseño (landing, dashboard, mobile app, etc.)
- Audiencia target
- Estilo deseado (minimalista, colorido, corporativo)
- Referencias o inspiración

### 2. Obtener Guidelines
```
get_guidelines(topic="landing-page|web-app|mobile-app|dashboard|slides")
```

### 3. Obtener Style Guide
```
get_style_guide_tags()  # Ver tags disponibles
get_style_guide(tags=["modern", "saas", "minimal"])
```

### 4. Diseñar

**Verificar estado del editor:**
```
get_editor_state()
```

**Si no hay archivo abierto:**
```
open_document("new")  # Crear nuevo
open_document("/path/to/file.pen")  # Abrir existente
```

**Diseñar con batch_design:**
```
batch_design(operations=[
    'frame1=I("root", {...})',  # Insert
    'button=I("frame1", {...})',
    'U("frame1", {...})',  # Update
])
```

### 5. Validar Visualmente
```
get_screenshot(nodeId="frame1")
```

## Herramientas Pencil MCP

Ver `references/tools-reference.md` para documentación completa. Resumen:

| Tool | Uso |
|------|-----|
| `get_editor_state` | Estado actual del editor |
| `open_document` | Abrir o crear .pen |
| `get_guidelines` | Guidelines por tipo de diseño |
| `get_style_guide` | Inspiración de estilo |
| `batch_get` | Leer nodos existentes |
| `batch_design` | Crear/modificar diseño |
| `get_screenshot` | Validar visualmente |
| `snapshot_layout` | Ver estructura de layout |

## Gotchas

1. **NUNCA usar Read/Grep en archivos .pen**: El contenido está encriptado. Solo usar herramientas Pencil MCP.

2. **batch_design tiene límite**: Máximo ~25 operaciones por llamada. Para diseños complejos, dividir en múltiples llamadas.

3. **IDs de nodos son importantes**: Guardar los IDs retornados por Insert para referencias posteriores.

4. **Validar con screenshot**: No confiar solo en el código. Siempre verificar visualmente el resultado.

5. **Resolución de exportación**: Screenshots tienen ~500px max. Para alta resolución, exportar con `export_nodes`.

6. **Auto-layout vs manual**: Preferir auto-layout cuando sea posible para diseños responsivos.

## Operaciones batch_design

### Insert (I)
```javascript
foo=I("parentId", {
  type: "FRAME",
  name: "Container",
  width: 400,
  height: 300,
  fills: [{ type: "SOLID", color: "#FFFFFF" }]
})
```

### Update (U)
```javascript
U("nodeId", {
  name: "Updated Name",
  fills: [{ type: "SOLID", color: "#000000" }]
})
```

### Copy (C)
```javascript
baz=C("sourceId", "parentId", { x: 100, y: 100 })
```

### Replace (R)
```javascript
R("nodeId", { ...nuevas propiedades })
```

### Delete (D)
```javascript
D("nodeId")
```

### Move (M)
```javascript
M("nodeId", "newParentId", 2)  // índice 2
```

### Generate Image (G)
```javascript
G("nodeId", "ai", "descripción de la imagen")
```

## Patrones de Diseño

Ver `references/design-patterns.md` para:
- Hero sections
- Feature grids
- Pricing tables
- Forms
- Navigation
- Cards
- CTAs

## Ejemplos

Ver `references/design-patterns.md` para patrones reutilizables de diseño: landing pages, dashboards, modales, formularios y componentes comunes.
