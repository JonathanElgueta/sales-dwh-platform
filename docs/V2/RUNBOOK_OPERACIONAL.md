# SALES DWH - Runbook Operacional

Autor: Jonathan Elgueta Elgueta  
Versión: V2.0.0  
Estado: STABLE

---

# Descripción

Este documento describe los procedimientos operacionales y de recovery para el proyecto Sales DWH.

La arquitectura V2 implementa:

- warehouse particionado
- procesamiento incremental
- metadata orchestration
- semantic layer desacoplada
- marts analíticos
- QA operacional

---

# Flujo Operacional Recomendado

La secuencia operacional estándar es:

1. validar metadata
2. ejecutar incremental
3. refrescar semantic layer
4. reconstruir marts
5. ejecutar QA

---

# Flujo Completo

```text
RAW XLSX
    ↓

METADATA VALIDATION
    ↓

INCREMENTAL LOAD
    ↓

WAREHOUSE UPDATE
    ↓

SEMANTIC REFRESH
    ↓

MARTS REFRESH
    ↓

QA VALIDATION
```

---

# 1. Validar Metadata

Este proceso valida:

- un único ACTIVE
- continuidad períodos
- metadata consistente

Comando:

```bash
python -m src.orchestration.validate_metadata
```

Resultado esperado:

- un único ACTIVE
- continuidad correcta
- metadata validada

---

# 2. Ejecutar Incremental

Este proceso:

- identifica período ACTIVE
- elimina partición existente
- reprocesa período activo
- recrea parquet particionado
- actualiza metadata

Comando:

```bash
python -m src.orchestration.execute_incremental_load
```

Resultado esperado:

- partición recreada
- metadata actualizada
- incremental completado

---

# 3. Refrescar Semantic Layer

Este proceso:

- recrea vw_sales_enriched
- centraliza joins
- actualiza semantic layer

Comando:

```bash
python -m src.semantic.create_views
```

Resultado esperado:

```text
7406100 registros
```

---

# 4. Reconstruir Marts

Este proceso genera:

- mart_sales_monthly
- mart_brand_performance
- mart_sales_weekly_bimbo
- mart_category_performance
- mart_channel_performance

Comando:

```bash
python -m src.marts.build_marts
```

Resultado esperado:

- marts exportados correctamente
- marts actualizados

---

# 5. Ejecutar QA

## QA Sales

Valida:

- duplicados
- nulos
- integridad dimensional
- validación financiera

Comando:

```bash
python -m src.qa.validate_sales_enriched
```

Resultado esperado:

```text
0 duplicados
0 nulos críticos
```

---

## QA Date

Valida:

- semana bimbo
- calendario
- quarter
- continuidad fechas

Comando:

```bash
python -m src.qa.validate_dim_date
```

Resultado esperado:

```text
semana_bimbo correcta
QA calendario exitoso
```

---

# Recovery Operacional

---

# Caso 1 - Error Incremental

## Síntomas

- parquet corrupto
- partición incompleta
- error escritura parquet

## Recovery

1. eliminar partición afectada
2. reejecutar incremental
3. recrear semantic layer
4. reconstruir marts
5. ejecutar QA

---

# Caso 2 - Error Semantic Layer

## Recovery

Ejecutar:

```bash
python -m src.semantic.create_views
```

---

# Caso 3 - Error Marts

## Recovery

Ejecutar:

```bash
python -m src.marts.build_marts
```

---

# Caso 4 - Metadata Incorrecta

## Síntomas

- múltiples ACTIVE
- períodos faltantes
- continuidad inválida

## Recovery

1. revisar processed_files.parquet
2. corregir metadata
3. validar ACTIVE
4. reejecutar validate_metadata

Comando validación:

```bash
python -m src.orchestration.validate_metadata
```

---

# Validaciones QA Críticas

## Duplicados

Resultado esperado:

```text
0 duplicados
```

---

## UNKNOWN Productos

Resultado esperado:

```text
porcentaje mínimo
```

---

## Nulos

Resultado esperado:

```text
0 nulos críticos
```

---

# Cambio Manual ACTIVE

Cuando aparece nuevo período:

```text
2026_06
```

Proceso esperado:

1. marcar 2026_05 → CLOSED
2. marcar 2026_06 → ACTIVE
3. ejecutar incremental

---

# Pipeline Correcto si:

- warehouse actualizado
- metadata consistente
- semantic layer operativa
- marts actualizados
- QA exitoso

---

# Arquitectura Operacional

```text
raw/
    ↓

metadata/
    ↓

warehouse/
    ↓

semantic/
    ↓

marts/
    ↓

qa/
```

---

# Estado Operacional

La arquitectura V2 actualmente se encuentra:

- operacional
- validada
- estable
- desacoplada
- preparada para evolución V3

---

# Componentes Activos

| Componente | Estado |
|---|---|
| Warehouse | ✅ |
| Incremental | ✅ |
| Metadata Layer | ✅ |
| Semantic Layer | ✅ |
| Marts | ✅ |
| QA | ✅ |

---

# Estado Actual

Versión:

```text
V2.0.0
```

Estado:

```text
STABLE
```