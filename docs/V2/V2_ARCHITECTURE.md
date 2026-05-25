# SALES DWH - Arquitectura V2

Autor: Jonathan Elgueta Elgueta  
Versión: V2.0.0  
Fecha: 2026-05-23

---

## Descripción

Este documento describe la arquitectura funcional y operacional de la versión V2 del proyecto Sales Data Warehouse.

La arquitectura V2 fue diseñada bajo principios de:

- desacoplamiento
- procesamiento incremental
- almacenamiento particionado
- semantic layer
- modularidad enterprise

---

# Objetivo del Proyecto

Construir un Data Warehouse moderno para procesamiento incremental de ventas,
permitiendo análisis comerciales eficientes mediante una arquitectura desacoplada y escalable.

---

# Arquitectura General

RAW XLSX
    ↓

METADATA LAYER
    ↓

INCREMENTAL ORCHESTRATION
    ↓

WAREHOUSE PARTITIONED
    ↓

SEMANTIC LAYER
    ↓

MARTS ANALÍTICOS
    ↓

QA / ANALYTICS

---

# Componentes Arquitectónicos

## 1. RAW LAYER

Ubicación:

data/raw/sales/

Responsabilidad:

- almacenar archivos XLSX originales
- representar la fuente oficial del negocio
- mantener histórico de ingestión

Ejemplo:

- data sell in total (2026_05).xlsx

---

## 2. METADATA LAYER

Ubicación:

data/metadata/

Archivo principal:

- processed_files.parquet

Responsabilidad:

- controlar períodos procesados
- identificar período ACTIVE
- habilitar incremental processing
- controlar planificación operacional

Campos principales:

- file_name
- period
- status
- processed_at
- warehouse_partition

Estados:

- CLOSED
- ACTIVE

---

## 3. ORCHESTRATION LAYER

Ubicación:

src/orchestration/

Responsabilidad:

- validar metadata
- planificar incremental
- ejecutar overwrite particionado
- controlar pipeline operacional

Scripts principales:

- initialize_metadata.py
- validate_metadata.py
- plan_incremental_load.py
- execute_incremental_load.py

---

# Estrategia Incremental

La arquitectura V2 implementa incremental overwrite por partición.

Regla principal:

- períodos CLOSED nunca se reprocesan
- período ACTIVE siempre se reprocesa completamente

Ejemplo:

2026_05 → ACTIVE

Proceso:

1. eliminar partición existente
2. reprocesar XLSX
3. recrear parquet particionado
4. actualizar metadata

Beneficios:

- simplicidad operacional
- bajo riesgo
- fácil recuperación
- alta mantenibilidad

---

## 4. WAREHOUSE LAYER

Ubicación:

data/warehouse/

Responsabilidad:

- almacenamiento analítico oficial
- facts particionados
- dimensiones desacopladas

---

# Facts

Ubicación:

warehouse/facts/sales/

Particionado:

- year
- month

Ejemplo:

warehouse/facts/sales/year=2026/month=05/

Beneficios:

- partition pruning
- incremental overwrite
- performance optimizada
- aislamiento de períodos

---

# Dimensions

Ubicación:

warehouse/dimensions/

Dimensiones actuales:

- dim_producto
- dim_agencia
- dim_date

---

## 5. SEMANTIC LAYER

Ubicación:

src/semantic/

Script principal:

- create_views.py

Responsabilidad:

- desacoplar marts del storage físico
- centralizar joins
- generar vista analítica única

Vista principal:

- vw_sales_enriched

Beneficios:

- desacoplamiento completo
- flexibilidad arquitectónica
- mantenimiento simplificado

---

## 6. MARTS LAYER

Ubicación:

data/marts/

Responsabilidad:

- consumo analítico
- KPIs comerciales
- agregaciones optimizadas

Marts actuales:

- mart_sales_monthly
- mart_brand_performance
- mart_sales_weekly_bimbo
- mart_category_performance
- mart_channel_performance

---

## 7. QA LAYER

Ubicación:

src/qa/

Responsabilidad:

- validación operacional
- control de calidad
- validación dimensional
- validación financiera

Validaciones actuales:

- duplicados
- nulos
- integridad dimensional
- semana bimbo
- métricas financieras

---

# Semana Bimbo

La dimensión calendario incorpora lógica especial denominada:

Semana Bimbo

Características:

- inicia jueves
- finaliza miércoles

Esto permite alineamiento con lógica comercial del negocio.

---

# Principales Mejoras V2

Comparado con V1:

| V1 | V2 |
|---|---|
| Full reload | Incremental |
| Parquet plano | Warehouse particionado |
| Sin metadata | Metadata layer |
| ETL monolítico | Arquitectura modular |
| Sin semantic layer | Semantic desacoplada |
| Bajo control operacional | Pipeline enterprise |

---

# Beneficios Arquitectónicos

La arquitectura V2 entrega:

- escalabilidad
- desacoplamiento
- mantenibilidad
- procesamiento incremental
- modularidad
- recovery simplificado
- QA operacional

---

# Estado Actual

Versión:

V2 Stable

Estado Operacional:

- Warehouse Operacional
- Incremental Activo
- Semantic Layer Estable
- Marts Productivos
- QA Validado

---

# Próximas Mejoras Futuras

Posibles evoluciones V3:

- orchestrator master
- logging centralizado
- monitoreo operacional
- parallel processing
- CI/CD
- cloud migration
- API serving