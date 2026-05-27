# SALES DWH PLATFORM — ANALYTICS APPLICATION

Autor: Jonathan Elgueta Elgueta
Versión: V4.0.0
Estado: STABLE
Documento: ANALYTICS APPLICATION
Última actualización: 2026-05-26

---

# Descripción

Este documento describe la arquitectura de la aplicación analítica empresarial implementada en Sales DWH Platform V4.

La aplicación representa la capa final de consumo analítico enterprise construida sobre:

- Analytics Data Marts
- Semantic Layer
- Enterprise Governance
- Incremental Warehouse
- AI Analytics

---

# Objetivo

La aplicación fue diseñada para:

- visualización ejecutiva
- monitoreo operacional
- análisis empresarial
- forecasting
- anomaly detection
- QA monitoring
- pipeline orchestration

---

# Arquitectura Aplicación

```text
RAW XLSX
    ↓
WAREHOUSE
    ↓
SEMANTIC LAYER
    ↓
DATA MARTS
    ↓
STREAMLIT ANALYTICS APP
```

---

# Framework

La plataforma fue desarrollada utilizando:

```text
Streamlit
```

---

# Objetivos Streamlit

- rapid enterprise development
- dashboards interactivos
- analytics enterprise
- operational monitoring
- AI visualization

---

# Arquitectura Frontend

La aplicación consume exclusivamente:

```text
data/marts
```

---

# Regla Oficial

```text
LA APP NUNCA CONSUME FACTS DIRECTAMENTE
```

---

# Reglas Arquitectónicas

## Regla 1

```text
FACTS = CRUDO
```

---

## Regla 2

```text
SEMANTIC LAYER = BUSINESS LOGIC
```

---

## Regla 3

```text
MARTS = ANALYTICS OPTIMIZED
```

---

## Regla 4

```text
APP = VISUALIZATION ONLY
```

---

# Arquitectura Módulos

```text
STREAMLIT APP
│
├── HOME
├── EXECUTIVE DASHBOARD
├── BRAND ANALYTICS
├── PIPELINE MONITOR
├── QA MONITOR
├── AI FORECASTING
└── AI ANOMALY DETECTION
```

---

# Home Dashboard

Dashboard ejecutivo principal.

---

## Objetivos

- KPIs ejecutivos
- ventas totales
- tendencias
- freshness diario
- alertas ejecutivas

---

## Data Sources

| Mart | Uso |
|---|---|
| mart_sales_monthly | KPIs ventas |
| mart_brand_performance | Top marca |
| mart_daily_sales | Última fecha |

---

# KPIs Home

| KPI | Descripción |
|---|---|
| Venta Total | Venta consolidada |
| Venta Promedio | Promedio ventas |
| Top Marca | Marca líder |
| Variación % | Comparativo período |

---

# Freshness Diario

La V4 incorpora monitoreo diario oficial.

---

## Objetivo

Mostrar:

```text
Última fecha real cargada
```

---

## Fuente

```text
mart_daily_sales
```

---

# Executive Dashboard

Dashboard empresarial consolidado.

---

## Objetivos

- análisis ejecutivo
- tendencias enterprise
- consolidación negocio
- KPIs estratégicos

---

## Capacidades

- ventas históricas
- YoY analysis
- comparativos
- tendencias

---

# Brand Analytics

Módulo especializado en marcas.

---

## Objetivos

- market share
- ranking marcas
- performance marcas
- analytics negocio

---

## Fuente

```text
mart_brand_performance
```

---

# Pipeline Monitor

Módulo operacional enterprise.

---

# Objetivos

- ejecutar incremental ETL
- monitoreo pipeline
- QA validation
- refresh marts
- governance operacional

---

# Capacidades

## Upload XLSX

Carga incremental enterprise.

---

## QA Validation

Validación automática:

- columnas
- nulos
- duplicados
- fechas
- integridad

---

## Incremental Refresh

Actualización automática:

```text
warehouse
semantic layer
marts
cache
dashboards
```

---

## Audit Logs

Registro ejecución:

- usuario
- archivo
- filas
- estado
- timestamp

---

# QA Monitor

Módulo especializado en calidad de datos.

---

# Objetivos

- monitoreo calidad
- validación operacional
- governance datos
- observabilidad

---

# Validaciones

| Validación | Objetivo |
|---|---|
| Required Columns | Schema |
| Null Check | Integridad |
| Duplicates | Calidad |
| Date Validation | Fechas |
| Negative Sales | Ventas |

---

# AI Forecasting

Módulo inteligencia artificial forecasting.

---

# Objetivos

- proyección ventas
- forecasting enterprise
- análisis predictivo

---

# Estado

```text
FOUNDATION READY
```

---

# AI Anomaly Detection

Módulo inteligencia artificial anomalías.

---

# Objetivos

- detectar anomalías
- monitoreo operacional
- observabilidad enterprise

---

# Estado

```text
FOUNDATION READY
```

---

# Arquitectura Seguridad

La aplicación incorpora:

- autenticación
- roles
- governance
- permisos

---

# Roles

| Rol | Acceso |
|---|---|
| admin | Full Access |
| qa | QA Layer |
| ejecutivo | Dashboards |
| operaciones | Pipeline |

---

# Session Management

La plataforma implementa:

```text
session_manager
```

---

# Authentication Layer

La plataforma incorpora:

```text
auth_service
```

---

# Navegación Enterprise

La aplicación implementa navegación basada en roles.

---

# Arquitectura Navegación

```text
ROLE
    ↓
PERMISSIONS
    ↓
AVAILABLE MODULES
```

---

# Component Architecture

La app utiliza arquitectura desacoplada componentes.

---

# Componentes

| Componente | Objetivo |
|---|---|
| kpi_card | KPIs |
| alerts | Alertas |
| section_header | Headers |
| theme | Styling |

---

# Beneficios Arquitectónicos

## Escalabilidad

- nuevos dashboards
- nuevos módulos
- nuevos KPIs

---

## Gobernanza

- roles
- permisos
- trazabilidad

---

## Performance

- marts optimizados
- cache Streamlit
- desacoplamiento

---

## Mantenibilidad

- arquitectura modular
- separación responsabilidades
- reusable components

---

# Cache Layer

La aplicación implementa:

```python
@st.cache_data
```

---

# Objetivo

- optimizar performance
- evitar recargas innecesarias
- acelerar dashboards

---

# Refresh Enterprise

Posterior al incremental:

```python
st.cache_data.clear()
```

---

# Objetivo

Garantizar:

- dashboards actualizados
- datos sincronizados
- freshness enterprise

---

# Integración Arquitectura V4

```text
WAREHOUSE
    ↓
SEMANTIC LAYER
    ↓
MARTS
    ↓
STREAMLIT APP
```

---

# Beneficios V4

## Enterprise Analytics

- dashboards ejecutivos
- analytics marcas
- monitoreo operacional

---

## Governance

- QA
- audit logs
- autenticación

---

## Operational Monitoring

- freshness diario
- pipeline monitoring
- incremental execution

---

## AI Foundation

La arquitectura habilita:

- forecasting
- anomaly detection
- advanced analytics

---

# Consolidación V4

La V4 consolida oficialmente:

- Enterprise Analytics App
- Operational Monitoring
- Incremental Governance
- Executive Dashboards
- QA Monitoring
- AI Foundation

---

# Estado Analytics App

## V4 COMPLETADA

Estado oficial:

```text
STABLE
```

---