# Muno-OS (beta)

**Muno-OS** es un plugin de Claude Code con skills especializados para agencias de software y equipos de tecnologia en LATAM.

Estos skills fueron creados originalmente para uso interno de [Muno Labs](https://munolabs.com), una agencia de software e IA en Colombia. Estamos abriendolos al publico porque creemos que pueden ser utiles para mas equipos. Es una beta -- recibimos comentarios, sugerencias y reportes de issues con los brazos abiertos.

## Skills Incluidos

### Sin dependencias externas (funcionan en cualquier entorno)

| Skill | Descripcion |
|-------|-------------|
| **quick-start** | Onboarding guiado: explica el framework de capas, detecta tu entorno y recomienda por donde empezar |
| **daily-brief** | Brief matutino personalizado en HTML. Setup conversacional, secciones modulares, progressive enhancement |
| **daily-writing** | Generacion de contenido para LinkedIn/Twitter con sistema anti-slop |
| **document-style** | Estilos corporativos configurables para documentos (propuestas, contratos, reportes) |

### Requieren Python (entorno local con shell)

| Skill | Descripcion |
|-------|-------------|
| **conciliacion** | Analisis y conciliacion de extractos bancarios CSV (Bancolombia, Global66) |
| **indicadores** | Consulta de TRM, indicadores economicos del Banco de la Republica |

### Requieren MCP o servicios externos (Advanced)

| Skill | Dependencia | Descripcion |
|-------|-------------|-------------|
| **agency-pm** | Linear MCP | Gestion de proyectos: onboarding, weekly reports, tiers, seguimiento |
| **pencil-design** | Pencil MCP + App | Diseno de interfaces, mockups, landing pages |
| **document-ocr** | AWS Textract + Python | Extraccion de texto de PDFs e imagenes escaneadas |
| **screenshot-organizer** | macOS + Python | Organizacion inteligente de capturas de pantalla |

> **Nota sobre Claude Cowork / interfaces web:** Los skills que requieren Python, MCP o acceso al filesystem solo funcionan con Claude Code en terminal. Los skills sin dependencias (daily-writing, document-style) funcionan en cualquier entorno.

## Instalacion

### Opcion A: Descarga directa (recomendado)

1. Descargar: [muno-os-plugin.zip](https://github.com/munolabs/muno-os-plugin/archive/refs/heads/main.zip)
2. Descomprimir
3. En Claude Code: `claude --plugin-dir /ruta/a/muno-os-plugin`

### Opcion B: Clonar desde GitHub

```bash
cd ~/.claude/plugins
git clone https://github.com/munolabs/muno-os-plugin.git
claude --plugin-dir ~/.claude/plugins/muno-os-plugin
```

## Configurar MCPs (opcional, para skills Advanced)

### Linear (para agency-pm)

```json
{
  "mcpServers": {
    "linear": {
      "command": "npx",
      "args": ["-y", "@linear/mcp-server-linear"]
    }
  }
}
```

### Pencil (para pencil-design)

```json
{
  "mcpServers": {
    "pencil": {
      "command": "npx",
      "args": ["-y", "@getpencil/mcp-server-pencil"]
    }
  }
}
```

### AWS Textract (para document-ocr)

Requiere AWS CLI configurado con credenciales y permisos para Textract.
Ver [documentacion de AWS Textract](https://docs.aws.amazon.com/textract/).

## Uso

Los skills se invocan con el prefijo del plugin:

```
/muno-os:quick-start          # Onboarding: por donde empezar con el plugin
/muno-os:daily-brief           # Brief matutino personalizado
/muno-os:indicadores          # Consultar TRM actual
/muno-os:conciliacion         # Analizar extracto bancario
/muno-os:agency-pm            # Gestionar proyectos en Linear
/muno-os:daily-writing        # Crear post LinkedIn/Twitter
/muno-os:document-style       # Formatear documento corporativo
/muno-os:pencil-design        # Crear mockup (requiere Pencil MCP)
```

## Scripts de referencia

La carpeta `scripts/` contiene scripts Python que los skills usan como base.
El agente los adapta automaticamente segun tu entorno:

```
scripts/
├── bancos/          # Consolidacion de extractos bancarios
├── trm/             # Consulta de TRM del Banco de la Republica
└── ocr/             # OCR con AWS Textract
```

Los scripts reciben parametros por argumento (no tienen rutas hardcodeadas).

## Personalizar estilos corporativos

El skill `document-style` usa estilos por defecto que puedes personalizar
editando `skills/document-style/config.json` con los colores y fuentes de tu marca.

## Requisitos

- Claude Code v1.x o superior
- Python 3.x (para indicadores, conciliacion, document-ocr, screenshot-organizer)
- Node.js (para MCPs opcionales)

## Troubleshooting

### "MCP not connected" al usar pencil-design o agency-pm

El MCP correspondiente no esta configurado. Ver seccion "Configurar MCPs" arriba.
Si usas Claude desde una interfaz web sin soporte para MCPs locales, estos skills
no estaran disponibles -- usa Claude Code en terminal.

### Scripts fallan por encoding

Los extractos de Bancolombia usan encoding Latin-1. Si ves caracteres raros,
verifica que el script use `encoding='latin-1'`.

## Feedback

Este plugin esta en beta. Estamos iterando activamente y valoramos tu feedback:

- Issues y sugerencias: https://github.com/munolabs/muno-os-plugin/issues
- Contacto: fb@munolabs.com

Hecho con cafe en Medellin, Colombia por [Muno Labs](https://munolabs.com).

## Licencia

MIT
