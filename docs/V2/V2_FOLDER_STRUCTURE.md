# SALES DWH - Estructura de Carpetas V2

Autor: Jonathan Elgueta Elgueta  
Versión: V2.0.0  
Fecha: 2026-05-23

---

## Descripción

Este documento describe la arquitectura oficial de carpetas para la versión V2 del proyecto Sales Data Warehouse.

La versión V2 introduce:

- procesamiento incremental
- warehouse particionado
- metadata operacional
- semantic layer desacoplada
- arquitectura modular enterprise

---

# Estructura General del Proyecto

sales-dwh/

├── data/
│
│   ├── raw/
│   │   └── sales/
│   │
│   ├── warehouse/
│   │
│   │   ├── dimensions/
│   │   │
│   │   │   ├── agencies/
│   │   │   ├── date/
│   │   │   └── products/
│   │   │
│   │   └── facts/
│   │       └── sales/
│   │
│   ├── marts/
│   │
│   ├── metadata/
│   │
│   ├── duckdb/
│   │
│   └── parquet/
│       └── LEGACY V1 LAYER
│
├── docs/
│
├── outputs/
│
├── src/
│
│   ├── analytics/
│   │
│   ├── config/
│   │
│   ├── marts/
│   │
│   ├── migrations/
│   │
│   ├── orchestration/
│   │
│   ├── profiling/
│   │
│   ├── qa/
│   │
│   ├── semantic/
│   │
│   ├── transformation/
│   │
│   └── warehouse/
│
└── venv/

---

# Responsabilidad de Carpetas

## data/raw

Contiene los archivos originales XLSX provenientes del negocio.

Ejemplo:

- data sell in total (2026_05).xlsx

Esta capa representa la fuente oficial de ingestión del sistema.

---

## data/warehouse

Capa oficial de almacenamiento V2.

Contiene:

- tablas fact particionadas
- dimensiones analíticas

### Facts

Las ventas se almacenan particionadas por:

- year
- month

Ejemplo:

warehouse/facts/sales/year=2026/month=05/

### Dimensions

Contiene:

- dim_producto
- dim_agencia
- dim_date

---

## data/marts

Contiene marts analíticos para consumo BI y KPIs.

Ejemplos:

- mart_sales_monthly
- mart_brand_performance
- mart_sales_weekly_bimbo

---

## data/metadata

Capa operacional de metadata.

Contiene:

- processed_files.parquet

Se utiliza para:

- planificación incremental
- detección de período activo
- control operacional

---

## data/duckdb

Contiene la base DuckDB del proyecto.

Incluye:

- semantic layer
- vistas analíticas

---

## data/parquet

Capa legacy V1.

Fue reemplazada por warehouse en V2.

Se mantiene temporalmente para recuperación y rollback.

---

# Responsabilidad de Carpetas SRC

## analytics

Scripts de análisis exploratorio y KPIs comerciales.

---

## config

Configuración centralizada del proyecto.

---

## marts

Construcción de marts analíticos.

---

## migrations

Scripts históricos de migración arquitectónica.

---

## orchestration

Orquestación del pipeline incremental.

---

## profiling

Exploración y profiling de datos fuente.

---

## qa

Validaciones de calidad y QA operacional.

---

## semantic

Capa semántica y vistas de negocio.

---

## transformation

Procesos ETL y transformaciones.

---

# Principales Mejoras V2

Comparado con V1:

- procesamiento incremental
- overwrite por partición
- metadata-driven orchestration
- warehouse particionado
- desacoplamiento semantic layer
- arquitectura enterprise modular

---

# Estado Actual

Versión: V2 Stable

Estado Arquitectura:

- Warehouse Operacional
- Incremental Habilitado
- Semantic Layer Estable
- Marts Operacionales
- QA Validado