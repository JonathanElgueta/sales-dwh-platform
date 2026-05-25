# SALES DWH PLATFORM — DATA MARTS

Autor: Jonathan Elgueta Elgueta  
Versión: V3.0.0  
Estado: STABLE  
Documento: DATA MARTS  
Última actualización: 2026-05-25  

---

# Descripción

Este documento describe los Data Marts implementados en Sales DWH Platform V3.

Los marts fueron diseñados como capas analíticas especializadas orientadas a dashboards ejecutivos, analytics multidimensional y visual analytics.

---

# Objetivos Data Marts

La arquitectura marts fue diseñada para:

- analytics rápidos
- desacoplar frontend
- reducir complejidad consultas
- reutilización KPIs
- optimizar performance
- soportar dashboards ejecutivos

---

# Arquitectura General

Los marts consumen directamente la semantic layer.

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

- consultas rápidas
- menor complejidad frontend
- desacoplamiento analytics
- performance optimizado
- reutilización métricas

---

## Negocio

- dashboards ejecutivos
- KPIs centralizados
- analytics especializados
- reporting consistente

---

# Marts Implementados

## Sales Monthly

---

### Objetivo

Centralizar métricas temporales agregadas mensualmente.

---

### Grain

```text
1 registro =
1 año
1 mes
```

---

### Métricas

| Métrica | Descripción |
|---|---|
| venta_total | ventas monetarias |
| unidades_vendidas | volumen ventas |
| pct_devolucion | porcentaje devolución |

---

### Uso principal

- tendencias
- comparativos YoY
- executive KPIs
- heatmaps

---

# Brand Performance

---

### Objetivo

Analytics especializados por marca comercial.

---

### Grain

```text
1 registro =
1 marca
1 año
1 mes
```

---

### KPIs implementados

| KPI | Descripción |
|---|---|
| venta_total | ventas marca |
| market_share_pct | participación mercado |
| ranking_venta | ranking marca |
| pct_devolucion | devoluciones marca |

---

### Uso principal

- analytics marcas
- market share
- ranking comercial
- drilldown analytics

---

# Category Performance

---

### Objetivo

Analytics comerciales por categoría producto.

---

### Grain

```text
1 registro =
1 categoría
1 año
1 mes
```

---

### KPIs implementados

| KPI | Descripción |
|---|---|
| venta_total | ventas categoría |
| unidades_vendidas | volumen categoría |
| pct_devolucion | devoluciones categoría |

---

### Uso principal

- top categorías
- category analytics
- treemap analytics
- dashboard ejecutivo

---

# Channel Performance

---

### Objetivo

Analytics comerciales por canal y cadena.

---

### Grain

```text
1 registro =
1 canal
1 cadena
1 año
1 mes
```

---

### KPIs implementados

| KPI | Descripción |
|---|---|
| venta_total | ventas canal |
| unidades_vendidas | volumen canal |
| pct_devolucion | devoluciones canal |

---

### Uso principal

- analytics retail
- analytics canal
- top cadenas
- dashboard ejecutivo

---

# Persistencia Marts

Los marts se almacenan utilizando formato Parquet.

---

## Objetivos

- performance lectura
- persistencia eficiente
- integración analytics
- optimización frontend

---

## Ubicación

```text
data/marts/
```

---

# Integración Frontend

La aplicación Streamlit consume marts directamente.

---

## Beneficios

- dashboards rápidos
- menor consumo memoria
- analytics desacoplados
- queries simplificadas

---

# Integración Semantic Layer

Los marts reutilizan KPIs centralizados.

---

## KPIs reutilizados

- market_share_pct
- ranking_venta
- pct_devolucion

---

# Arquitectura Analytics

Los marts habilitan:

- dashboards ejecutivos
- heatmaps
- YoY analytics
- drilldown analytics
- executive insights
- trend analytics

---

# Pipeline Marts

La generación marts forma parte pipeline principal.

---

## Flujo

```text
Semantic Layer
        ↓
Build Marts
        ↓
Persistencia Parquet
        ↓
Frontend Analytics
```

---

# Modularidad

Cada mart fue construido desacoplado.

---

## Beneficios

- mantenibilidad
- extensibilidad
- reutilización
- escalabilidad

---

# Performance

La V3 optimiza analytics mediante marts agregados.

---

## Estrategias implementadas

- agregaciones precalculadas
- parquet persistence
- marts especializados
- desacoplamiento frontend

---

# Beneficios Técnicos

## Backend

- simplificación analytics
- menor complejidad consultas
- desacoplamiento capas
- reutilización métricas

---

## Frontend

- dashboards rápidos
- menor tiempo carga
- visual analytics eficientes
- menor consumo RAM

---

# Características Enterprise

## Implementado en V3

- marts desacoplados
- reusable analytics
- executive marts
- analytics optimization
- parquet analytics layer

---

# Estado Data Marts

## V3 COMPLETADA

La V3 implementa una arquitectura Data Marts enterprise desacoplada, reutilizable y optimizada para analytics ejecutivos modernos.