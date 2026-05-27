# SALES DWH PLATFORM — DATA MARTS

Autor: Jonathan Elgueta Elgueta
Versión: V4.0.0
Estado: STABLE
Documento: DATA MARTS
Última actualización: 2026-05-26

---

# Descripción

Este documento describe la arquitectura de Data Marts implementada en Sales DWH Platform V4.

La V4 consolida oficialmente una arquitectura desacoplada donde:

```text
Semantic Layer
    ↓
Analytics Data Marts
    ↓
Enterprise Dashboards
```

Los marts representan la capa optimizada de consumo analítico empresarial.

---

# Objetivos Data Marts

La arquitectura marts fue diseñada para:

- optimizar dashboards
- desacoplar analytics del warehouse
- acelerar consultas
- centralizar KPIs
- habilitar reporting enterprise
- soportar IA y forecasting

---

# Arquitectura Marts

```text
FACT SALES
    +
DIMENSIONS
    ↓
VW_SALES_ENRICHED
    ↓
DATA MARTS
    ↓
STREAMLIT APP
```

---

# Principio Oficial

## Regla Principal

```text
TODOS LOS MARTS CONSUMEN EXCLUSIVAMENTE:
vw_sales_enriched
```

---

# Reglas Oficiales

## Regla 1

```text
MARTS NO LEEN FACTS DIRECTAMENTE
```

---

## Regla 2

```text
MARTS NO REALIZAN JOINS
```

---

## Regla 3

```text
SEMANTIC LAYER CENTRALIZA BUSINESS LOGIC
```

---

## Regla 4

```text
MARTS = CAPA ANALÍTICA OPTIMIZADA
```

---

# Ubicación Oficial

```text
data/marts
```

---

# Arquitectura Física

```text
data/marts/
│
├── mart_sales_monthly.parquet
├── mart_brand_performance.parquet
└── mart_daily_sales.parquet
```

---

# mart_sales_monthly

Mart principal de ventas mensuales.

---

## Objetivo

Proveer:

- ventas mensuales
- tendencias
- YoY analysis
- dashboards ejecutivos

---

## Fuente

```sql
vw_sales_enriched
```

---

## Granularidad

```text
Year / Month
```

---

## Métricas

| Métrica | Descripción |
|---|---|
| venta_total | Venta neta mensual |

---

## Uso

Consumido por:

- Home Dashboard
- Executive Dashboard
- Forecasting

---

# mart_brand_performance

Mart especializado en performance marcas.

---

## Objetivo

Proveer:

- ventas por marca
- market share
- rankings
- analytics marcas

---

## Fuente

```sql
vw_sales_enriched
```

---

## Granularidad

```text
Year / Month / Marca
```

---

## Métricas

| Métrica | Descripción |
|---|---|
| venta_total | Venta neta |
| market_share_pct | Participación mercado |
| ranking_venta | Ranking ventas |

---

## Uso

Consumido por:

- Brand Analytics
- Executive Dashboard
- Market Share KPIs

---

# mart_daily_sales

Mart especializado en granularidad diaria.

---

## Objetivo

Proveer:

- freshness diario
- monitoreo operacional
- última fecha disponible
- análisis transaccional

---

## Fuente

```sql
vw_sales_enriched
```

---

## Granularidad

```text
Diaria
```

---

## Métricas

| Métrica | Descripción |
|---|---|
| venta_total | Venta diaria |

---

## Uso

Consumido por:

- Home Dashboard
- Operational Monitoring
- Freshness Validation

---

# Flujo Generación Marts

```text
WAREHOUSE FACTS
    +
DIMENSIONS
    ↓
SEMANTIC LAYER
    ↓
generate_all_marts()
    ↓
PARQUET MARTS
    ↓
STREAMLIT DASHBOARDS
```

---

# Regeneración Marts

La V4 incorpora regeneración automática.

---

# Flujo

```text
NEW XLSX
    ↓
WAREHOUSE UPDATE
    ↓
SEMANTIC REFRESH
    ↓
MART REBUILD
    ↓
CACHE REFRESH
```

---

# Objetivo

Garantizar:

- consistencia analítica
- dashboards sincronizados
- KPIs actualizados
- freshness enterprise

---

# Performance Enterprise

Los marts optimizan:

- tiempos lectura
- memoria
- rendering dashboards
- consultas analíticas

---

# Beneficios Arquitectónicos

## Desacoplamiento

Separación oficial entre:

```text
WAREHOUSE
SEMANTIC LAYER
MARTS
DASHBOARDS
```

---

## Escalabilidad

Permite:

- nuevos marts
- nuevos dashboards
- nuevos KPIs
- nuevas métricas

---

## Performance

- menor volumen lectura
- agregaciones optimizadas
- consultas rápidas

---

## Gobernanza

- lógica centralizada
- consistencia empresarial
- trazabilidad semántica

---

# Integración Streamlit

La aplicación Streamlit consume exclusivamente:

```text
data/marts
```

---

# Dashboards Consumidores

| Dashboard | Mart |
|---|---|
| Home | mart_sales_monthly |
| Home | mart_daily_sales |
| Executive Dashboard | mart_sales_monthly |
| Executive Dashboard | mart_brand_performance |
| Brand Analytics | mart_brand_performance |

---

# Integración IA

Los marts habilitan:

- forecasting
- anomaly detection
- semantic KPIs
- AI analytics

---

# Beneficios Operacionales

## Operational Monitoring

- freshness diario
- monitoreo incremental
- validación operacional

---

## Executive Analytics

- KPIs ejecutivos
- tendencias
- comparativos YoY

---

## Business Intelligence

- performance marcas
- market share
- analytics negocio

---

# Arquitectura Final

```text
FACTS
    ↓
SEMANTIC LAYER
    ↓
ANALYTICS MARTS
    ↓
STREAMLIT ENTERPRISE APP
```

---

# Consolidación V4

La V4 consolida oficialmente:

- marts desacoplados
- analytics optimizado
- performance enterprise
- semantic governance
- analytical scalability

---

# Estado Data Marts

## V4 COMPLETADA

Estado oficial:

```text
STABLE
```

---