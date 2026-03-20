---
name: screenshot-organizer
description: Organiza y renombra capturas de pantalla analizando contenido visual, agregando metadata descriptiva y tags de Finder. Trigger en "organizar capturas", "renombrar screenshots", "limpiar screenshots", "organize screenshots", "clasificar capturas".
---

# Screenshot Organizer

Analiza imágenes de capturas de pantalla, las renombra descriptivamente según su contenido, y agrega metadata en macOS para facilitar búsquedas.

## Archivos en este Skill

```
screenshot-organizer/
├── SKILL.md
└── references/
    ├── tag-taxonomy.md   # Categorías y tags disponibles
    └── naming-rules.md   # Reglas de nombrado
```

## Flujo de Trabajo

### 1. Buscar Capturas

```bash
# Patrones por defecto
find ~/Desktop ~/Downloads -name "CleanShot*" -o -name "Screenshot*" -mtime -30
```

**Omitir:**
- Archivos en subcarpetas (a menos que se pida explícitamente)
- Archivos ya procesados (verificar xattr)

### 2. Verificar si Ya Procesado

```bash
# Verificar marca
xattr -p com.munolabs.screenshot-organized "/path/file.png" 2>/dev/null
# Si retorna "true", saltar
```

### 3. Analizar Cada Imagen

Usar Read tool (multimodal) para ver la imagen. Identificar:
- **Tipo de contenido**: UI, código, email, documento, gráfico, formulario, error
- **Aplicación/contexto**: Slack, GitHub, Figma, terminal, browser
- **Proyecto/cliente**: Si se puede relacionar con proyectos conocidos
- **Identificadores**: Nombres, fechas, números, títulos visibles

### 4. Generar Nombre Descriptivo

**Formato:** `[contexto]-[descripcion].png`

```
slack-mensaje-error-deploy.png
github-pr-review-comments.png
figma-wireframe-login.png
excel-reporte-ventas-q1.png
terminal-docker-logs.png
```

**Reglas:**
- Minúsculas, kebab-case
- Sin fechas en nombre (metadata maneja eso)
- Máximo 60 caracteres
- Específico pero conciso

### 5. Agregar Metadata (macOS)

**Comentario Spotlight** (buscable con Cmd+Space):
```bash
osascript -e 'set fp to POSIX file "/ruta/archivo.png" as alias' \
  -e 'tell application "Finder" to set comment of fp to "Descripción. Proyecto: X"'
```

**Tags de Finder** (colores):
```bash
xattr -w com.apple.metadata:_kMDItemUserTags \
  '<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><array><string>Tag1</string><string>Tag2</string></array></plist>' \
  "/ruta/archivo.png"
```

### 6. Marcar como Procesado

```bash
xattr -w com.munolabs.screenshot-organized "true" "/path/file.png"
```

## Modos de Ejecución

| Modo | Descripción |
|------|-------------|
| **Interactivo** (default) | Mostrar cambios propuestos, confirmar antes |
| **Auto** (`--auto`) | Procesar sin confirmación |
| **Dry run** (`--dry-run`) | Mostrar qué haría, sin ejecutar |

## Gotchas

1. **Read tool funciona con imágenes**: Claude es multimodal, puede "ver" screenshots.

2. **xattr puede fallar en algunos sistemas de archivos**: Verificar que el sistema soporte extended attributes.

3. **Nombres muy largos**: macOS tiene límite de 255 caracteres. Truncar si necesario.

4. **Screenshots con información sensible**: No incluir passwords, tokens, o datos sensibles en el nombre o comentario.

5. **Duplicados**: Si el nombre ya existe, agregar sufijo numérico (-1, -2, etc.)

## Tags por Categoría

Ver `references/tag-taxonomy.md` para lista completa.

### Genéricos
- `UI` - Interfaces de usuario
- `Code` - Código, terminales
- `Error` - Mensajes de error
- `Email` - Correos
- `Document` - Documentos, PDFs
- `Chart` - Gráficos, dashboards
- `Meeting` - Calls, videollamadas

### Por Aplicación
- `Slack`, `GitHub`, `Figma`, `Notion`
- `VSCode`, `Terminal`, `Browser`
- `Excel`, `Docs`, `Sheets`

## Output

Al finalizar, reportar:
- Total de archivos procesados
- Archivos renombrados
- Tags aplicados
- Archivos omitidos (ya procesados o excluidos)
