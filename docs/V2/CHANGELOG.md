# SALES DWH - CHANGELOG

Autor: Jonathan Elgueta Elgueta

---

# V2.0.0 - 2026-05-23

## Estado

VERSIÓN ESTABLE

---

# Resumen

La versión V2 representa una evolución completa de arquitectura para el proyecto Sales Data Warehouse.

Se migra desde una arquitectura ETL monolítica basada en parquet simple hacia una plataforma incremental desacoplada con warehouse particionado y metadata operacional.

---

# Principales Cambios Arquitectónicos

## Nuevo Warehouse V2

Se implementa nueva capa:

data/warehouse/

Características:

- almacenamiento particionado
- separación facts/dimensions
- estructura enterprise

---

## Particionado de Facts

Las ventas ahora se almacenan particionadas por:

- year
- month

Ejemplo:

warehouse/facts/sales/year=2026/month=05/

Beneficios:

- incremental overwrite
- partition pruning
- mejor performance
- aislamiento histórico

---

## Metadata Layer

Nueva capa:

data/metadata/

Archivo principal:

processed_files.parquet

Funcionalidades:

- control de períodos
- identificación ACTIVE
- control incremental
- orchestration metadata

---

## Incremental Processing

Nueva arquitectura incremental implementada.

Reglas:

- períodos CLOSED → SKIP
- período ACTIVE → REPROCESS

Beneficios:

- menor tiempo procesamiento
- menor riesgo operacional
- recovery simplificado

---

## Semantic Layer

Nueva capa:

src/semantic/

Vista principal:

vw_sales_enriched

Beneficios:

- desacoplamiento marts/storage
- joins centralizados
- mantenimiento simplificado

---

## Nueva Organización SRC

Reorganización completa de carpetas:

- semantic/
- marts/
- orchestration/
- migrations/
- qa/

Arquitectura modular enterprise.

---

## Migración Warehouse

Se implementa script histórico:

migrate_to_warehouse.py

Responsabilidad:

- migración V1 → V2
- construcción warehouse particionado

---

## QA Operacional

Se consolida capa QA:

src/qa/

Validaciones:

- duplicados
- nulos
- integridad dimensional
- validación financiera
- semana bimbo

---

## Semana Bimbo

Se implementa lógica calendario comercial:

- inicio jueves
- cierre miércoles

Integrada en:

- dim_date
- marts semanales
- semantic layer

---

# Marts Analíticos V2

Nuevos marts:

- mart_sales_monthly
- mart_brand_performance
- mart_sales_weekly_bimbo
- mart_category_performance
- mart_channel_performance

---

# Estado Final V2

Componentes operacionales:

- Warehouse
- Incremental
- Semantic Layer
- Marts
- QA
- Metadata Layer

---

# Validaciones Exitosas

Smoke tests ejecutados exitosamente:

- semantic layer
- marts
- QA sales
- QA date
- metadata validation
- incremental planning
- incremental execution

---

# Mejoras Técnicas Clave

## V1

- full reload
- parquet plano
- ETL monolítico
- sin metadata
- sin orchestration

---

## V2

- incremental processing
- warehouse particionado
- metadata-driven orchestration
- semantic desacoplado
- arquitectura modular

---

# Compatibilidad

V2 mantiene compatibilidad lógica con:

- marts históricos
- KPIs comerciales
- semantic queries

---

# Próximas Mejoras Futuras (V3)

Roadmap preliminar:

- master orchestrator
- scheduler automático
- logging centralizado
- monitoreo operacional
- alertas automáticas
- CI/CD
- cloud migration

---

# Estado Oficial

V2.0.0

ESTABLE Y VALIDADO