# SALES DWH PLATFORM — INCREMENTAL ARCHITECTURE

Autor: Jonathan Elgueta Elgueta
Versión: V4.0.0
Estado: STABLE
Documento: INCREMENTAL ARCHITECTURE
Última actualización: 2026-05-26

---

# Descripción

Este documento describe la arquitectura incremental enterprise implementada en Sales DWH Platform V4.

La V4 consolida oficialmente un modelo de ingestión incremental desacoplado capaz de:

- procesar nuevos archivos XLSX
- mantener histórico persistente
- actualizar particiones warehouse
- refrescar semantic layer
- regenerar marts automáticamente
- mantener dashboards sincronizados

---

# Objetivo

La arquitectura incremental fue diseñada para:

- evitar rebuilds completos innecesarios
- soportar crecimiento multi-año
- mantener performance enterprise
- habilitar refresh operacional
- preservar granularidad diaria
- soportar governance enterprise

---

# Arquitectura Incremental

```text
NEW XLSX FILE
    ↓
QA VALIDATION
    ↓
SCHEMA NORMALIZATION
    ↓
PARTITION UPDATE
    ↓
SEMANTIC REFRESH
    ↓
MART REGENERATION
    ↓
CACHE REFRESH
    ↓
DASHBOARD UPDATE
```

---

# Principio Oficial

## Regla Principal

```text
EL HISTÓRICO NUNCA SE REPROCESA COMPLETAMENTE
```

---

# Estrategia Enterprise

La V4 implementa:

```text
PARTITION-BASED INCREMENTAL PROCESSING
```

---

# Beneficios

- menor consumo memoria
- menor tiempo procesamiento
- escalabilidad enterprise
- refresh desacoplado

---

# Arquitectura Warehouse

La arquitectura incremental opera sobre:

```text
PARTITIONED FACT WAREHOUSE
```

---

# Particionamiento Oficial

```text
year=YYYY/month=MM
```

---

# Ejemplo

```text
data/warehouse/facts/sales/year=2026/month=05/data.parquet
```

---

# Flujo Incremental Enterprise

```text
UPLOAD XLSX
    ↓
VALIDATE FILE
    ↓
NORMALIZE SCHEMA
    ↓
IDENTIFY PARTITION
    ↓
UPDATE PARTITION
    ↓
REFRESH SEMANTIC LAYER
    ↓
REBUILD MARTS
    ↓
REFRESH APP
```

---

# Incremental Loader

Componente principal:

```text
incremental_loader.py
```

---

# Responsabilidades

- cargar XLSX
- ejecutar QA
- normalizar columnas
- actualizar warehouse
- disparar refresh marts

---

# Warehouse Loader

Componente responsable de:

```text
warehouse_loader.py
```

---

# Objetivos

- actualizar particiones
- preservar histórico
- mantener granularidad diaria

---

# Estrategia Update

La actualización ocurre por:

```text
year/month
```

---

# Ejemplo

Si se carga:

```text
2026_05.xlsx
```

El sistema actualiza:

```text
year=2026/month=05
```

sin afectar otras particiones.

---

# Beneficio Principal

```text
AISLAMIENTO HISTÓRICO
```

---

# Granularidad

La arquitectura incremental preserva:

```text
GRANULARIDAD DIARIA
```

---

# Beneficios Granularidad

- freshness real
- monitoreo operacional
- análisis transaccional
- forecasting futuro

---

# Integración QA

La arquitectura incremental incorpora:

```text
QA BEFORE LOAD
```

---

# Flujo QA

```text
NEW FILE
    ↓
QA ENGINE
    ↓
PASS / FAIL
    ↓
WAREHOUSE UPDATE
```

---

# Objetivo

Garantizar:

- integridad histórica
- consistencia warehouse
- estabilidad dashboards

---

# Integración Semantic Layer

Posterior al warehouse update:

```text
FACTS + DIMENSIONS
```

alimentan:

```sql
vw_sales_enriched
```

---

# Objetivo

Centralizar:

- joins
- enriquecimiento
- business logic

---

# Integración Data Marts

Luego del semantic refresh:

```python
generate_all_marts()
```

---

# Arquitectura Marts

```text
SEMANTIC LAYER
    ↓
DATA MARTS
```

---

# Regla Oficial

```text
LOS MARTS NUNCA LEEN FACTS DIRECTAMENTE
```

---

# Refresh Application

Posteriormente:

```python
st.cache_data.clear()
```

---

# Objetivo

- refrescar dashboards
- evitar stale data
- sincronizar frontend

---

# Dashboard Update

Finalmente:

```text
STREAMLIT RERUN
```

actualiza la plataforma completa.

---

# Rebuild Histórico

La V4 incorporó:

```text
FULL HISTORICAL REBUILD
```

---

# Resultado Oficial

```text
2023 → 2026
```

Más de:

```text
7.5M registros
```

reconstruidos exitosamente.

---

# Arquitectura Enterprise

```text
RAW XLSX
    ↓
INCREMENTAL PIPELINE
    ↓
PARTITIONED WAREHOUSE
    ↓
SEMANTIC LAYER
    ↓
DATA MARTS
    ↓
ANALYTICS APP
```

---

# Operational Monitoring

La arquitectura incremental habilita:

- monitoreo pipeline
- freshness diario
- tracking cargas
- observabilidad enterprise

---

# Audit Logging

Cada incremental registra:

- usuario
- archivo
- filas procesadas
- timestamp
- estado
- mensaje ejecución

---

# Beneficios Arquitectónicos

## Escalabilidad

- crecimiento multi-año
- warehouse enterprise
- incremental real

---

## Performance

- particiones aisladas
- menor lectura
- refresh optimizado

---

## Gobernanza

- auditabilidad
- trazabilidad
- observabilidad

---

## Mantenibilidad

- desacoplamiento
- modularidad
- arquitectura limpia

---

# Reglas Oficiales Incremental

## Regla 1

```text
SOLO SE ACTUALIZA LA PARTICIÓN AFECTADA
```

---

## Regla 2

```text
EL HISTÓRICO SE PRESERVA
```

---

## Regla 3

```text
SEMANTIC LAYER CENTRALIZA JOINS
```

---

## Regla 4

```text
MARTS NACEN DESDE SEMANTIC LAYER
```

---

## Regla 5

```text
LA APP SOLO CONSUME MARTS
```

---

# Consolidación V4

La V4 consolida oficialmente:

- Incremental ETL enterprise
- Warehouse particionado
- Refresh desacoplado
- Historical persistence
- Granularidad diaria
- Governance operational

---

# Estado Incremental Architecture

## V4 COMPLETADA

Estado oficial:

```text
STABLE
```

---