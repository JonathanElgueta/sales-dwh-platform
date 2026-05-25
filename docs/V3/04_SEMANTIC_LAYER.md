# SALES DWH PLATFORM — SEMANTIC LAYER

Autor: Jonathan Elgueta Elgueta  
Versión: V3.0.0  
Estado: STABLE  
Documento: SEMANTIC LAYER  
Última actualización: 2026-05-25  

---

# Descripción

Este documento describe la Semantic Layer implementada en Sales DWH Platform V3.

La semantic layer abstrae complejidad técnica y centraliza lógica analítica reutilizable para dashboards, KPIs y analytics empresariales.

---

# Objetivos Semantic Layer

La semantic layer fue diseñada para:

- desacoplar lógica negocio
- centralizar KPIs
- reutilizar métricas
- simplificar analytics
- soportar dashboards ejecutivos
- reducir complejidad consultas

---

# Arquitectura Semantic Layer

La semantic layer se posiciona entre el Data Warehouse y los Data Marts.

```text
DATA WAREHOUSE
        ↓
SEMANTIC LAYER
        ↓
DATA MARTS
        ↓
ANALYTICS APPLICATION
```

---

# Beneficios Arquitectura

## Técnicos

- reutilización lógica
- desacoplamiento
- mantenibilidad
- simplificación SQL
- escalabilidad analytics

---

## Negocio

- KPIs consistentes
- reporting centralizado
- métricas homologadas
- analytics ejecutivos

---

# View Principal

## vw_sales_enriched

La principal view analítica implementada es:

```text
vw_sales_enriched
```

---

# Objetivos View

La view centraliza:

- joins dimensionales
- métricas derivadas
- KPIs ejecutivos
- market share
- rankings
- lógica comercial

---

# Arquitectura View

La view consume:

```text
fact_sales
    ↓
dim_date
dim_product
dim_customer
dim_channel
```

---

# Métricas Implementadas

## Métricas Base

| Métrica | Descripción |
|---|---|
| venta_total | ventas monetarias |
| unidades_vendidas | volumen ventas |
| devoluciones | devoluciones comerciales |

---

# KPIs Derivados

## KPIs ejecutivos

| KPI | Descripción |
|---|---|
| pct_devolucion | porcentaje devolución |
| market_share_pct | participación mercado |
| ranking_venta | ranking ventas |

---

# Market Share

La semantic layer implementa cálculo market share.

---

## Objetivo

Permitir analytics competitivos y participación mercado.

---

## Fórmula

```text
venta_marca
/
venta_total
```

---

# Ranking Comercial

La semantic layer implementa rankings automáticos.

---

## Objetivos

- top marcas
- top categorías
- top canales
- analytics ejecutivos

---

# Integración Temporal

La semantic layer consume directamente la dimensión temporal.

---

## Funcionalidades

- analytics mensuales
- comparativos YoY
- tendencias
- Semana Bimbo

---

# Semana Bimbo

La lógica temporal personalizada se integra directamente desde `dim_date`.

## Reglas

| Regla | Valor |
|---|---|
| inicio semana | jueves |
| fin semana | miércoles |

---

# Integración Data Marts

Los marts reutilizan semantic metrics.

---

## Marts consumidores

| Mart | Consumo |
|---|---|
| sales_monthly | métricas temporales |
| brand_performance | market share |
| category_performance | KPIs categorías |
| channel_performance | KPIs canales |

---

# Integración Frontend

La aplicación analytics consume marts construidos sobre semantic layer.

---

## Beneficios

- dashboards rápidos
- KPIs consistentes
- analytics desacoplados
- simplificación frontend

---

# Arquitectura Analytics

La semantic layer habilita:

- dashboards ejecutivos
- heatmaps
- drilldown analytics
- YoY analytics
- executive alerts
- executive insights

---

# Persistencia

La semantic layer opera directamente sobre DuckDB.

---

## Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| DuckDB | engine analytics |
| SQL | business logic |
| Pandas | integración pipeline |

---

# Modularidad

La semantic layer fue diseñada desacoplada.

---

## Beneficios

- mantenibilidad
- reutilización
- escalabilidad
- extensibilidad

---

# Características Enterprise

## Implementado en V3

- semantic abstraction
- reusable KPIs
- business logic layer
- centralized metrics
- executive analytics
- reusable analytics

---

# Performance

La semantic layer optimiza analytics mediante:

- joins centralizados
- KPIs precalculados
- lógica reutilizable
- integración DuckDB

---

# Beneficios Técnicos

## Backend

- menos duplicación lógica
- simplificación marts
- simplificación frontend
- desacoplamiento analytics

---

## Frontend

- dashboards rápidos
- KPIs homogéneos
- insights consistentes
- analytics reutilizables

---

# Estado Semantic Layer

## V3 COMPLETADA

La V3 implementa una semantic layer enterprise desacoplada y reutilizable orientada a analytics modernos y Business Intelligence escalable.