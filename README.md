# Data Engineering & Analytics Platform

A portfolio-grade data engineering project demonstrating a complete local ETL workflow: ingestion, validation, transformation, PostgreSQL loading, analytical SQL, and an interactive dashboard.

## Architecture
```text
CSV Source → Python ETL → Validation/Cleaning → PostgreSQL → Analytical SQL → Streamlit Dashboard
```

## Features
- Python ETL pipeline
- Data validation and quality reporting
- Data cleaning and transformation
- PostgreSQL relational modeling
- Analytical SQL for KPIs, trends, regions and products
- Dockerized PostgreSQL
- GitHub Actions CI
- Interactive Streamlit dashboard
- Synthetic dataset with no private data

## Run
```bash
docker compose up -d db
python -m venv .venv
# Git Bash
source .venv/Scripts/activate
# CMD
.venv\Scripts\activate
pip install -r requirements.txt
python -m pipeline.etl
streamlit run dashboard/app.py
```

Dashboard: `http://localhost:8501`

Database: `postgresql://analytics:analytics@localhost:5434/analytics_db`

## Project Structure
```text
├── .github/workflows/ci.yml
├── data/sales.csv
├── dashboard/app.py
├── pipeline/
│   ├── config.py
│   ├── db.py
│   ├── quality.py
│   └── etl.py
├── sql/analytics.sql
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

## Engineering Decisions
PostgreSQL provides relational storage while SQL handles repeatable analytical workloads. Validation is performed before loading, and the pipeline calculates revenue during transformation. The database uses indexes on common analytical dimensions.

## Production Roadmap
Airflow/Dagster orchestration, dbt, object storage, warehouse/lakehouse, incremental CDC, schema migrations, partitioning, retries, secrets management, observability, lineage and managed deployment.

## Portfolio Summary
**Data Engineering & Analytics Platform** — Built a Python ETL pipeline with validation, transformation and PostgreSQL loading, analytical SQL, data-quality checks, Dockerized infrastructure, GitHub Actions CI and an interactive Streamlit dashboard.
