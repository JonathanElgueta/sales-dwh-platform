# SALES DWH PLATFORM — PIPELINE

Autor: Jonathan Elgueta Elgueta  
Versión: V3.0.0  
Estado: STABLE  
Documento: ETL PIPELINE  
Última actualización: 2026-05-25  

---

# Descripción

Este documento describe el pipeline ETL implementado en Sales DWH Platform V3.

La solución implementa procesamiento incremental, transformaciones analíticas, carga dimensional y persistencia analítica utilizando arquitectura modular.

---

# Objetivos Pipeline

La arquitectura ETL fue diseñada para:

- automatización procesamiento
- desacoplamiento etapas
- incremental loading
- persistencia analítica
- reutilización datos
- QA validations
- escalabilidad

---

# Arquitectura Pipeline

El pipeline implementa múltiples capas de procesamiento:

```text
RAW FILES
    ↓
EXTRACT
    ↓
TRANSFORM
    ↓
WAREHOUSE LOAD
    ↓
SEMANTIC LAYER
    ↓
DATA MARTS
    ↓
ANALYTICS APP
```

---

# Flujo General

## Secuencia procesamiento

1. extracción archivos XLSX
2. transformación datos
3. generación dimensiones
4. carga fact table
5. generación semantic layer
6. construcción marts
7. validaciones QA
8. consumo analytics app

---

# Extract Layer

La capa extract procesa archivos fuente.

---

## Objetivos

- lectura XLSX
- validación inicial
- normalización básica
- generación DataFrames

---

## Tecnologías

| Tecnología | Uso |
|---|---|
| Python | procesamiento |
| Pandas | lectura datos |
| OpenPyXL | integración Excel |

---

# Transform Layer

La capa transform implementa lógica negocio y limpieza.

---

## Procesos implementados

### Limpieza

- null handling
- normalización texto
- tipificación columnas

---

### Enriquecimiento

- cálculo métricas
- generación KPIs
- lógica Semana Bimbo
- business transformations

---

### Integridad

- eliminación duplicados
- validaciones consistencia
- integridad dimensional

---

# Incremental Loading

La V3 implementa procesamiento incremental.

---

## Objetivos

- reducir tiempo procesamiento
- evitar recargas completas
- optimizar performance
- soportar escalabilidad

---

## Beneficios

| Beneficio | Resultado |
|---|---|
| menor tiempo carga | performance |
| menor consumo recursos | eficiencia |
| procesamiento parcial | escalabilidad |

---

# Data Warehouse Load

La carga warehouse utiliza DuckDB como motor central.

---

## Objetivos

- persistencia analítica
- consultas rápidas
- procesamiento columnar
- centralización datos

---

## Tablas implementadas

### Fact Table

```text
fact_sales
```

### Dimensiones

```text
dim_date
dim_product
dim_customer
dim_channel
```

---

# Dimensión Temporal

## Semana Bimbo

La dimensión temporal implementa lógica comercial personalizada.

### Reglas

| Regla | Valor |
|---|---|
| inicio semana | jueves |
| fin semana | miércoles |

---

# Semantic Layer Generation

La semantic layer encapsula lógica analítica.

---

## Objetivos

- centralización KPIs
- business logic layer
- desacoplamiento analytics
- simplificación reporting

---

## View implementada

```text
vw_sales_enriched
```

---

## KPIs calculados

- market_share_pct
- ranking_venta
- pct_devolucion

---

# Data Marts Generation

Los marts permiten analytics especializados.

---

## Marts implementados

| Mart | Objetivo |
|---|---|
| sales_monthly | métricas temporales |
| brand_performance | analytics marcas |
| category_performance | analytics categorías |
| channel_performance | analytics canales |

---

# Persistencia

La plataforma utiliza múltiples mecanismos persistencia.

---

## Formatos implementados

| Formato | Uso |
|---|---|
| XLSX | raw source |
| DuckDB | warehouse |
| Parquet | marts analytics |

---

# Orquestación Pipeline

El pipeline principal centraliza ejecución completa.

---

## Script principal

```text
run_pipeline.py
```

---

## Responsabilidades

- ejecutar ETL
- construir warehouse
- generar semantic layer
- construir marts
- ejecutar QA

---

# Metadata Tracking

La solución incorpora metadata operacional.

---

## Objetivos

- auditoría procesamiento
- tracking ejecuciones
- monitoreo pipeline

---

# QA Layer

La V3 implementa validaciones automáticas.

---

## Validaciones implementadas

- null checks
- duplicate checks
- integridad facts
- integridad dimensiones
- validación temporal
- validación Semana Bimbo

---

# Arquitectura Modular

La solución implementa desacoplamiento por módulos.

---

## Estructura

```text
src/

├── pipeline/
├── warehouse/
├── semantic/
├── marts/
└── qa/
```

---

# Performance

La V3 fue optimizada para analytics rápidos.

---

## Estrategias implementadas

- DuckDB columnar engine
- parquet persistence
- incremental loading
- marts agregados
- semantic abstraction

---

# Beneficios Pipeline

## Técnicos

- desacoplamiento
- mantenibilidad
- escalabilidad
- performance
- modularidad

---

## Negocio

- analytics rápidos
- monitoreo operacional
- KPIs centralizados
- reporting consistente

---

# Características Enterprise

## Implementado V3

- incremental ETL
- semantic layer
- marts desacoplados
- QA automation
- monitoring layer
- parquet persistence
- modular architecture

---

# Estado Pipeline

## V3 COMPLETADA

La V3 implementa un pipeline ETL enterprise modular, incremental y escalable orientado a plataformas analíticas modernas.