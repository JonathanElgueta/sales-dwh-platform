# SALES DWH PLATFORM — DATA MODEL

Autor: Jonathan Elgueta Elgueta
Versión: V4.0.0
Estado: STABLE
Documento: MODELO DE DATOS
Última actualización: 2026-05-26

---

# Descripción

Este documento describe el modelo de datos empresarial implementado en Sales DWH Platform V4.

La plataforma utiliza un modelo dimensional desacoplado basado en:

- Fact Tables
- Dimension Tables
- Semantic Views
- Analytics Data Marts

La V4 consolida oficialmente el modelo enterprise basado en warehouse particionado + semantic layer.

---

# Arquitectura del Modelo

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

# Principios del Modelo

## FACT TABLES

Los facts contienen únicamente:

- transacciones crudas
- granularidad diaria
- métricas operacionales

Los facts NO contienen:

- joins
- lógica de negocio
- KPIs
- market share
- rankings
- atributos dimensionales

---

## DIMENSIONS

Las dimensiones contienen:

- atributos empresariales
- metadata
- jerarquías analíticas
- clasificación negocio

---

## SEMANTIC LAYER

La semantic layer centraliza:

- joins
- enriquecimiento
- lógica analítica empresarial

Vista oficial:

```sql
vw_sales_enriched
```

---

# FACT SALES

La tabla fact principal almacena todas las transacciones de venta.

---

## Granularidad

```text
Diaria
```

Cada fila representa:

```text
Una transacción de venta diaria
```

---

## Particionamiento

La V4 implementa particionamiento enterprise:

```text
year=YYYY/month=MM
```

Ejemplo:

```text
data/warehouse/facts/sales/year=2026/month=05/data.parquet
```

---

## Ubicación

```text
data/warehouse/facts/sales
```

---

# Estructura FACT SALES

| Columna | Tipo | Descripción |
|---|---|---|
| fecha | date | Fecha venta |
| canal | string | Canal comercial |
| subcanal | string | Subcanal comercial |
| cadena | string | Cadena retail |
| agencia_id | int/string | Identificador agencia |
| agencia | string | Nombre agencia |
| producto_id | int/string | Identificador producto |
| producto | string | Nombre producto |
| devolucion_clp | numeric | Devolución CLP |
| devolucion_tn | numeric | Devolución toneladas |
| devolucion_ue | numeric | Devolución UE |
| devolucion_pz | numeric | Devolución piezas |
| venta_total | numeric | Venta neta CLP |
| venta_tn | numeric | Venta toneladas |
| venta_ue | numeric | Venta UE |
| venta_pz | numeric | Venta piezas |
| year | int | Año partición |
| month | int | Mes partición |

---

# DIM PRODUCTO

Dimensión maestra de productos.

---

## Ubicación

```text
data/warehouse/dimensions/products/dim_producto.parquet
```

---

## Primary Key

```text
producto_id
```

---

## Estructura

| Campo | Descripción |
|---|---|
| producto_id | ID producto |
| producto_nombre | Nombre producto |
| marca | Marca |
| categoria | Categoría |
| linea | Línea |
| cupo_contenedor | Cupo contenedor |
| unidad_equivalente | Unidad equivalente |
| gramaje | Gramaje |
| cluster | Cluster |
| negocio | Negocio |
| categoria_propia | Categoría propia |
| categoria_or | Categoría OR |

---

# DIM AGENCIA

Dimensión maestra de agencias.

---

## Ubicación

```text
data/warehouse/dimensions/agencies/dim_agencia.parquet
```

---

## Primary Key

```text
agencia_id
```

---

## Estructura

| Campo | Descripción |
|---|---|
| agencia_id | ID agencia |
| agencia_nombre | Nombre agencia |

---

# DIM DATE

Dimensión calendario empresarial.

---

## Ubicación

```text
data/warehouse/dimensions/date/dim_date.parquet
```

---

## Primary Key

```text
date_key
```

---

## Objetivo

Centralizar inteligencia calendario empresarial.

---

## Estructura

| Campo | Descripción |
|---|---|
| date_key | Key fecha |
| date | Fecha |
| year | Año |
| quarter | Quarter |
| month | Mes |
| month_name | Nombre mes |
| week | Semana |
| iso_year | ISO Year |
| semana_bimbo | Semana Bimbo |
| year_semana_bimbo | Año semana Bimbo |
| day | Día |
| day_of_week | Día semana |
| day_name | Nombre día |
| is_weekend | Indicador weekend |

---

# Semantic Layer

La semantic layer consolida todo el modelo analítico empresarial.

---

## Motor

```text
DuckDB
```

---

## Vista Principal

```sql
vw_sales_enriched
```

---

# Relaciones

```text
FACT SALES
    LEFT JOIN
DIM PRODUCTO
    ON producto_id

FACT SALES
    LEFT JOIN
DIM AGENCIA
    ON agencia_id

FACT SALES
    LEFT JOIN
DIM DATE
    ON fecha
```

---

# Resultado Semantic Layer

La vista enriquecida contiene:

- histórico completo
- granularidad diaria
- atributos producto
- atributos agencia
- atributos calendario
- estructura analítica empresarial

---

# Data Marts

Los marts consumen exclusivamente:

```text
vw_sales_enriched
```

---

# mart_sales_monthly

Granularidad:

```text
Year / Month
```

Objetivo:

- ventas mensuales
- tendencias
- dashboards ejecutivos

---

# mart_brand_performance

Granularidad:

```text
Year / Month / Marca
```

Objetivo:

- performance marcas
- market share
- rankings

---

# mart_daily_sales

Granularidad:

```text
Diaria
```

Objetivo:

- freshness
- monitoreo operacional
- última fecha disponible

---

# Reglas Oficiales Modelo

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

# Beneficios del Modelo

## Escalabilidad

- crecimiento incremental
- histórico multi-año
- warehouse enterprise

---

## Performance

- marts optimizados
- particionamiento
- menor lectura

---

## Gobernanza

- trazabilidad
- desacoplamiento
- mantenibilidad

---

## Analítica

El modelo habilita:

- dashboards enterprise
- forecasting
- anomaly detection
- semantic KPIs
- AI analytics

---

# Estado Modelo

## V4 COMPLETADA

La V4 consolida oficialmente:

- modelo dimensional enterprise
- warehouse particionado
- semantic layer desacoplada
- marts optimizados
- granularidad diaria

Estado oficial:

```text
STABLE
```

---