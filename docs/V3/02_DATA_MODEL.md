# SALES DWH PLATFORM — DATA MODEL

Autor: Jonathan Elgueta Elgueta  
Versión: V3.0.0  
Estado: STABLE  
Documento: MODELO DIMENSIONAL  
Última actualización: 2026-05-25  

---

# Descripción

Este documento describe el modelo dimensional implementado en Sales DWH Platform V3.

La solución utiliza arquitectura dimensional orientada a analytics empresariales utilizando fact tables y dimensiones desacopladas.

---

# Objetivos Modelo Dimensional

La arquitectura dimensional fue diseñada para:

- analytics rápidos
- simplicidad consultas
- reutilización métricas
- escalabilidad
- integración BI
- semantic analytics

---

# Arquitectura Modelo

La solución implementa:

```text
FACT TABLE
    ↓
DIMENSION TABLES
```

---

# Fact Table

## fact_sales

La tabla principal almacena métricas transaccionales comerciales.

---

# Grain Fact Table

## Grain definido

```text
1 registro = 
1 producto
1 cliente
1 canal
1 fecha
```

Esto garantiza granularidad consistente para analytics multidimensional.

---

# Métricas Fact

## Métricas principales

| Métrica | Descripción |
|---|---|
| venta_total | ventas monetarias |
| unidades_vendidas | unidades comerciales |
| devoluciones | unidades devueltas |
| pct_devolucion | porcentaje devolución |

---

# Claves Fact

## Foreign Keys

| FK | Referencia |
|---|---|
| date_id | dim_date |
| product_id | dim_product |
| customer_id | dim_customer |
| channel_id | dim_channel |

---

# Dimensiones

---

# dim_date

Dimensión temporal principal.

---

## Objetivos

- análisis temporal
- comparativos YoY
- agregaciones mensuales
- lógica comercial personalizada

---

## Columnas principales

| Columna | Descripción |
|---|---|
| date_id | clave fecha |
| full_date | fecha completa |
| year | año |
| quarter | trimestre |
| month | mes |
| week | semana |
| day_name | nombre día |

---

# Semana Bimbo

La dimensión incorpora lógica comercial personalizada.

## Reglas implementadas

| Regla | Valor |
|---|---|
| inicio semana | jueves |
| fin semana | miércoles |

---

## Objetivo comercial

La Semana Bimbo permite:

- análisis operacional real
- alineación negocio
- reporting corporativo
- consistencia ejecutiva

---

# dim_product

Dimensión productos comerciales.

---

## Objetivos

- analytics producto
- analytics marca
- analytics categoría

---

## Columnas principales

| Columna | Descripción |
|---|---|
| product_id | clave producto |
| producto | nombre producto |
| marca | marca comercial |
| categoria | categoría producto |

---

# dim_customer

Dimensión clientes.

---

## Objetivos

- analytics clientes
- segmentación
- customer performance

---

## Columnas principales

| Columna | Descripción |
|---|---|
| customer_id | clave cliente |
| cliente | nombre cliente |
| region | región |
| ciudad | ciudad |

---

# dim_channel

Dimensión canales comerciales.

---

## Objetivos

- analytics canal
- performance comercial
- retail analytics

---

## Columnas principales

| Columna | Descripción |
|---|---|
| channel_id | clave canal |
| canal | tipo canal |
| cadena | cadena comercial |

---

# Relaciones Modelo

## Relación principal

```text
fact_sales
    ↓
dim_date
dim_product
dim_customer
dim_channel
```

---

# Cardinalidad

| Relación | Cardinalidad |
|---|---|
| fact_sales → dim_date | many-to-one |
| fact_sales → dim_product | many-to-one |
| fact_sales → dim_customer | many-to-one |
| fact_sales → dim_channel | many-to-one |

---

# Semantic Layer

La semantic layer consume directamente el modelo dimensional.

## View principal

```text
vw_sales_enriched
```

---

# Métricas Derivadas

## KPIs implementados

| KPI | Descripción |
|---|---|
| market_share_pct | participación mercado |
| ranking_venta | ranking comercial |
| pct_devolucion | porcentaje devolución |

---

# Data Marts

Los marts reutilizan el modelo dimensional.

## Marts implementados

- sales_monthly
- brand_performance
- category_performance
- channel_performance

---

# Beneficios Modelo

## Técnicos

- simplicidad consultas
- performance analytics
- desacoplamiento
- reutilización
- escalabilidad

---

## Negocio

- analytics ejecutivos
- drilldown analytics
- KPIs consistentes
- reporting corporativo

---

# Arquitectura Analítica

El modelo dimensional soporta:

- dashboards ejecutivos
- heatmaps
- YoY analytics
- drilldown analytics
- market share analytics
- trend analytics

---

# Persistencia

## Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| DuckDB | warehouse principal |
| Parquet | persistencia marts |
| Pandas | transformación |

---

# Estado Modelo

## V3 COMPLETADA

La V3 implementa un modelo dimensional enterprise orientado a analytics modernos, semantic analytics y Business Intelligence escalable.