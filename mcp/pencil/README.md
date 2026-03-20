# Pencil MCP - Instrucciones

El Pencil MCP server es el editor para leer y escribir archivos `.pen` y proporciona herramientas para ser un experto generador y validador de diseños para aplicaciones web, móviles y sitios web.

## Reglas Críticas

1. **NUNCA usar Read o Grep en archivos .pen** - El contenido está encriptado y solo es accesible via herramientas Pencil MCP.

2. **SOLO usar herramientas "pencil" MCP** para leer (`batch_get`) y modificar (`batch_design`) contenido de archivos .pen.

3. **Seguir la sintaxis exacta** de las herramientas según sus definiciones.

## Herramientas Disponibles

### Estado y Navegación

| Herramienta | Descripción | Cuándo usar |
|-------------|-------------|-------------|
| `get_editor_state()` | Estado actual del editor | Al inicio de cada tarea |
| `open_document(path)` | Abrir archivo .pen o crear nuevo | Cuando no hay editor activo |
| `snapshot_layout()` | Ver estructura de layout | Para decidir dónde insertar |
| `find_empty_space_on_canvas(direction, size)` | Encontrar espacio vacío | Antes de insertar nuevos frames |

### Guidelines y Estilo

| Herramienta | Descripción | Cuándo usar |
|-------------|-------------|-------------|
| `get_guidelines(topic)` | Reglas de diseño por tipo | Al iniciar tarea de diseño |
| `get_style_guide_tags()` | Tags de estilos disponibles | Después de `get_guidelines` |
| `get_style_guide(tags, name)` | Inspiración de estilo | Para diseños de screens/dashboards |

**Topics de guidelines:**
- `code` - Editors, terminals
- `table` - Tablas de datos
- `tailwind` - Referencia Tailwind
- `landing-page` - Landing pages
- `slides` - Presentaciones
- `design-system` - Sistemas de diseño
- `mobile-app` - Apps móviles
- `web-app` - Aplicaciones web

### Lectura y Búsqueda

| Herramienta | Descripción | Cuándo usar |
|-------------|-------------|-------------|
| `batch_get(patterns, nodeIds)` | Leer nodos por patrón o ID | Para descubrir estructura |
| `search_all_unique_properties(parentIds)` | Buscar propiedades únicas | Para entender estilos existentes |
| `get_variables()` | Variables y temas | Para ver design tokens |

### Diseño y Modificación

| Herramienta | Descripción | Cuándo usar |
|-------------|-------------|-------------|
| `batch_design(operations)` | Insertar/copiar/actualizar/eliminar nodos | Para crear o modificar diseño |
| `set_variables(vars)` | Agregar/actualizar variables | Para definir design tokens |
| `replace_all_matching_properties(parentIds, old, new)` | Reemplazo masivo | Para cambios globales de estilo |

### Validación y Exportación

| Herramienta | Descripción | Cuándo usar |
|-------------|-------------|-------------|
| `get_screenshot(nodeId)` | Screenshot de un nodo | Para validar visualmente |
| `export_nodes(nodeIds, format, folder)` | Exportar a PNG/JPEG/WEBP/PDF | Para assets finales |

## Sintaxis de batch_design

**Límite:** Máximo ~25 operaciones por llamada.

### Insert (I)
```javascript
variableName=I("parentId", {
  type: "FRAME",
  name: "MiFrame",
  width: 400,
  height: 300,
  fills: [{ type: "SOLID", color: "#FFFFFF" }],
  // más propiedades...
})
```

### Copy (C)
```javascript
variableName=C("sourceNodeId", "parentId", {
  x: 100,
  y: 200,
  // overrides opcionales
})
```

### Replace (R)
```javascript
variableName=R("nodeId1/nodeId2", {
  // nuevas propiedades completas
})
```

### Update (U)
```javascript
U("nodeId", {
  name: "NuevoNombre",
  // propiedades a actualizar
})

// Con variable previa
U(variableName+"/childId", {
  // propiedades
})
```

### Delete (D)
```javascript
D("nodeId")
```

### Move (M)
```javascript
M("nodeId", "newParentId", indexPosition)
```

### Generate Image (G)
```javascript
G("nodeId", "ai", "Prompt describiendo la imagen a generar")
```

## Flujo de Trabajo Recomendado

```
1. get_editor_state()
   ↓
2. open_document() si necesario
   ↓
3. get_guidelines(topic) para el tipo de diseño
   ↓
4. get_style_guide_tags() → get_style_guide()
   ↓
5. batch_design() para crear diseño
   ↓
6. get_screenshot() para validar
   ↓
7. Iterar 5-6 hasta satisfecho
   ↓
8. export_nodes() para assets finales
```

## Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| No puede leer .pen | Usando Read tool | Usar batch_get |
| Nodo no encontrado | ID incorrecto | Usar batch_get para encontrar IDs |
| Operación falló | Sintaxis incorrecta | Verificar formato de operaciones |
| Demasiadas operaciones | >25 en batch_design | Dividir en múltiples llamadas |
