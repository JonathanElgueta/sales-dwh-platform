# SALES DWH - Arquitectura V1

Autor: Jonathan Elgueta Elgueta  
Versión: V1.0.0  
Fecha: 2026-05-23

---

## Descripción

Este documento describe la arquitectura original V1 del proyecto Sales Data Warehouse.

La versión V1 representa la primera implementación funcional del pipeline de ventas,
basada en procesamiento batch completo utilizando parquet y DuckDB.

---

# Objetivo Inicial

El objetivo inicial del proyecto fue:

- consolidar ventas comerciales
- construir primeras dimensiones
- habilitar análisis comerciales
- generar marts analíticos
- implementar semantic layer básica

---

# Arquitectura General V1

RAW XLSX
    ↓

ETL TRANSFORMATION
    ↓

PARQUET STORAGE
    ↓

DUCKDB VIEW
    ↓

ANALYTICAL MARTS

---

# Componentes V1

## 1. RAW XLSX

Ubicación:

data/raw/sales/

Responsabilidad:

- almacenar archivos originales
- representar fuente negocio

Ejemplo:

data sell in total (2026_05).xlsx

---

## 2. Transformation Layer

Ubicación:

src/transformation/

Responsabilidad:

- transformar XLSX
- construir dimensiones
- generar parquet

Scripts principales:

- sales_etl_to_parquet.py
- products_etl.py
- agencies_etl.py
- build_dim_date.py

---

## 3. Parquet Layer

Ubicación:

data/parquet/

Responsabilidad:

- almacenamiento parquet V1
- facts y dimensiones

Estructura:

- parquet plano
- sin particionado enterprise

---

## 4. Semantic Layer Inicial

Vista principal:

vw_sales_enriched

Responsabilidad:

- centralizar joins
- enriquecer ventas
- habilitar marts

Implementación inicial:

src/analytics/create_views.py

---

## 5. Analytical Marts

Ubicación:

data/marts/

Primeros marts implementados:

- ventas mensuales
- performance marcas
- ventas semana bimbo
- categorías
- canales

---

# Semana Bimbo

V1 incorpora lógica comercial personalizada denominada:

Semana Bimbo

Características:

- inicio jueves
- cierre miércoles

Integrada inicialmente en:

- dim_date
- semantic layer
- marts semanales

---

# Limitaciones Arquitectónicas V1

A medida que el volumen y complejidad crecieron,
se identificaron limitaciones importantes.

---

## 1. Full Reload

Cada ejecución reprocesaba:

TODO el histórico completo.

Impacto:

- alto tiempo procesamiento
- baja escalabilidad
- alto costo operacional

---

## 2. Sin Metadata Operacional

V1 no poseía:

- control ACTIVE/CLOSED
- control incremental
- tracking operacional

---

## 3. Storage No Particionado

La capa parquet utilizaba:

- almacenamiento plano
- sin particionado por período

Impacto:

- menor performance
- difícil incremental
- recovery complejo

---

## 4. Arquitectura Parcialmente Monolítica

Algunos componentes se encontraban mezclados:

- QA en analytics
- semantic mezclado con analytics
- orchestration inexistente

---

## 5. Recovery Limitado

Ante errores:

- recovery complejo
- reproceso total requerido
- alto impacto operacional

---

# Valor de V1

A pesar de sus limitaciones,
V1 fue fundamental para:

- validar modelo dimensional
- construir semantic layer
- desarrollar marts
- validar lógica negocio
- implementar semana bimbo

---

# Evolución hacia V2

Las limitaciones identificadas en V1 impulsaron la creación de V2.

Principales motivadores:

- incremental processing
- warehouse particionado
- metadata layer
- orchestration
- desacoplamiento arquitectónico

---

# Legado V1

En V2, la carpeta:

data/parquet/

queda marcada como:

LEGACY V1 LAYER

Se mantiene temporalmente para:

- rollback
- recuperación
- trazabilidad histórica

---

# Comparación Arquitectónica

| V1 | V2 |
|---|---|
| Full reload | Incremental |
| Parquet plano | Warehouse particionado |
| Sin metadata | Metadata layer |
| Arquitectura parcial | Arquitectura modular |
| Recovery complejo | Recovery simplificado |

---

# Estado Final

V1 queda oficialmente reemplazada por:

V2.0.0

---

# Importancia Histórica

V1 representa la base fundacional del proyecto Sales Data Warehouse.

Permitió validar:

- modelo de negocio
- semantic layer
- marts analíticos
- estrategia dimensional
- lógica comercial semana bimbo

Sin V1 no habría sido posible evolucionar hacia la arquitectura enterprise V2.