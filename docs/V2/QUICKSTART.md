# SALES DWH - Quickstart

Autor: Jonathan Elgueta Elgueta  
Versión: V2.0.0  
Estado: STABLE

---

# Descripción

Este documento explica cómo ejecutar el proyecto Sales DWH desde cero.

La arquitectura V2 implementa:

- warehouse particionado
- procesamiento incremental
- metadata orchestration
- semantic layer desacoplada
- marts analíticos
- QA operacional

---

# Requisitos

Antes de comenzar se requiere:

- Python 3.11+
- DuckDB
- Pandas
- PyArrow
- Virtual Environment
- Archivos XLSX de ventas

---

# Estructura Esperada

```text
sales-dwh/

├── data/
│
│   ├── raw/
│   ├── warehouse/
│   ├── marts/
│   ├── metadata/
│   └── duckdb/
│
├── docs/
├── outputs/
├── src/
└── venv/
```

---

# 1. Crear Entorno Virtual

Ubicarse en:

```bash
C:\sales-dwh
```

Crear entorno virtual:

```bash
python -m venv venv
```

---

# 2. Activar Entorno Virtual

## Windows PowerShell

```bash
venv\Scripts\activate
```

Resultado esperado:

```bash
(venv) PS C:\sales-dwh>
```

---

# 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

---

# 4. Inicializar Metadata

Este proceso:

- detecta archivos XLSX
- construye metadata inicial
- define ACTIVE
- crea processed_files.parquet

Comando:

```bash
python -m src.orchestration.initialize_metadata
```

---

# 5. Validar Metadata

Este proceso valida:

- existencia ACTIVE
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

# 6. Ejecutar Incremental

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

---

# 7. Crear Semantic Layer

Este proceso:

- genera vw_sales_enriched
- centraliza joins dimensionales
- desacopla marts del storage físico

Comando:

```bash
python -m src.semantic.create_views
```

Resultado esperado:

```text
7406100 registros
```

---

# 8. Construir Marts

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

---

# 9. Ejecutar QA

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
- quarter
- calendario
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

# Flujo Operacional Completo

```text
RAW XLSX
    ↓

METADATA
    ↓

INCREMENTAL
    ↓

WAREHOUSE
    ↓

SEMANTIC
    ↓

MARTS
    ↓

QA
```

---

# Resultado Final Esperado

Al finalizar exitosamente:

- warehouse actualizado
- metadata validada
- semantic layer operativa
- marts generados
- QA validado
- incremental estable

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