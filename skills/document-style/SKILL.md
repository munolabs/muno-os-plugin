---
name: document-style
description: Aplica estilos corporativos a documentos. Tipografia, colores, formatos de propuestas y contratos. Trigger en "aplicar estilos", "formato corporativo", "formatear documento", "propuesta con estilo", "documento corporativo".
---

# Document Style

Aplica guia de estilos corporativos a documentos: tipografia, colores, tamanos, formatos consistentes.

## Configuracion

Si existe `config.json` en este directorio, usar esos estilos. Si no, preguntar al usuario
o usar los defaults de abajo.

```json
{
  "company_name": "Mi Empresa",
  "fonts": {
    "primary": "Roboto",
    "fallback": "Arial"
  },
  "colors": {
    "primary": "#0000FF",
    "secondary": "#000000",
    "text": "#333333",
    "text_secondary": "#666666",
    "background_alt": "#F5F5F5"
  },
  "logo_path": ""
}
```

> **Personalizar:** Editar `config.json` con los colores y tipografia de tu marca.
> Los valores de abajo son los defaults si no se configura.

## Archivos en este Skill

```
document-style/
├── SKILL.md
├── config.json             # Estilos de tu marca (se crea en setup)
└── references/
    └── brand-guidelines.md # Guia de referencia
```

## Cuando Usar

- Crear propuestas comerciales
- Formatear contratos
- Documentos para clientes
- Presentaciones corporativas
- Reportes formales

## Guia de Estilos (Default)

### Tipografía

| Elemento | Fuente | Tamaño | Peso |
|----------|--------|--------|------|
| Títulos H1 | Roboto | 24pt | Bold |
| Títulos H2 | Roboto | 18pt | Bold |
| Títulos H3 | Roboto | 14pt | SemiBold |
| Cuerpo | Roboto | 11pt | Regular |
| Captions | Roboto | 9pt | Regular |

### Colores

| Uso | Color | Hex |
|-----|-------|-----|
| **Primario** | Azul | #0000FF |
| **Secundario** | Negro | #000000 |
| **Texto** | Gris oscuro | #333333 |
| **Texto secundario** | Gris | #666666 |
| **Fondo alternativo** | Gris claro | #F5F5F5 |
| **Acentos/enlaces** | Azul | #0000FF |

### Espaciado

| Elemento | Valor |
|----------|-------|
| Márgenes de página | 2.5cm todos los lados |
| Espacio entre párrafos | 12pt |
| Espacio entre secciones | 24pt |
| Interlineado | 1.15 |

### Alineación

| Elemento | Alineación |
|----------|------------|
| Títulos | Izquierda |
| Cuerpo | Justificado |
| Bullets | Izquierda |
| Tablas | Izquierda (texto), Derecha (números) |

## Formatos por Tipo de Documento

### Propuesta Comercial

```
1. Portada
   - Logo arriba izquierda
   - Título centrado
   - Fecha abajo derecha

2. Índice (si >5 páginas)

3. Resumen Ejecutivo
   - Máximo 1 página
   - Problema → Solución → Beneficios

4. Alcance
   - Bullets claros
   - Entregables específicos

5. Cronograma
   - Tabla o timeline visual
   - Milestones claros

6. Inversión
   - Tabla con desglose
   - Total prominente

7. Términos y Condiciones
   - Forma de pago
   - Validez de propuesta

8. Equipo (opcional)
   - Fotos + bio breve

9. Contacto
   - Datos de contacto
   - Próximos pasos
```

### Contrato

```
1. Encabezado
   - Título: "CONTRATO DE [TIPO]"
   - Número de contrato

2. Partes
   - Datos completos de cada parte

3. Antecedentes (Considerando que...)

4. Cláusulas
   - Numeradas: PRIMERA, SEGUNDA, etc.
   - Subtítulos en negrita

5. Firmas
   - Espacio para firmas
   - Nombres y cargos
   - Fecha
```

### Reporte

```
1. Portada
2. Resumen Ejecutivo
3. Metodología (si aplica)
4. Hallazgos/Resultados
5. Conclusiones
6. Recomendaciones
7. Anexos
```

## Aplicación en Google Docs

**IMPORTANTE**: Google Docs NO interpreta Markdown directamente. Usar la API de estilos:

```javascript
// Ejemplo: Aplicar estilo de título
requests.push({
  updateParagraphStyle: {
    range: { startIndex, endIndex },
    paragraphStyle: {
      namedStyleType: 'HEADING_1'
    },
    fields: 'namedStyleType'
  }
});
```

## Gotchas

1. **Google Docs ≠ Markdown**: No pegar markdown crudo. Usar herramientas de formateo de Google Docs MCP.

2. **Fuentes**: Si Roboto no está disponible, usar Arial como fallback.

3. **Colores exactos**: Verificar que el azul sea exactamente #0000FF, no aproximaciones.

4. **PDFs**: Al exportar a PDF, verificar que los estilos se mantengan.

5. **Tablas**: Mantener bordes sutiles (gris claro, 0.5pt) no gruesos.

6. **Imágenes**: Resolución mínima 150dpi para impresión.

## Checklist Pre-entrega

- [ ] Tipografía consistente
- [ ] Colores de marca correctos
- [ ] Márgenes uniformes
- [ ] Numeración de páginas
- [ ] Logo en posición correcta
- [ ] Ortografía revisada
- [ ] Links funcionando
- [ ] PDF generado y verificado
