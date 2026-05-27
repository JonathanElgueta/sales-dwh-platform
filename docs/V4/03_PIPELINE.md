# SALES DWH PLATFORM — PIPELINE

Autor: Jonathan Elgueta Elgueta
Versión: V4.0.0
Estado: STABLE
Documento: ENTERPRISE PIPELINE
Última actualización: 2026-05-26

---

# Descripción

Este documento describe la arquitectura pipeline implementada en Sales DWH Platform V4.

La V4 consolida oficialmente un pipeline incremental enterprise capaz de:

- procesar archivos XLSX incrementales
- mantener histórico completo
- actualizar warehouse particionado
- refrescar semantic layer
- regenerar marts analíticos
- refrescar dashboards automáticamente

---

# Arquitectura Pipeline

```text
XLSX FILE
    ↓
QA VALIDATION
    ↓
SCHEMA MAPPING
    ↓
FACT WAREHOUSE UPDATE
    ↓
SEMANTIC LAYER REFRESH
    ↓
DATA MART REGENERATION
    ↓
CACHE REFRESH
    ↓
DASHBOARD UPDATE
```

---

# Objetivos Pipeline V4

La arquitectura pipeline fue diseñada para:

- soportar cargas incrementales
- escalar históricamente
- mantener consistencia analítica
- desacoplar procesamiento y consumo
- soportar gobernanza enterprise
- habilitar monitoreo operacional

---

# Arquitectura Incremental

La V4 implementa procesamiento incremental enterprise.

---

## Flujo Incremental

```text
NEW XLSX
    ↓
VALIDATION
    ↓
NORMALIZATION
    ↓
PARTITION UPDATE
    ↓
SEMANTIC REFRESH
    ↓
MART REFRESH
    ↓
APP REFRESH
```

---

# Componentes Pipeline

| Componente | Función |
|---|---|
| incremental_loader | Procesamiento incremental |
| warehouse_loader | Actualización warehouse |
| schema_mapper | Normalización columnas |
| qa_engine | Validación calidad |
| mart_generator | Regeneración marts |
| audit_logger | Auditoría |
| pipeline_monitor | Monitoreo operacional |

---

# Incremental Loader

Responsable de:

- cargar XLSX
- validar estructura
- normalizar columnas
- procesar incrementalmente

---

## Objetivos

- evitar reprocesamiento total
- mantener histórico
- soportar nuevos períodos
- automatizar refresh analítico

---

# Schema Mapper

El schema mapper estandariza columnas provenientes de XLSX.

---

# Objetivo

Convertir estructura operacional a estructura enterprise.

---

# Ejemplo

```text
"Venta Neta $"
    ↓
venta_total
```

---

# Normalización

El proceso incluye:

- rename columnas
- lowercase
- limpieza nombres
- estandarización empresarial

---

# QA Engine

Motor de validación de calidad empresarial.

---

# Validaciones QA

| Validación | Objetivo |
|---|---|
| Required Columns | Validar schema |
| Null Check | Detectar nulos |
| Duplicate Check | Detectar duplicados |
| Date Validation | Validar fechas |
| Negative Sales | Detectar ventas negativas |

---

# QA Score

El pipeline genera:

```text
QA SCORE
```

para validar integridad de carga.

---

# Warehouse Loader

Responsable de actualizar:

```text
FACT SALES
```

---

# Arquitectura Warehouse

La V4 implementa:

```text
PARTITIONED FACT STORAGE
```

---

# Particionamiento

```text
year=YYYY/month=MM
```

---

# Ejemplo

```text
data/warehouse/facts/sales/year=2026/month=05/data.parquet
```

---

# Beneficios

- performance
- escalabilidad
- menor consumo memoria
- incremental enterprise

---

# Rebuild Histórico

La V4 incorporó rebuild completo histórico.

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

# Semantic Layer Refresh

Luego de actualizar warehouse:

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
- lógica analítica

---

# Data Mart Regeneration

Posteriormente el pipeline ejecuta:

```text
generate_all_marts()
```

---

# Arquitectura Marts

Los marts consumen exclusivamente:

```text
vw_sales_enriched
```

Nunca:

```text
warehouse facts directos
```

---

# Marts Generados

| Mart | Objetivo |
|---|---|
| mart_sales_monthly | Ventas mensuales |
| mart_brand_performance | Performance marcas |
| mart_daily_sales | Freshness diario |

---

# Cache Refresh

Posterior al refresh marts:

```python
st.cache_data.clear()
```

---

# Objetivo

- refrescar dashboards
- evitar datos stale
- sincronizar frontend

---

# Dashboard Refresh

Finalmente:

```text
Streamlit Rerun
```

actualiza toda la aplicación.

---

# Pipeline Monitor

La V4 incorpora monitor operacional enterprise.

---

# Capacidades

- upload XLSX
- preview datos
- QA monitoring
- refresh marts
- refresh cache
- monitoreo ejecución
- logs auditoría

---

# Audit Logger

Cada ejecución registra:

- usuario
- archivo
- timestamp
- filas procesadas
- estado
- mensaje ejecución

---

# Objetivo

Garantizar:

- trazabilidad
- governance
- observabilidad
- debugging

---

# Flujo Completo Enterprise

```text
USER UPLOAD
    ↓
QA VALIDATION
    ↓
INCREMENTAL PROCESS
    ↓
WAREHOUSE UPDATE
    ↓
SEMANTIC REFRESH
    ↓
MART REBUILD
    ↓
CACHE CLEAR
    ↓
APP REFRESH
```

---

# Reglas Oficiales Pipeline

## Regla 1

```text
FACTS = SOLO CRUDO
```

---

## Regla 2

```text
SEMANTIC LAYER = ÚNICO LUGAR DE JOINS
```

---

## Regla 3

```text
MARTS = SOLO DESDE SEMANTIC LAYER
```

---

## Regla 4

```text
APP = SOLO CONSUMO MARTS
```

---

# Beneficios Pipeline V4

## Escalabilidad

- multi-año
- incremental
- warehouse enterprise

---

## Performance

- particionamiento
- marts optimizados
- refresh desacoplado

---

## Gobernanza

- auditabilidad
- QA
- monitoreo

---

## Mantenibilidad

- arquitectura modular
- desacoplamiento
- separación responsabilidades

---

# Consolidación Enterprise

La V4 consolida oficialmente:

- Incremental ETL enterprise
- Warehouse particionado
- Semantic refresh
- Analytics marts
- QA pipeline
- Governance pipeline
- Operational monitoring

---

# Estado Pipeline

## V4 COMPLETADA

Estado oficial:

```text
STABLE
```

---