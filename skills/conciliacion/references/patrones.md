# Patrones de Categorización

## Bancolombia

### Egresos (valores negativos)

| Patrón en Descripción | Categoría | Notas |
|----------------------|-----------|-------|
| `COMPRA INTL` | Suscripciones SaaS | Ver lista en suscripciones.md |
| `PAGO A NOMIN` | Nómina empleados | Pagos de nómina interna |
| `PAGO A PROV` | Proveedores | Solo si valor < 0 |
| `TRANSF INTERNACIONAL ENVIADA` | Pagos equipo remoto | Freelancers internacionales |
| `COMIS SWIFT GIRO VTA MDA EXT` | Comisión transferencia | Agregar al costo de la transferencia anterior |
| `GMF 4X1000` | Impuesto GMF | 4 por mil |
| `CUOTA CREDITO` | Crédito bancario | Pago de préstamo |
| `COMISION` | Comisiones bancarias | Varios tipos |

### Ingresos (valores positivos)

| Patrón en Descripción | Categoría | Notas |
|----------------------|-----------|-------|
| `TRANSF DE` | Ingreso cliente | Transferencia recibida |
| `ABONO` | Ingreso cliente | Consignación |
| `PAGO A PROV` | Ingreso cliente | Sí, confuso pero si es positivo es ingreso |

## Global66

| Patrón | Categoría | Notas |
|--------|-----------|-------|
| `Transferencia enviada` | Pago equipo remoto | Pagos internacionales |
| `Transferencia recibida` | Ingreso | Fondeo de cuenta |
| `Comisión` | Fee Global66 | Costo del servicio |

## Reglas Especiales

### Agrupar transferencias SWIFT
```
TRANSF INTERNACIONAL ENVIADA    -$5,000,000
COMIS SWIFT GIRO VTA MDA EXT   -$150,000
---
Total real del pago: $5,150,000
```

Buscar comisión SWIFT dentro de las 3 transacciones siguientes a una transferencia internacional.

### Suscripciones en USD
Las "COMPRA INTL" se cobran en COP con TRM del día. Para calcular USD:
1. Obtener TRM de la fecha de la transacción
2. Dividir monto COP / TRM = USD aproximado
