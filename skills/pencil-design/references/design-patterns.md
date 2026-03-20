# Patrones de Diseño

Patrones comunes para interfaces web y mobile.

## Landing Page

### Hero Section
```
┌─────────────────────────────────────────┐
│  Logo                    Nav  Nav  CTA  │
├─────────────────────────────────────────┤
│                                         │
│         [Headline Grande]               │
│         Subheadline explicativo         │
│                                         │
│         [CTA Primario] [CTA Sec]        │
│                                         │
│         [Hero Image/Video]              │
│                                         │
└─────────────────────────────────────────┘
```

**Propiedades clave:**
- Headline: 48-72px, bold
- Subheadline: 18-24px, regular, color secundario
- CTA: Contraste alto, padding generoso
- Espacio: Mucho whitespace

### Features Grid
```
┌─────────────────────────────────────────┐
│         [Título de Sección]             │
│         Descripción breve               │
├───────────┬───────────┬─────────────────┤
│  [Icon]   │  [Icon]   │     [Icon]      │
│  Título   │  Título   │     Título      │
│  Desc     │  Desc     │     Desc        │
├───────────┼───────────┼─────────────────┤
│  [Icon]   │  [Icon]   │     [Icon]      │
│  Título   │  Título   │     Título      │
│  Desc     │  Desc     │     Desc        │
└───────────┴───────────┴─────────────────┘
```

**Propiedades:**
- Grid: 3 columnas desktop, 1 mobile
- Icons: 24-48px, color de marca
- Títulos: 18-24px, semibold
- Descripciones: 14-16px, color secundario

### Pricing Table
```
┌─────────────┬─────────────┬─────────────┐
│   Basic     │   Pro ★     │   Enterprise│
│   $9/mo     │   $29/mo    │   Custom    │
├─────────────┼─────────────┼─────────────┤
│ ✓ Feature 1 │ ✓ Feature 1 │ ✓ All Pro   │
│ ✓ Feature 2 │ ✓ Feature 2 │ ✓ Custom    │
│ ✗ Feature 3 │ ✓ Feature 3 │ ✓ Support   │
├─────────────┼─────────────┼─────────────┤
│  [Choose]   │  [Choose]   │  [Contact]  │
└─────────────┴─────────────┴─────────────┘
```

**Propiedades:**
- Plan destacado: Borde o sombra extra
- Precios: Grande y bold
- Features: Lista con checks
- CTA: Prominente en cada columna

## Dashboard

### Layout Típico
```
┌──────┬──────────────────────────────────┐
│ Logo │  Search        User  Notif       │
├──────┼──────────────────────────────────┤
│ Nav  │  ┌──────────────────────────────┐│
│ Item │  │  KPI Cards (4 columnas)      ││
│ Item │  └──────────────────────────────┘│
│ Item │  ┌─────────────┬────────────────┐│
│ Item │  │  Chart 1    │   Chart 2      ││
│      │  │             │                ││
│ ──── │  └─────────────┴────────────────┘│
│ Item │  ┌──────────────────────────────┐│
│ Item │  │  Table de datos              ││
└──────┴──┴──────────────────────────────┘┘
```

### KPI Card
```
┌────────────────────┐
│ [Icon]  Label      │
│                    │
│ $12,345           │
│ ↑ 12.5%           │
└────────────────────┘
```

**Propiedades:**
- Valor: 24-32px, bold
- Cambio: 12-14px, verde/rojo según dirección
- Background: Ligeramente diferente del fondo

## Componentes Comunes

### Button
```javascript
{
  type: "FRAME",
  cornerRadius: 8,
  paddingLeft: 16,
  paddingRight: 16,
  paddingTop: 12,
  paddingBottom: 12,
  fills: [{ type: "SOLID", color: "#0066FF" }],
  // Texto dentro con color blanco
}
```

### Input Field
```javascript
{
  type: "FRAME",
  cornerRadius: 6,
  strokeWeight: 1,
  strokes: [{ type: "SOLID", color: "#E0E0E0" }],
  fills: [{ type: "SOLID", color: "#FFFFFF" }],
  paddingLeft: 12,
  paddingRight: 12,
  paddingTop: 10,
  paddingBottom: 10,
}
```

### Card
```javascript
{
  type: "FRAME",
  cornerRadius: 12,
  fills: [{ type: "SOLID", color: "#FFFFFF" }],
  effects: [{
    type: "DROP_SHADOW",
    color: { r: 0, g: 0, b: 0, a: 0.08 },
    offset: { x: 0, y: 4 },
    radius: 16
  }],
  padding: 24,
}
```

## Colores

### Escala de Grises
| Nombre | Hex | Uso |
|--------|-----|-----|
| White | #FFFFFF | Fondos, cards |
| Gray 50 | #F9FAFB | Fondos alternos |
| Gray 100 | #F3F4F6 | Hover states |
| Gray 200 | #E5E7EB | Bordes |
| Gray 500 | #6B7280 | Texto secundario |
| Gray 900 | #111827 | Texto principal |
| Black | #000000 | Acentos |

### Semánticos
| Color | Hex | Uso |
|-------|-----|-----|
| Primary | #0066FF | CTAs, links |
| Success | #10B981 | Confirmaciones |
| Warning | #F59E0B | Alertas |
| Error | #EF4444 | Errores |
| Info | #3B82F6 | Información |

## Spacing

Escala de 4px:
- 4, 8, 12, 16, 24, 32, 48, 64, 96

**Uso típico:**
- Padding interno de componentes: 12-16px
- Gap entre elementos: 8-16px
- Secciones: 48-96px
- Márgenes laterales: 24-64px
