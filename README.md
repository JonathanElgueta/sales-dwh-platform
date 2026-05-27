# 🚀 SALES DWH PLATFORM

Enterprise Analytics Platform powered by:

- Incremental ETL
- Partitioned Data Warehouse
- Semantic Layer
- Analytics Data Marts
- Streamlit Enterprise Dashboards
- AI Analytics Foundation

---

# 📌 Current Version

| Version | Status | Description |
|---|---|---|
| V1 | CLOSED | Initial Analytics Prototype |
| V2 | CLOSED | Enterprise Dashboard Expansion |
| V3 | CLOSED | Semantic Layer + AI Foundation |
| V4 | STABLE | Partitioned Enterprise Warehouse + Incremental Architecture |

---

# 🧠 Platform Overview

Sales DWH Platform is an enterprise-grade analytics ecosystem designed to process, govern, enrich and visualize sales data through a modern multi-layer architecture.

The platform evolved from a dashboard prototype into a fully desacoplada enterprise analytics architecture capable of:

- Incremental XLSX ingestion
- Historical persistence
- Partitioned warehouse storage
- Semantic business modeling
- Analytics optimization
- Operational governance
- AI-ready analytics

---

# 🏗️ Official V4 Architecture

```text
RAW XLSX FILES
    ↓
INCREMENTAL ETL PIPELINE
    ↓
PARTITIONED DATA WAREHOUSE
    ↓
DIMENSIONAL MODEL
    ↓
SEMANTIC LAYER (DuckDB Views)
    ↓
ANALYTICS DATA MARTS
    ↓
ENTERPRISE ANALYTICS APPLICATION
```

---

# ⚙️ Enterprise Architecture Principles

## FACTS = RAW TRANSACTIONS

Facts store only:

- transactional data
- daily granularity
- operational metrics

Facts NEVER contain:

- joins
- KPIs
- business logic
- dimensional enrichments

---

## DIMENSIONS = BUSINESS ATTRIBUTES

Dimensions centralize:

- product metadata
- calendar intelligence
- business hierarchies
- enterprise attributes

---

## SEMANTIC LAYER = BUSINESS LOGIC

The Semantic Layer centralizes:

- joins
- enrichments
- enterprise semantics
- analytical logic

Main enterprise view:

```sql
vw_sales_enriched
```

---

## MARTS = ANALYTICS OPTIMIZATION

Marts are generated exclusively from:

```text
Semantic Layer
```

Marts NEVER consume raw facts directly.

---

## APP = VISUALIZATION & OPERATIONS

The Streamlit application consumes only:

```text
Analytics Data Marts
```

---

# 📂 Enterprise Project Structure

```text
sales-dwh/
│
├── data/
│   │
│   ├── raw/
│   │   └── sales/
│   │
│   ├── warehouse/
│   │   │
│   │   ├── facts/
│   │   │   └── sales/
│   │   │       └── year=YYYY/month=MM/
│   │   │
│   │   └── dimensions/
│   │       ├── products/
│   │       ├── agencies/
│   │       └── date/
│   │
│   ├── duckdb/
│   │   └── sales_dwh.duckdb
│   │
│   ├── marts/
│   │
│   ├── metadata/
│   │
│   └── logs/
│
├── docs/
│   ├── V1/
│   ├── V2/
│   ├── V3/
│   └── V4/
│
├── src/
│   ├── app/
│   ├── config/
│   └── services/
│
└── outputs/
```

---

# 🏢 Enterprise Features

## ✅ Incremental ETL

Supports:

- incremental XLSX ingestion
- partition updates
- historical persistence
- automatic mart regeneration

---

## ✅ Partitioned Warehouse

Official partition strategy:

```text
year=YYYY/month=MM
```

Example:

```text
data/warehouse/facts/sales/year=2026/month=05/data.parquet
```

---

## ✅ Semantic Layer

Enterprise semantic architecture based on:

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
```

---

## ✅ Analytics Data Marts

Current marts:

| Mart | Purpose |
|---|---|
| mart_sales_monthly | Monthly analytics |
| mart_brand_performance | Brand analytics |
| mart_daily_sales | Daily freshness |

---

## ✅ Enterprise Governance

Includes:

- authentication
- role-based access
- audit logs
- QA monitoring
- pipeline monitoring

---

## ✅ Daily Granularity

The platform now supports:

- daily operational monitoring
- real freshness tracking
- transaction-level analytics

---

# 📊 Enterprise Modules

| Module | Description |
|---|---|
| Home | Executive KPIs |
| Executive Dashboard | Enterprise analytics |
| Brand Analytics | Brand performance |
| Pipeline Monitor | Incremental ETL execution |
| QA Monitor | Data quality monitoring |
| AI Forecasting | Forecasting foundation |
| AI Anomaly Detection | Operational anomaly monitoring |

---

# 🧪 QA Layer

The QA Engine validates:

- required columns
- null values
- duplicate records
- invalid dates
- negative sales

Pipeline rule:

```text
NO FILE ENTERS THE WAREHOUSE WITHOUT QA VALIDATION
```

---

# 🔄 Incremental Enterprise Flow

```text
NEW XLSX FILE
    ↓
QA VALIDATION
    ↓
SCHEMA NORMALIZATION
    ↓
PARTITION UPDATE
    ↓
SEMANTIC REFRESH
    ↓
MART REGENERATION
    ↓
CACHE REFRESH
    ↓
DASHBOARD UPDATE
```

---

# 🧠 Semantic Layer Architecture

The semantic layer centralizes:

- joins
- business rules
- enrichments
- analytical structure

Main enterprise view:

```sql
vw_sales_enriched
```

---

# 📦 Historical Rebuild

V4 successfully rebuilt:

```text
2023 → 2026 historical sales
```

With more than:

```text
7.5M rows
```

processed successfully.

---

# 🚀 Getting Started

## 1. Clone Repository

```bash
git clone <repository>
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Run Application

```bash
streamlit run src/app/app.py
```

---

# 🔐 Default Users

| User | Password | Role |
|---|---|---|
| admin | admin123 | admin |
| qa_user | qa123 | qa |
| ejecutivo_user | exec123 | ejecutivo |
| ops_user | ops123 | operaciones |

---

# 📚 Documentation

Complete enterprise documentation available in:

```text
docs/V4/
```

Includes:

- Architecture
- Data Model
- Pipeline
- Semantic Layer
- Data Marts
- QA Layer
- Governance
- Incremental Architecture
- V5 Roadmap

---

# 🛣️ V5 Roadmap

Next evolution:

```text
AI-Driven Enterprise Analytics Platform
```

Future capabilities:

- Semantic KPI Engine
- Enterprise Orchestration
- AI Forecasting
- Advanced Anomaly Detection
- Enterprise Alerting
- Observability Layer
- Semantic Governance
- Predictive Analytics

---

# 🏁 Current Platform Status

## SALES DWH PLATFORM V4

```text
STABLE
```

Architecture officially consolidated:

```text
RAW XLSX
    ↓
INCREMENTAL ETL
    ↓
PARTITIONED WAREHOUSE
    ↓
SEMANTIC LAYER
    ↓
DATA MARTS
    ↓
ENTERPRISE ANALYTICS APP
```

---

# 👨‍💻 Author

Jonathan Elgueta Elgueta

---

# 📌 Final Status

```text
V4 OFFICIALLY CLOSED
```