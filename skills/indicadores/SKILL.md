---
name: indicadores
description: Consulta de indicadores económicos (TRM, IBR, DTF) y precios de mercado (acciones, ETFs). Usar cuando pidan "TRM", "dólar hoy", "precio de [acción]", "indicadores económicos".
---

# Indicadores Económicos y Mercado

Obtiene indicadores económicos colombianos (TRM, IBR, DTF) del Banco de la República y precios de acciones/ETFs via Alpha Vantage.

## Trigger

Usar cuando el usuario pida:
- "cuál es la TRM hoy"
- "precio del dólar"
- "indicadores económicos"
- "precio de NVDA/AAPL/SPY"
- "cómo está el mercado"
- "variación del S&P 500"

## TRM - Tasa Representativa del Mercado

### Script Principal

```bash
python3 scripts/trm/get_trm_sdmx.py
```

### Fuente Oficial
- **API**: Banco de la República (SDMX REST)
- **URL**: https://totoro.banrep.gov.co/nsi-jax-ws/rest/data
- **Actualización**: Diaria (días hábiles)

### Output Ejemplo

```
=============================================
 TRM OFICIAL - Banco de la República
=============================================

   Valor:  $4.123,45 COP/USD
   Fecha:  18/03/2026

   Fuente: https://www.banrep.gov.co
=============================================
```

### Backup

Si el API principal falla:
```bash
python3 scripts/trm/get_trm_banrep.py
```

## Otros Indicadores Colombia

### IBR (Indicador Bancario de Referencia)
- Tasa interbancaria a un dia
- Usado para creditos corporativos

### DTF (Depositos a Termino Fijo)
- Promedio ponderado de captacion CDTs
- Base para muchos creditos

> Nota: Para consultar IBR y DTF, el agente puede usar el mismo API SDMX
> del Banco de la Republica ajustando el FLOW_ID en el script de TRM.

## Acciones y ETFs

Para consultar precios de acciones y ETFs, se puede usar cualquier API
de mercado (Alpha Vantage, Yahoo Finance, etc.). El agente debe adaptar
el script segun la API disponible.

### ETFs Comunes

| Símbolo | Índice | Descripción |
|---------|--------|-------------|
| SPY | S&P 500 | 500 empresas más grandes de USA |
| QQQ | Nasdaq 100 | Tech-heavy index |
| DIA | Dow Jones | 30 blue chips industriales |
| IWM | Russell 2000 | Small caps |

### Acciones Tech Frecuentes

| Símbolo | Empresa |
|---------|---------|
| AAPL | Apple |
| MSFT | Microsoft |
| NVDA | NVIDIA |
| GOOGL | Alphabet |
| AMZN | Amazon |
| META | Meta |

## Uso en Rutina Diaria

Este skill se puede integrar en rutinas de inicio del asistente para
obtener automaticamente la TRM al comenzar el dia.

## Output Formateado

### TRM
```
TRM hoy (18/03/2026): $4.123,45 COP/USD
Fuente: Banco de la República
```

### Acciones
```
NVDA - NVIDIA Corporation
Precio: $875.23 USD
Cambio: +2.34% (+$20.01)
Volumen: 45.2M
```

## Parámetros

| Param | Valores | Default | Descripción |
|-------|---------|---------|-------------|
| indicador | `trm`, `ibr`, `dtf`, `todos` | `trm` | Indicador económico |
| simbolo | Ticker (NVDA, SPY, etc) | - | Acción o ETF |
| periodo | `dia`, `mes`, `año` | `dia` | Período para históricos |
| chart | `true`, `false` | `false` | Generar gráfica |
