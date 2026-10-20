[en English](#english) | [🇷🇺 Русский](#русский)
<a id="english"></a>
# ⚙️ETL Pipeline — Fake Store API🛒

ETL project that extracts data from the free public REST API (Fake Store API), transforms it with Python and Pandas, stores it in PostgreSQL, and visualizes insights in Power BI.

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

## 🗄️ Database schema

![Database schema](images/df_schema.png")

## 📊 Dashboard Preview

![Product Analytics Dashboard](dashboards/etl_project_dashboard_en.png)

## 🔗 Data Source

- [Fake Store API](https://fakestoreapi.com/)

<a id="Русский"></a>
# ⚙️ETL Пайплайн — Fake Store API🛒

В данном проекте строится ETL пайплайн, который извлекает данные из бесплатного публичного REST API (Fake Store API), трансформирует их в Python, переносит в БД с помощью PostgreSQL и строит аналитический дашборд в Power BI.

## 🔄 Пайплайн

```mermaid
flowchart TD
    A["🛒 Fake Store API<br/>Товары · Корзины · Покупатели"]
    B["📥 Извлечение из API"]
    C["⚙️ Трансформация<br/>Python · Pandas"]
    D["📦 Загрузка<br/>PostgreSQL"]
    E["📊 Анализ и Визуализация<br/>Power BI"]

    A --> B --> C --> D --> E

    classDef source fill:#DCEEFF,stroke:#4285C5,color:#17365D
    classDef process fill:#FFF0D9,stroke:#D99A2B,color:#704600
    classDef output fill:#DDF5E5,stroke:#45A36B,color:#174D2B

    class A source
    class B,C,D process
    class E output
```

## 🛠️ Стек

- 🌐 **Fake Store API** — Источник данных
- 🐍 **Python & Pandas** — Извлечение днных и трансформация
- 🐘 **PostgreSQL** — Управление БД
- 📊 **Power BI** — Визуализация
- 🔧 **Git & GitHub** — Контроль версий

## 🗄️ Схема базы данных

![Схема базы данных](images/df_schema.png)

## 📊 Дашборд

![Дашборд](dashboards/etl_project_dashboard_ru.png)

## 🔗 Источник данных

- [Fake Store API](https://fakestoreapi.com/)