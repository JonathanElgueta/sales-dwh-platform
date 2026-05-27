# SALES DWH PLATFORM — SEMANTIC LAYER

Autor: Jonathan Elgueta Elgueta
Versión: V4.0.0
Estado: STABLE
Documento: SEMANTIC LAYER
Última actualización: 2026-05-26

---

# Descripción

Este documento describe la arquitectura Semantic Layer implementada en Sales DWH Platform V4.

La Semantic Layer representa el núcleo analítico empresarial de la plataforma.

La V4 consolida oficialmente la separación entre:

- facts transaccionales
- dimensiones empresariales
- lógica analítica
- marts
- dashboards

---

# Objetivo

La Semantic Layer fue diseñada para:

- centralizar joins empresariales
- desacoplar lógica analítica
- unificar modelo de negocio
- soportar marts analíticos
- evitar duplicación lógica
- habilitar gobernanza semántica

---

# Arquitectura Semantic Layer

```text
FACT SALES
    +
DIM PRODUCTO
    +
DIM AGENCIA
    +
DIM DATE
    ↓
VW_SALES_ENRICHED
    ↓
ANALYTICS MARTS
```

---

# Motor Analítico

La Semantic Layer utiliza:

```text
DuckDB
```

---

# Objetivos DuckDB

- procesamiento analítico
- alto performance
- consultas SQL enterprise
- semantic views
- analytical joins

---

# Vista Oficial

La vista principal empresarial es:

```sql
vw_sales_enriched
```

---

# Objetivo Vista

Centralizar:

- enriquecimiento
- joins
- semántica empresarial
- modelo analítico unificado

---

# Arquitectura Oficial

```text
FACT SALES
    LEFT JOIN
DIM PRODUCTO

FACT SALES
    LEFT JOIN
DIM AGENCIA

FACT SALES
    LEFT JOIN
DIM DATE
```

---

# FACT SALES

La tabla fact almacena únicamente:

- transacciones crudas
- granularidad diaria
- métricas operacionales

Los facts NO contienen:

- joins
- KPIs
- market share
- rankings
- lógica negocio

---

# DIM PRODUCTO

Responsable de:

- marca
- categoria
- linea
- cluster
- negocio
- metadata producto

---

# DIM AGENCIA

Responsable de:

- metadata agencias
- nombres operacionales

---

# DIM DATE

Responsable de:

- inteligencia calendario
- semanas
- quarter
- semana_bimbo
- atributos temporales

---

# Resultado Semantic Layer

La vista enriquecida contiene:

- histórico completo
- granularidad diaria
- atributos producto
- atributos agencia
- atributos fecha
- estructura enterprise analytics

---

# Beneficios Semantic Layer

## Desacoplamiento

Separación oficial entre:

```text
FACTS
DIMENSIONS
MARTS
DASHBOARDS
```

---

## Centralización

Toda la lógica empresarial queda centralizada en:

```sql
vw_sales_enriched
```

---

## Escalabilidad

Permite:

- crecimiento histórico
- nuevos marts
- nuevos KPIs
- nuevas métricas

---

## Gobernanza

Evita:

- lógica duplicada
- joins inconsistentes
- reglas contradictorias

---

# Reglas Oficiales Semantic Layer

## Regla 1

```text
SOLO LA SEMANTIC LAYER REALIZA JOINS
```

---

## Regla 2

```text
FACTS = SOLO CRUDO
```

---

## Regla 3

```text
MARTS NO HACEN JOINS
```

---

## Regla 4

```text
DASHBOARDS NO HACEN BUSINESS LOGIC
```

---

# Integración Warehouse

La Semantic Layer consume:

```text
data/warehouse/facts/sales
```

y:

```text
data/warehouse/dimensions
```

---

# Integración Marts

Los marts consumen exclusivamente:

```sql
vw_sales_enriched
```

---

# Arquitectura Marts

```text
SEMANTIC LAYER
    ↓
mart_sales_monthly

SEMANTIC LAYER
    ↓
mart_brand_performance

SEMANTIC LAYER
    ↓
mart_daily_sales
```

---

# Granularidad

La Semantic Layer conserva:

```text
GRANULARIDAD DIARIA
```

Esto permite:

- freshness diario
- monitoreo operacional
- análisis transaccional
- forecasting futuro

---

# Integración Aplicación

La aplicación Streamlit NO consume:

```text
warehouse directo
```

La aplicación consume:

```text
analytics marts
```

---

# Beneficios Enterprise

## Performance

- marts optimizados
- joins centralizados
- consultas desacopladas

---

## Mantenibilidad

- lógica centralizada
- menor duplicación
- arquitectura limpia

---

## Escalabilidad

- nuevos marts
- nuevos dashboards
- nuevos KPIs
- IA avanzada

---

## Gobernanza

- semántica única
- reglas centralizadas
- trazabilidad

---

# Arquitectura Final V4

```text
RAW XLSX
    ↓
PARTITIONED FACTS
    ↓
DIMENSIONS
    ↓
SEMANTIC LAYER
    ↓
ANALYTICS MARTS
    ↓
ENTERPRISE APP
```

---

# Consolidación V4

La V4 consolida oficialmente:

- Semantic Layer enterprise
- joins desacoplados
- business logic centralizada
- analytical views
- modelo semántico enterprise

---

# Estado Semantic Layer

## V4 COMPLETADA

Estado oficial:

```text
STABLE
```

---