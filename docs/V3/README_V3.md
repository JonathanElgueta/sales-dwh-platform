# SALES DWH PLATFORM — V3

Autor: Jonathan Elgueta Elgueta  
Versión: V3.0.0  
Estado: STABLE  
Arquitectura: ENTERPRISE ANALYTICS PLATFORM  
Frontend: STREAMLIT BI APP  
Data Warehouse: DUCKDB  
Última actualización: 2026-05-25  

---

# Descripción

La versión V3 transforma el proyecto Sales DWH desde un ETL analítico tradicional hacia una plataforma analítica enterprise completa.

La solución incorpora:

- arquitectura modular frontend
- semantic layer
- data marts analíticos
- dashboard ejecutivo
- analytics multidimensional
- QA layer
- pipeline monitoring
- executive insights
- visual analytics
- arquitectura escalable

---

# Objetivos V3

La versión V3 tuvo como objetivo construir una plataforma BI empresarial moderna utilizando arquitectura desacoplada y modular.

## Principales mejoras implementadas

- frontend enterprise modular
- dashboards ejecutivos
- analytics interactivos
- drilldown analytics
- YoY analytics
- heatmaps
- market share analytics
- pipeline monitoring
- QA monitoring
- executive alerts
- semantic analytics
- reusable marts

---

# Arquitectura General

```text
RAW XLSX FILES
        ↓
EXTRACT LAYER
        ↓
TRANSFORM LAYER
        ↓
DATA WAREHOUSE (DuckDB)
        ↓
SEMANTIC LAYER
        ↓
DATA MARTS
        ↓
STREAMLIT ANALYTICS PLATFORM
```

---

# Arquitectura Técnica

## Backend

### ETL Pipeline

Implementaciones principales:

- extracción desde XLSX
- transformaciones con Pandas
- carga incremental
- logging operacional
- metadata orchestration
- QA validations
- parquet persistence

---

## Data Warehouse

### Fact Table

- fact_sales

### Dimensiones

- dim_date
- dim_product
- dim_customer
- dim_channel

---

## Semana Bimbo

La dimensión temporal implementa lógica comercial personalizada:

- semana inicia jueves
- semana finaliza miércoles

---

# Semantic Layer

Views analíticas enriquecidas:

- vw_sales_enriched
- KPIs ejecutivos
- rankings comerciales
- market share
- métricas derivadas
- business logic layer

---

# Data Marts

## Marts implementados

| Mart | Descripción |
|---|---|
| Sales Monthly | métricas mensuales |
| Brand Performance | performance marcas |
| Category Performance | performance categorías |
| Channel Performance | performance canales |

---

# Frontend Analytics App

## Módulos implementados

### Home

- KPIs ejecutivos
- executive summary
- executive alerts
- tendencia ventas
- comparativo YoY

---

### Dashboard Ejecutivo

- top marcas
- top categorías
- top canales
- market share
- heatmap ventas
- executive insights

---

### Analytics Marcas

- drilldown analytics
- evolución mensual
- market share trend
- treemap categorías
- YoY analytics
- insights automáticos

---

### Pipeline Monitor

- estado pipeline
- métricas ETL
- monitoreo operacional

---

### QA Monitor

- validaciones calidad
- integridad datos
- estado QA

---

# UX / UI

Características implementadas:

- dark mode
- KPI cards premium
- sidebar enterprise
- plotly interactive charts
- responsive layout
- modular frontend architecture

---

# Stack Tecnológico

| Tecnología | Uso |
|---|---|
| Python | backend |
| Pandas | transformaciones |
| DuckDB | data warehouse |
| Streamlit | frontend BI |
| Plotly | visualizaciones |
| Parquet | persistencia |

---

# Estructura Proyecto

```text
sales-dwh/

├── data/
│   ├── raw/
│   ├── marts/
│   ├── semantic/
│   └── duckdb/
│
├── docs/
│   └── v3/
│
├── src/
│   ├── app/
│   │   ├── app.py
│   │   ├── views/
│   │   └── services/
│   │
│   ├── pipeline/
│   ├── marts/
│   ├── semantic/
│   ├── warehouse/
│   └── qa/
│
└── README.md
```

---

# Cómo Ejecutar

## 1. Crear entorno virtual

```bash
python -m venv venv
```

---

## 2. Activar entorno

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 4. Ejecutar pipeline

```bash
python -m src.pipeline.run_pipeline
```

---

## 5. Ejecutar aplicación

```bash
streamlit run src/app/app.py
```

---

# Características Enterprise

## Implementado en V3

- arquitectura modular
- incremental ETL
- semantic layer
- QA layer
- data marts
- executive analytics
- drilldown analytics
- monitoring layer
- executive alerts
- modular frontend

---

# Roadmap V4

## Próximas funcionalidades

### Machine Learning

- forecast ventas
- detección anomalías
- predicción devoluciones

---

### Cloud & DevOps

- Docker
- CI/CD
- Airflow
- cloud deployment

---

### Seguridad

- login
- roles
- control acceso

---

### APIs

- REST API
- integración sistemas externos

---

# Estado Proyecto

## V3 COMPLETADA

La versión V3 implementa una plataforma analítica enterprise funcional, modular y escalable con capacidades BI avanzadas.

---

# Autor

Proyecto desarrollado como plataforma analítica empresarial end-to-end orientada a arquitectura moderna de datos y Business Intelligence.