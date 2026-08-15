# End-to-End ETL & Data Quality Pipeline

A portfolio project demonstrating practical ETL, Python, SQL Server, data validation, reconciliation, and data-quality testing.

## Project Overview

This project implements an end-to-end ETL and data-quality workflow using Python and SQL Server.

The pipeline extracts synthetic customer and order data from CSV files, performs data standardization and validation using Python, loads the transformed data into SQL Server, and executes SQL-based data-quality checks to identify potential data issues.

The project demonstrates practical skills relevant to:

- Data Engineering
- ETL / Data Integration
- Data Testing
- Data Quality
- SQL Development
- Data Validation
- Data Reconciliation
- Python Data Processing

## Architecture

CSV Source Files
       |
       v
+------------------+
| Python ETL       |
|                  |
| Extract          |
| Transform        |
| Validate         |
| Load             |
+------------------+
       |
       v
SQL Server Database
       |
       v
Data Quality Checks
       |
       +----------------------+
       |                      |
       v                      v
Duplicate Checks       Null / Invalid Data
       |                      |
       +----------+-----------+
                  |
                  v
        Reconciliation Results

## ETL Workflow

### 1. Extract

The pipeline reads synthetic customer and order datasets from CSV files using Python and Pandas.

Source files:

- data/customers.csv
- data/orders.csv

### 2. Transform

The Python ETL process performs data standardization and transformation, including:

- Date parsing and standardization
- Handling invalid or missing dates
- Text normalization
- Status standardization
- Numeric conversion for amount fields
- Data validation before loading

### 3. Load

The transformed datasets are loaded into SQL Server staging tables.

Target staging tables:

- stg_customers
- stg_orders

### 4. Data Quality Validation

SQL-based validation rules identify common data-quality issues, including:

- Duplicate order IDs
- Missing order dates
- Non-positive order amounts
- Potential orphan customer records
- Customer-to-order row-count reconciliation

## Example Data Quality Results

The sample dataset intentionally contains data-quality issues to demonstrate validation.

Example findings include:

| Data Quality Check | Result |
|---|---|
| Duplicate Order IDs | Detected |
| Missing Order Dates | Detected |
| Non-positive Amounts | Detected |
| Orphan Customer IDs | Detected |
| Customer / Order Row Counts | Reconciled |

## Project Structure

etl-data-quality-pipeline/
|
├── data/
│   ├── customers.csv
│   └── orders.csv
|
├── docs/
│   └── data_quality_rules.md
|
├── python/
│   └── etl_pipeline.py
|
├── sql/
│   ├── 01_create_schema.sql
│   └── 02_data_quality_checks.sql
|
├── .gitignore
├── README.md
└── requirements.txt

## Technologies Used

- Python
- Pandas
- PyODBC
- SQL Server
- T-SQL
- SQL Server Express
- Git
- GitHub
- PowerShell

## Python Responsibilities

The Python ETL component handles:

- CSV extraction
- Data transformation
- Data type standardization
- Date validation
- Numeric validation
- Data preparation
- SQL Server connectivity
- Loading transformed data into staging tables

## SQL Responsibilities

The SQL component handles:

- Database and table creation
- Staging table management
- Data-quality validation
- Duplicate detection
- Null / missing-value detection
- Invalid amount detection
- Referential data checks
- Row-count reconciliation

## Running the Project

### Prerequisites

Install:

- Python 3.x
- SQL Server / SQL Server Express
- ODBC Driver for SQL Server
- Git

### 1. Clone the repository

git clone https://github.com/prashanth050492/etl-data-quality-pipeline.git
cd etl-data-quality-pipeline

### 2. Create a Python virtual environment

python -m venv .venv

Activate it in PowerShell:

.\.venv\Scripts\Activate.ps1

### 3. Install dependencies

pip install -r requirements.txt

### 4. Create the SQL Server database

sqlcmd -S "localhost\SQLEXPRESS" -E -i ".\sql\01_create_schema.sql"

### 5. Run the ETL pipeline

.\.venv\Scripts\python.exe ".\python\etl_pipeline.py"

Expected output includes extraction statistics, data-quality findings, and confirmation of the ETL load.

### 6. Run data-quality checks

sqlcmd -S "localhost\SQLEXPRESS" -E -d ETLDataQuality -i ".\sql\02_data_quality_checks.sql"

## Skills Demonstrated

### Data Engineering

- ETL Pipelines
- Data Transformation
- Data Processing
- Data Validation
- Data Reconciliation
- Data Quality

### Programming

- Python
- Pandas
- PyODBC
- SQL
- T-SQL

### Testing & Quality

- Data Quality Testing
- Validation Rules
- Duplicate Detection
- Null Validation
- Referential Checks
- Row-Count Reconciliation

### Database

- SQL Server
- SQL Server Express
- Staging Tables
- Database Schema
- SQL Queries

### Development Tools

- Git
- GitHub
- PowerShell
- Python Virtual Environments

## Key Takeaways

This project demonstrates the ability to build and validate a complete data pipeline rather than focusing only on database administration.

It combines Python-based ETL, SQL Server development, automated data-quality validation, and reconciliation into a single practical workflow.

## Author

Prashanth Vollala

Data & AI | ETL / Data Testing | SQL | Data Quality | Python | Data Pipelines | AI Evaluation