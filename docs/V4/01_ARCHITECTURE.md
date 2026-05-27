# SALES DWH PLATFORM — ARCHITECTURE

Autor: Jonathan Elgueta Elgueta
Versión: V4.0.0
Estado: STABLE
Documento: ARQUITECTURA TÉCNICA
Última actualización: 2026-05-26

---

# Descripción

Este documento describe la arquitectura técnica completa implementada en Sales DWH Platform V4.

La solución evolucionó hacia una arquitectura empresarial desacoplada basada en:

- Data Warehouse Particionado
- Modelo Dimensional
- Semantic Layer
- Data Marts
- Incremental ETL
- Enterprise Analytics

La V4 representa la consolidación oficial de la arquitectura enterprise de Sales DWH Platform.

---

# Objetivos Arquitectónicos

La arquitectura V4 fue diseñada para:

- soportar cargas incrementales empresariales
- mantener histórico completo de ventas
- escalar mediante particionamiento
- desacoplar facts y dimensiones
- centralizar joins analíticos
- separar lógica semántica de dashboards
- habilitar granularidad diaria
- soportar IA y analítica avanzada

---

# Arquitectura General

La plataforma implementa una arquitectura analítica multicapa empresarial:

```text
RAW XLSX FILES
    ↓
INCREMENTAL ETL PIPELINE
    ↓
PARTITIONED DATA WAREHOUSE
    ↓
DIMENSIONAL MODEL
    ↓
SEMANTIC LAYER (DuckDB Views)
    ↓
ANALYTICS DATA MARTS
    ↓
ENTERPRISE ANALYTICS APPLICATION
```

---

# Arquitectura Conceptual

```text
RAW
→ ingestión incremental

WAREHOUSE
→ facts particionados por year/month

DIMENSIONS
→ producto / agencia / fecha

SEMANTIC LAYER
→ joins enriquecidos y lógica analítica

MARTS
→ agregaciones optimizadas para dashboards

APPLICATION
→ visualización ejecutiva + IA + QA + pipeline ops
```

---

# Principios Arquitectónicos

La V4 implementa principios enterprise de desacoplamiento y escalabilidad.

---

## 1. FACT TABLES

Los facts almacenan únicamente:

- transacciones crudas
- granularidad diaria
- información operacional
- métricas transaccionales

Los facts NO contienen:

- joins
- KPIs derivados
- enriquecimiento dimensional
- lógica de negocio
- market share
- rankings

---

## 2. DIMENSIONS

Las dimensiones contienen:

- atributos empresariales
- metadata analítica
- jerarquías
- categorización de negocio

Dimensiones oficiales:

| Dimensión | Propósito |
|---|---|
| dim_producto | Master data productos |
| dim_agencia | Master data agencias |
| dim_date | Inteligencia calendario |

---

## 3. SEMANTIC LAYER

La Semantic Layer es el único lugar autorizado para:

- joins
- enriquecimiento
- lógica analítica
- consolidación empresarial

La semantic layer centraliza completamente:

```text
FACTS + DIMENSIONS
```

Vista principal:

```sql
vw_sales_enriched
```

---

## 4. DATA MARTS

Los marts consumen SIEMPRE:

```text
Semantic Layer
```

Los marts NUNCA:

- leen facts directamente
- realizan joins
- duplican lógica semántica

Objetivos:

- performance dashboards
- agregaciones
- KPIs ejecutivos
- consumo rápido

---

## 5. APPLICATION

La aplicación Streamlit consume únicamente marts optimizados.

Responsabilidades:

- visualización ejecutiva
- monitoreo operacional
- forecasting
- anomaly detection
- governance
- QA monitoring

---

# Arquitectura Oficial V4

```text
RAW XLSX
→ Incremental Loader
→ FACT Warehouse (crudo particionado)

FACT + DIMENSIONS
→ Semantic Layer (DuckDB Views)

Semantic Layer
→ Analytics Data Marts

Data Marts
→ Enterprise Analytics App
```

---

# Flujo Empresarial V4

```text
XLSX FILE
    ↓
QA VALIDATION
    ↓
SCHEMA MAPPING
    ↓
FACT PARTITION UPDATE
    ↓
SEMANTIC REFRESH
    ↓
MART REGENERATION
    ↓
DASHBOARD REFRESH
```

---

# Particionamiento Enterprise

La V4 introduce warehouse particionado empresarial.

Estrategia oficial:

```text
year=YYYY/month=MM
```

Ejemplo:

```text
data/warehouse/facts/sales/year=2026/month=05/data.parquet
```

---

# Beneficios Arquitectónicos

## Escalabilidad

- soporte multi-año
- crecimiento incremental
- menor consumo memoria

---

## Performance

- lectura optimizada
- scans reducidos
- marts desacoplados

---

## Gobernanza

- trazabilidad
- auditabilidad
- QA centralizado

---

## Mantenibilidad

- separación de responsabilidades
- modularidad
- desacoplamiento enterprise

---

## Analítica Avanzada

La arquitectura habilita:

- AI Forecasting
- anomaly detection
- semantic metrics
- enterprise KPIs
- operational monitoring

---

# Estructura Empresarial

```text
sales-dwh/
│
├── data/
│   │
│   ├── raw/
│   │   └── sales/
│   │
│   ├── warehouse/
│   │   │
│   │   ├── facts/
│   │   │   └── sales/
│   │   │       └── year=YYYY/month=MM/
│   │   │
│   │   └── dimensions/
│   │       ├── products/
│   │       ├── agencies/
│   │       └── date/
│   │
│   ├── duckdb/
│   │   └── sales_dwh.duckdb
│   │
│   ├── marts/
│   │
│   ├── metadata/
│   │
│   └── logs/
│
├── src/
│   ├── app/
│   ├── config/
│   └── services/
│
└── outputs/
```

---

# Separación Oficial de Capas

## RAW LAYER

Contiene:

- XLSX originales
- archivos fuente
- ingestión operacional

Ruta:

```text
data/raw/sales
```

---

## WAREHOUSE LAYER

Contiene:

- facts particionados
- almacenamiento enterprise
- histórico persistente

Ruta:

```text
data/warehouse
```

---

## DIMENSIONAL LAYER

Contiene:

- dimensiones empresariales
- metadata analítica
- entidades maestras

---

## SEMANTIC LAYER

Contiene:

- joins
- lógica empresarial
- vistas analíticas

Motor:

```text
DuckDB
```

---

## MART LAYER

Contiene:

- agregaciones optimizadas
- datasets dashboards
- KPIs empresariales

Ruta:

```text
data/marts
```

---

## APPLICATION LAYER

Contiene:

- dashboards
- IA
- monitoreo
- operaciones

Framework:

```text
Streamlit
```

---

# Reglas Oficiales V4

## Regla 1

```text
FACTS = CRUDO
```

---

## Regla 2

```text
DIMENSIONS = ATRIBUTOS
```

---

## Regla 3

```text
SEMANTIC LAYER = JOINS + BUSINESS LOGIC
```

---

## Regla 4

```text
MARTS = AGREGACIONES
```

---

## Regla 5

```text
APP = CONSUMO FINAL
```

---

# Consolidación Arquitectónica

La V4 consolida oficialmente:

- Incremental ETL
- Warehouse empresarial
- Modelo dimensional
- Semantic Layer
- Data Marts desacoplados
- Granularidad diaria
- Enterprise governance
- Plataforma analítica empresarial

---

# Estado Arquitectura

## V4 COMPLETADA

La V4 representa la primera versión enterprise completamente desacoplada de Sales DWH Platform.

Estado oficial:

```text
STABLE
```

---