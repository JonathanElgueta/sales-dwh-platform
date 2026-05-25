# SALES DWH - Proceso Incremental V2

Autor: Jonathan Elgueta Elgueta  
Versión: V2.0.0  
Fecha: 2026-05-23

---

## Descripción

Este documento describe el funcionamiento completo del procesamiento incremental implementado en la versión V2 del proyecto Sales Data Warehouse.

La arquitectura incremental fue diseñada para:

- minimizar reprocesamiento
- aislar períodos históricos
- simplificar recovery
- habilitar overwrite controlado
- mejorar performance operacional

---

# Objetivo del Incremental

La estrategia incremental permite reprocesar únicamente el período activo del negocio,
manteniendo congelado el histórico previamente consolidado.

---

# Conceptos Principales

## ACTIVE

Representa el período actualmente abierto y en crecimiento.

Características:

- puede cambiar diariamente
- se reprocesa completamente
- representa el último período disponible

Ejemplo:

2026_05

---

## CLOSED

Representa períodos históricos cerrados.

Características:

- nunca se reprocesan
- permanecen congelados
- se consideran históricos estables

Ejemplo:

2026_04
2026_03
2025_12

---

# Arquitectura Incremental

RAW XLSX
    ↓

METADATA VALIDATION
    ↓

INCREMENTAL PLANNING
    ↓

PARTITION OVERWRITE
    ↓

WAREHOUSE UPDATE
    ↓

SEMANTIC REFRESH
    ↓

MARTS REFRESH

---

# Metadata Layer

Ubicación:

data/metadata/processed_files.parquet

Responsabilidad:

- identificar ACTIVE
- controlar períodos
- habilitar orchestration
- registrar procesamiento

---

# Campos Principales Metadata

| Campo | Descripción |
|---|---|
| file_name | nombre archivo origen |
| period | período YYYY_MM |
| status | ACTIVE o CLOSED |
| processed_at | timestamp procesamiento |
| warehouse_partition | partición warehouse |
| rows_processed | cantidad filas procesadas |
| file_size_mb | tamaño archivo |

---

# Regla Operacional Principal

La arquitectura V2 implementa una regla simple:

- CLOSED → SKIP
- ACTIVE → REPROCESS

---

# Ejemplo Real

## Estado Metadata

| period | status |
|---|---|
| 2026_04 | CLOSED |
| 2026_05 | ACTIVE |

---

# Resultado Planner

| period | action |
|---|---|
| 2026_04 | SKIP |
| 2026_05 | REPROCESS |

---

# Estrategia de Overwrite

El sistema NO hace append.

La estrategia oficial es:

overwrite completo por partición.

---

# Flujo Overwrite

Ejemplo:

ACTIVE = 2026_05

Proceso:

1. localizar XLSX origen
2. eliminar partición existente
3. reprocesar XLSX completo
4. recrear parquet
5. actualizar metadata

---

# Ejemplo Warehouse

Antes:

warehouse/facts/sales/year=2026/month=05/

↓

DELETE PARTITION

↓

RECREATE PARTITION

---

# Beneficios Arquitectónicos

La estrategia incremental entrega:

- simplicidad operacional
- bajo riesgo
- fácil debugging
- recovery simple
- aislamiento histórico
- alta mantenibilidad

---

# Ejecución Pipeline

## 1. Validar Metadata

Comando:

python -m src.orchestration.validate_metadata

---

## 2. Planificar Incremental

Comando:

python -m src.orchestration.plan_incremental_load

---

## 3. Ejecutar Incremental

Comando:

python -m src.orchestration.execute_incremental_load

---

## 4. Refrescar Semantic Layer

Comando:

python -m src.semantic.create_views

---

## 5. Refrescar Marts

Comando:

python -m src.marts.build_marts

---

# Validaciones QA

Posterior al incremental se recomienda ejecutar:

python -m src.qa.validate_sales_enriched

python -m src.qa.validate_dim_date

---

# Cambio Automático de ACTIVE

Cuando aparece un nuevo período:

Ejemplo:

2026_06

El sistema debe:

1. marcar 2026_05 como CLOSED
2. marcar 2026_06 como ACTIVE
3. reprocesar solamente 2026_06

---

# Recovery Operacional

En caso de error:

1. eliminar partición corrupta
2. reejecutar incremental
3. regenerar semantic layer
4. regenerar marts

Debido al aislamiento particionado,
el recovery es rápido y de bajo impacto.

---

# Principales Ventajas V2

Comparado con full reload:

| Full Reload | Incremental V2 |
|---|---|
| reprocesa todo | reprocesa solo ACTIVE |
| alto tiempo | tiempo reducido |
| alto riesgo | bajo riesgo |
| recovery complejo | recovery simple |
| baja escalabilidad | alta escalabilidad |

---

# Estado Actual

Incremental:

Operacional y Validado

Características:

- overwrite particionado
- metadata-driven
- warehouse incremental
- QA validado
- semantic desacoplado

---

# Futuras Mejoras V3

Posibles evoluciones:

- auto detección ACTIVE
- scheduler automático
- logging centralizado
- monitoreo operacional
- alertas automáticas
- parallel processing