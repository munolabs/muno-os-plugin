# Way of Working - Agency PM

## Estructura de Proyectos

```
proyectos/
├── [cliente]/
│   ├── README.md         # Info cliente + tabla de proyectos
│   ├── activo/           # Proyectos en curso
│   │   └── [proyecto]/
│   ├── _cerrado/         # Proyectos finalizados
│   └── [generales]       # Contratos, templates del cliente
```

## Clasificación por Tiers

> ⚙️ **Personalización**: Los umbrales de revenue son orientativos — ajustalos según el tamaño
> de tu agencia. Una agencia de $50K USD/mes tiene umbrales diferentes a una de $500K.
> Puedes decirle a Claude: *"En mi agencia, Tier 1 es +$5K USD/mes"* y usará ese criterio.

### Tier 1 - Alta Prioridad

**Owner:** Socio / Director

**Criterios (ajustar según tu agencia en `config.json`):**
- Revenue alto para tu contexto (definir umbral en config)
- Decisión estratégica (aunque revenue bajo)
- ROI potencial alto
- Proyecto referencia para el portafolio

**Commitment:**
- Weekly interno obligatorio
- Weekly con cliente obligatorio
- Reporte semanal al cliente
- Respuesta en <24h

### Tier 2 - Delegable

**Owner:** Miembro del equipo (con supervisión de socio)

**Criterios:**
- Revenue menor
- Proyectos operativos
- Equipo listo para ownership

**Commitment:**
- Biweekly interno
- Weekly con cliente
- Reporte quincenal
- Supervisión quincenal de socio

## Tipos de Proyecto

### Project Based (Entrega)
- **Duración:** Finita (semanas a meses)
- **Facturación:** Por milestones
- **Entregable:** Producto/feature específico
- **Soporte post-entrega:** Limitado o no incluido

**Estructura mínima:**
```
[proyecto]/
├── README.md
└── meetings.md (opcional)
```

### Service Based (Servicio)
- **Duración:** Ongoing (meses a años)
- **Facturación:** Retainer mensual
- **Entregable:** Capacidad extendida, expertise
- **Rol típico:** Fractional CTO, Staff augmentation

**Estructura mínima:**
```
[proyecto]/
├── README.md
├── Soporte.md
├── meetings.md
└── weekly-notes.md
```

### Product Based (Producto)
- **Duración:** Ongoing
- **Facturación:** Por consumo o mensual
- **Entregable:** Plataforma/producto como servicio
- **Responsabilidad:** Desarrollo + operación

**Estructura mínima:**
```
[proyecto]/
├── README.md
├── Soporte.md      # CRÍTICO
├── meetings.md
└── weekly-notes.md
```

## Mínimos No Negociables

Todo proyecto activo debe tener:

- [ ] Owner definido
- [ ] Weekly interno (mínimo biweekly para Tier 2)
- [ ] Weekly con cliente
- [ ] Tareas en Linear actualizadas
- [ ] Documentación en Notion

Para Service/Product Based, adicional:
- [ ] Soporte.md con procedimientos
- [ ] weekly-notes.md actualizado
