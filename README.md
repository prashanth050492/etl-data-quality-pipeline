# End-to-End ETL & Data Quality Pipeline

A portfolio project demonstrating practical ETL, Python, SQL Server, data validation, reconciliation, and data-quality testing.

## Objective

Build a small but realistic data pipeline that:
1. Extracts source CSV files.
2. Cleans and transforms the data with Python.
3. Loads curated data into SQL Server.
4. Runs data-quality checks.
5. Produces a validation report.

The source data intentionally contains common quality issues such as duplicates, missing values, invalid foreign keys, negative amounts, and inconsistent status values.

## Architecture

Source CSV -> Python ETL -> SQL Server staging -> Curated tables -> Data-quality checks -> Validation report

## Skills demonstrated

- Python
- Pandas
- ETL / ELT concepts
- SQL Server / T-SQL
- Data validation
- Data quality
- Source-to-target reconciliation
- Duplicate detection
- Referential-integrity checks
- Transformation and standardization
- Git/GitHub-ready project structure

## Project structure

```text
etl_data_quality_pipeline/
├── data/
│   ├── customers.csv
│   └── orders.csv
├── python/
│   └── etl_pipeline.py
├── sql/
│   ├── 01_create_schema.sql
│   └── 02_data_quality_checks.sql
├── docs/
│   └── data_quality_rules.md
├── requirements.txt
└── README.md
```

## Run locally

### 1. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure SQL Server

Create a database named `ETLDataQuality` and update the connection string in `python/etl_pipeline.py`.

### 3. Create tables

Run:

```text
sql/01_create_schema.sql
```

### 4. Run the ETL

```bash
python python/etl_pipeline.py
```

### 5. Run data-quality checks

Execute:

```text
sql/02_data_quality_checks.sql
```

## Important

This is a synthetic portfolio project. It is designed to demonstrate technical skills and testing methodology; it does not represent confidential client data or production systems.
