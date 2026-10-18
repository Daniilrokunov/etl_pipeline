
# 🛒 ETL Pipeline — Fake Store API

ETL project that extracts data from the Fake Store API, transforms it with Python and Pandas, stores it in PostgreSQL, and visualizes insights in Power BI.

## 🔄 ETL Pipeline

```mermaid
flowchart TD
    A["🛒 Fake Store API<br/>Products · Carts · Users"]
    B["📥 Extract<br/>API data extraction"]
    C["⚙️ Transform<br/>Python · Pandas"]
    D["📦 Load<br/>PostgreSQL"]
    E["📊 Analyze & Visualize<br/>Power BI"]

    A --> B --> C --> D --> E

    classDef source fill:#DCEEFF,stroke:#4285C5,color:#17365D
    classDef process fill:#FFF0D9,stroke:#D99A2B,color:#704600
    classDef output fill:#DDF5E5,stroke:#45A36B,color:#174D2B

    class A source
    class B,C,D process
    class E output
```

## 🛠️ Tech Stack

- 🌐 **Fake Store API** — data source
- 🐍 **Python & Pandas** — data extraction and transformation
- 🐘 **PostgreSQL** — data storage
- 📊 **Power BI** — data visualization
- 🔧 **Git & GitHub** — version control

## 📊 Dashboard Preview

![Product Analytics Dashboard](dashboards/product_analytics.png)

## 🔗 Data Source

- [Fake Store API](https://fakestoreapi.com/)

