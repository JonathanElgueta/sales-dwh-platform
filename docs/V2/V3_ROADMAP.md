# SALES DWH - Roadmap V3

Autor: Jonathan Elgueta Elgueta  
Versión Objetivo: V3.0.0  
Fecha: 2026-05-23

---

# Descripción

Este documento define las posibles evoluciones futuras para la versión V3 del proyecto Sales Data Warehouse.

La versión V2 dejó implementada una arquitectura estable y modular basada en:

- warehouse particionado
- incremental processing
- metadata orchestration
- semantic layer desacoplada

V3 buscará evolucionar hacia una plataforma más automatizada, observable y escalable.

---

# Objetivos V3

Los principales objetivos para V3 son:

- automatización completa pipeline
- monitoreo operacional
- logging centralizado
- reducción intervención manual
- mayor escalabilidad
- preparación cloud

---

# Roadmap Propuesto

## 1. MASTER ORCHESTRATOR

Prioridad: Alta

Objetivo:

Crear pipeline maestro único.

Ejemplo:

run_pipeline.py

Responsabilidad:

1. validar metadata
2. planificar incremental
3. ejecutar incremental
4. refrescar semantic layer
5. regenerar marts
6. ejecutar QA
7. generar logs

Beneficios:

- ejecución única
- simplificación operacional
- automatización completa

---

## 2. AUTO ACTIVE DETECTION

Prioridad: Alta

Objetivo:

Detectar automáticamente nuevo período ACTIVE.

Ejemplo:

2026_06

Proceso esperado:

1. detectar nuevo XLSX
2. marcar período anterior CLOSED
3. marcar nuevo período ACTIVE
4. actualizar metadata

Beneficios:

- menor operación manual
- pipeline más autónomo

---

## 3. CENTRALIZED LOGGING

Prioridad: Alta

Objetivo:

Implementar logging estructurado.

Posibles componentes:

- logs por ejecución
- logs incremental
- logs QA
- logs orchestration

Posible estructura:

data/logs/

Beneficios:

- trazabilidad
- debugging
- auditoría operacional

---

## 4. ERROR HANDLING

Prioridad: Alta

Objetivo:

Implementar manejo robusto de errores.

Posibles mejoras:

- rollback automático
- retry logic
- validaciones preventivas
- control excepciones centralizado

---

## 5. SCHEDULER AUTOMATION

Prioridad: Media

Objetivo:

Automatizar ejecución diaria.

Opciones:

- Windows Task Scheduler
- Apache Airflow
- Prefect
- Dagster

Beneficios:

- ejecución automática
- menor operación manual

---

## 6. QA AUTOMATION

Prioridad: Media

Objetivo:

Automatizar QA post pipeline.

Proceso esperado:

1. ejecutar QA automáticamente
2. generar reporte validación
3. alertar errores críticos

---

## 7. MONITORING

Prioridad: Media

Objetivo:

Agregar monitoreo operacional.

Posibles métricas:

- tiempo procesamiento
- volumen registros
- errores
- estado incremental
- estado marts

---

## 8. PERFORMANCE OPTIMIZATION

Prioridad: Media

Objetivo:

Optimizar procesamiento.

Posibles mejoras:

- parallel processing
- lazy loading
- DuckDB optimization
- memory optimization

---

## 9. CLOUD MIGRATION

Prioridad: Baja

Objetivo:

Preparar arquitectura cloud-ready.

Posibles destinos:

- AWS
- Azure
- GCP

Posibles componentes:

- S3 Data Lake
- Cloud orchestration
- Managed warehouse

---

## 10. API SERVING

Prioridad: Baja

Objetivo:

Exponer marts mediante APIs.

Posibles tecnologías:

- FastAPI
- Flask

Beneficios:

- consumo externo
- integración dashboards
- servicios analíticos

---

# Principios Arquitectónicos V3

V3 deberá mantener:

- modularidad
- desacoplamiento
- incremental processing
- semantic layer
- warehouse partitioning

---

# Estado Actual Base

La arquitectura V2 ya entrega:

- warehouse estable
- incremental funcional
- semantic desacoplado
- marts operacionales
- QA validado

Esto permite evolucionar hacia V3 de manera segura y escalable.

---

# Visión Objetivo

La visión de largo plazo es construir una plataforma moderna de ingeniería de datos con:

- automatización completa
- observabilidad
- escalabilidad
- arquitectura cloud-ready
- pipelines enterprise

---

# Estado Actual

Roadmap V3 Definido

Pendiente de Implementación Futura