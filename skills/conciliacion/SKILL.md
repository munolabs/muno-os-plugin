---
name: conciliacion
description: Reconciliación de extractos bancarios CSV, categorización de transacciones y análisis de cashflow. Trigger en "conciliar", "extracto bancario", "movimientos del banco", "cashflow", "suscripciones SaaS", "categorizar transacciones".
---

# Conciliación Bancaria

Procesa extractos bancarios CSV, identifica patrones de movimientos, categoriza transacciones y genera análisis de cashflow.

## Setup

Si no existe `config.json` en este directorio, preguntar al usuario:
1. Ruta donde guarda extractos bancarios
2. Moneda principal (COP, USD)
3. Si quiere comparación con períodos anteriores

```json
{
  "extractos_path": "/ruta/a/extractos",
  "moneda": "COP",
  "comparar_anterior": true
}
```

## Archivos en este Skill

```
conciliacion/
├── SKILL.md              # Este archivo
├── config.json           # Configuracion del usuario (se crea en setup)
├── references/
│   ├── patrones.md       # Patrones de categorizacion por banco
│   └── suscripciones.md  # Lista de suscripciones SaaS conocidas
└── assets/
    └── reporte-template.md  # Template del reporte de salida
```

Scripts de referencia (en /scripts/bancos/):
- `consolidar_adaptativo.py` - Consolida multiples CSVs con auto-deteccion de formato
- `consolidar_simple.py` - Version simple para un solo formato
- `consolidar_estados_bancarios.py` - Version con pandas y categorizacion

> **Nota:** Los scripts son de referencia. El agente los adapta automaticamente
> segun el formato de tu banco y la ruta de tus archivos.

## Flujo de Trabajo

### 1. Cargar Extracto
- Buscar CSV en la ruta configurada o pedir al usuario
- Detectar formato automáticamente (Bancolombia, Global66, etc.)

### 2. Categorizar Transacciones
Ver `references/patrones.md` para reglas completas. Resumen:

| Patrón | Categoría | Signo |
|--------|-----------|-------|
| `COMPRA INTL` | Suscripciones SaaS | Negativo |
| `PAGO A NOMIN` | Nómina | Negativo |
| `PAGO A PROV` | Proveedores | Negativo |
| `TRANSF INTERNACIONAL ENVIADA` | Pagos equipo remoto | Negativo |

### 3. Generar Reporte
Usar `assets/reporte-template.md` como base.

## Gotchas

1. **Signo de valores**: En Bancolombia, negativos = egresos, positivos = ingresos. NO asumir lo contrario.

2. **Comisiones SWIFT**: Siempre buscar `COMIS SWIFT GIRO` después de `TRANSF INTERNACIONAL`. Son dos líneas separadas que deben sumarse.

3. **"PAGO A PROV" positivo**: Si el valor es positivo, NO es un pago a proveedor sino un ingreso de cliente. El patrón de texto es ambiguo.

4. **Fechas duplicadas**: Un extracto puede tener múltiples transacciones el mismo día. Agrupar por fecha pierde detalle.

5. **Encoding CSV**: Bancolombia usa Latin-1, no UTF-8. Abrir con `encoding='latin-1'`.

6. **TRM variable**: Las suscripciones en USD se cobran con TRM del día. No asumir TRM fija para calcular equivalencias.

## Scripts de Referencia

Los scripts en `/scripts/bancos/` sirven como base. El agente los adapta al formato
de tu banco y los ejecuta en un directorio temporal:

```bash
# Ejemplo: consolidar extractos
python3 scripts/bancos/consolidar_adaptativo.py extracto1.csv extracto2.csv -o consolidado.csv
```
