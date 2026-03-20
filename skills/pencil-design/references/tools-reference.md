# Pencil MCP - Referencia de Herramientas

## Flujo Típico

```
1. get_editor_state()     → Entender contexto actual
2. open_document()        → Abrir/crear archivo
3. get_guidelines()       → Obtener reglas de diseño
4. get_style_guide()      → Obtener inspiración
5. batch_design()         → Crear diseño
6. get_screenshot()       → Validar visualmente
7. export_nodes()         → Exportar assets finales
```

## Herramientas Disponibles

### get_editor_state()
Obtener estado actual del editor. **Usar al inicio de cada tarea.**

**Retorna:**
- Archivo activo
- Selección actual
- Contexto del usuario

---

### open_document(filePathOrNew)
Abrir archivo .pen existente o crear uno nuevo.

**Parámetros:**
- `"new"` → Crear archivo vacío
- `"/path/to/file.pen"` → Abrir archivo existente

---

### get_guidelines(topic)
Obtener guidelines de diseño por tipo.

**Topics disponibles:**
| Topic | Descripción |
|-------|-------------|
| `code` | Diseño de code editors, terminals |
| `table` | Tablas de datos |
| `tailwind` | Referencia Tailwind |
| `landing-page` | Landing pages |
| `slides` | Presentaciones |
| `design-system` | Sistemas de diseño |
| `mobile-app` | Apps móviles |
| `web-app` | Aplicaciones web |

---

### get_style_guide_tags()
Listar tags disponibles para buscar style guides.

---

### get_style_guide(tags, name)
Obtener style guide por tags o nombre específico.

**Parámetros:**
- `tags`: Array de tags (ej: `["modern", "saas", "minimal"]`)
- `name`: Nombre específico de style guide

---

### batch_get(patterns, nodeIds)
Leer nodos del archivo.

**Parámetros:**
- `patterns`: Patrones de búsqueda
- `nodeIds`: IDs específicos de nodos

---

### batch_design(operations)
Ejecutar operaciones de diseño. **Máximo ~25 operaciones por llamada.**

**Sintaxis de operaciones:**
```javascript
// Insert
varName=I("parentId", { propiedades })

// Copy
varName=C("sourceId", "parentId", { overrides })

// Replace
varName=R("nodeId", { propiedades })

// Update
U("nodeId", { propiedades })

// Delete
D("nodeId")

// Move
M("nodeId", "newParentId", index)

// Generate Image (AI)
G("nodeId", "ai", "prompt de imagen")
```

---

### snapshot_layout()
Ver estructura de layout computado con rectángulos de cada nodo.

---

### get_screenshot(nodeId)
Obtener screenshot de un nodo. **Usar para validación visual.**

---

### get_variables()
Obtener variables y temas definidos en el archivo.

---

### set_variables(variables)
Agregar o actualizar variables del archivo.

---

### find_empty_space_on_canvas(direction, size)
Encontrar espacio vacío para insertar nuevos elementos.

---

### search_all_unique_properties(parentIds)
Buscar propiedades únicas en el árbol de nodos.

---

### replace_all_matching_properties(parentIds, oldValue, newValue)
Reemplazar propiedades recursivamente.

---

### export_nodes(nodeIds, format, folder)
Exportar nodos a imágenes.

**Formatos:** PNG, JPEG, WEBP, PDF
