# Conciliación Bancaria: {{BANCO}}

**Período:** {{FECHA_INICIO}} - {{FECHA_FIN}}
**Generado:** {{FECHA_GENERACION}}

---

## Resumen Ejecutivo

{{RESUMEN_3_LINEAS}}

---

## Flujo de Caja

| Concepto | Monto |
|----------|------:|
| **Ingresos** | {{TOTAL_INGRESOS}} |
| **Egresos** | {{TOTAL_EGRESOS}} |
| **Flujo Neto** | **{{FLUJO_NETO}}** |

---

## Ingresos por Origen

| Cliente/Origen | Monto | % |
|----------------|------:|--:|
| {{CLIENTE_1}} | {{MONTO_1}} | {{PCT_1}} |
| {{CLIENTE_2}} | {{MONTO_2}} | {{PCT_2}} |
| ... | | |
| **Total** | **{{TOTAL_INGRESOS}}** | 100% |

---

## Egresos por Categoría

| Categoría | Monto | % | vs Anterior |
|-----------|------:|--:|------------:|
| Nómina | {{NOMINA}} | {{PCT}} | {{DELTA}} |
| Proveedores | {{PROVEEDORES}} | {{PCT}} | {{DELTA}} |
| Suscripciones SaaS | {{SUSCRIPCIONES}} | {{PCT}} | {{DELTA}} |
| Pagos equipo remoto | {{REMOTO}} | {{PCT}} | {{DELTA}} |
| Impuestos & comisiones | {{IMPUESTOS}} | {{PCT}} | {{DELTA}} |
| Otros | {{OTROS}} | {{PCT}} | {{DELTA}} |
| **Total** | **{{TOTAL_EGRESOS}}** | 100% | {{DELTA_TOTAL}} |

---

## Suscripciones SaaS Detectadas

| Servicio | Monto COP | ~USD | Fecha |
|----------|----------:|-----:|-------|
| {{SERVICIO}} | {{COP}} | {{USD}} | {{FECHA}} |

**Total suscripciones:** {{TOTAL_SUSCRIPCIONES}}

---

## Alertas

{{#if ALERTAS}}
{{#each ALERTAS}}
- **{{TIPO}}**: {{DESCRIPCION}}
{{/each}}
{{else}}
Sin alertas para este período.
{{/if}}

---

## Comparación con Período Anterior

{{#if COMPARACION}}
| Métrica | Anterior | Actual | Cambio |
|---------|----------|--------|-------:|
| Ingresos | {{ING_ANT}} | {{ING_ACT}} | {{ING_DELTA}} |
| Egresos | {{EGR_ANT}} | {{EGR_ACT}} | {{EGR_DELTA}} |
| Flujo Neto | {{FLUJO_ANT}} | {{FLUJO_ACT}} | {{FLUJO_DELTA}} |
{{else}}
_No hay datos del período anterior para comparar._
{{/if}}

---

_Generado por skill conciliacion - muno-os-plugin_
