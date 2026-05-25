# SALES DWH PLATFORM — ARCHITECTURE

Autor: Jonathan Elgueta Elgueta  
Versión: V3.0.0  
Estado: STABLE  
Documento: ARQUITECTURA TÉCNICA  
Última actualización: 2026-05-25  

---

# Descripción

Este documento describe la arquitectura técnica completa implementada en Sales DWH Platform V3.

La solución fue diseñada utilizando principios de arquitectura modular, desacoplada y escalable orientada a plataformas analíticas empresariales modernas.

---

# Arquitectura General

La plataforma implementa una arquitectura analítica multicapa:

```text
RAW FILES
    ↓
EXTRACT LAYER
    ↓
TRANSFORM LAYER
    ↓
DATA WAREHOUSE
    ↓
SEMANTIC LAYER
    ↓
DATA MARTS
    ↓
ANALYTICS APPLICATION
```

---

# Capas Arquitectura

## 1. RAW LAYER

La capa RAW almacena archivos fuente originales.

### Características

- archivos XLSX originales
- almacenamiento histórico
- fuente primaria datos
- persistencia inicial

### Ubicación

```text
data/raw/
```

---

# 2. EXTRACT LAYER

La capa de extracción se encarga de:

- lectura archivos XLSX
- validación inicial
- normalización básica
- carga a DataFrames

### Tecnologías

- Python
- Pandas

---

# 3. TRANSFORM LAYER

La capa de transformación implementa lógica de negocio y limpieza de datos.

### Procesos implementados

- limpieza datos
- tipificación columnas
- cálculo métricas
- enriquecimiento
- generación dimensiones
- incremental loading

---

# 4. DATA WAREHOUSE LAYER

La plataforma utiliza DuckDB como motor analítico principal.

### Objetivos

- almacenamiento analítico
- procesamiento columnar
- consultas rápidas
- persistencia centralizada

### Arquitectura dimensional

#### Fact Table

```text
fact_sales
```

#### Dimensiones

```text
dim_date
dim_product
dim_customer
dim_channel
```

---

# Semana Bimbo

La dimensión temporal implementa lógica comercial personalizada.

## Reglas

- inicio semana: jueves
- fin semana: miércoles

Esta lógica permite análisis alineados al calendario operacional del negocio.

---

# 5. SEMANTIC LAYER

La semantic layer abstrae complejidad técnica y expone métricas analíticas reutilizables.

## Objetivos

- desacoplar lógica negocio
- centralizar KPIs
- reutilización métricas
- simplificar analytics

---

## View principal

```text
vw_sales_enriched
```

### Métricas implementadas

- venta_total
- pct_devolucion
- market_share_pct
- ranking_venta

---

# 6. DATA MARTS LAYER

Los data marts permiten analytics especializados por dominio.

## Marts implementados

### Sales Monthly

Métricas mensuales agregadas.

---

### Brand Performance

Analytics por marca:

- market share
- ranking
- ventas
- devoluciones

---

### Category Performance

Analytics por categoría comercial.

---

### Channel Performance

Analytics por canal de venta.

---

# 7. ANALYTICS APPLICATION LAYER

La aplicación frontend fue desarrollada con Streamlit.

## Objetivos

- visual analytics
- dashboards ejecutivos
- drilldown analytics
- executive monitoring

---

# Arquitectura Frontend

La V3 implementa arquitectura modular desacoplada.

## Estructura

```text
src/app/

├── app.py
├── views/
├── services/
```

---

# Views Layer

Cada módulo analítico fue desacoplado:

```text
home.py
executive_dashboard.py
brand_analytics.py
pipeline_monitor.py
qa_monitor.py
```

---

# Services Layer

La capa services encapsula acceso a datos.

## Implementaciones

```text
data_loader.py
```

---

# Navegación Aplicación

La aplicación implementa navegación centralizada mediante sidebar enterprise.

## Módulos disponibles

- Home
- Dashboard Ejecutivo
- Analytics Marcas
- Pipeline Monitor
- QA Monitor

---

# Arquitectura QA

La solución incorpora capa QA operacional.

## Validaciones implementadas

- null checks
- duplicate checks
- integridad dimensiones
- integridad facts
- validación temporal
- validación Semana Bimbo

---

# Arquitectura Incremental

La V3 implementa procesamiento incremental.

## Beneficios

- menor tiempo carga
- procesamiento eficiente
- escalabilidad
- reducción costos

---

# Persistencia

La plataforma utiliza múltiples formatos persistencia.

## Formatos utilizados

| Formato | Uso |
|---|---|
| XLSX | raw source |
| Parquet | analytics persistence |
| DuckDB | warehouse engine |

---

# Stack Tecnológico

| Tecnología | Uso |
|---|---|
| Python | backend |
| Pandas | transformaciones |
| DuckDB | warehouse |
| Streamlit | frontend |
| Plotly | visualización |
| Parquet | persistencia |

---

# Características Enterprise

## Implementado en V3

- arquitectura modular
- semantic layer
- marts desacoplados
- QA layer
- analytics layer
- monitoring
- executive insights
- frontend enterprise
- reusable metrics

---

# Beneficios Arquitectura

## Técnicos

- desacoplamiento
- mantenibilidad
- escalabilidad
- reutilización
- performance

---

## Negocio

- analytics ejecutivos
- monitoreo operacional
- KPIs centralizados
- insights automáticos
- visual analytics

---

# Estado Arquitectura

## V3 COMPLETADA

La arquitectura V3 implementa una plataforma analítica enterprise modular, desacoplada y escalable orientada a Business Intelligence moderno.