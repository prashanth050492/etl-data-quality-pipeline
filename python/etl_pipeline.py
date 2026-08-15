"""
End-to-End ETL & Data Quality Pipeline
Loads synthetic CSV data into SQL Server after basic standardization.
"""

from pathlib import Path
import pandas as pd
import pyodbc

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

# Replace with your local SQL Server connection details.
CONNECTION_STRING = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=ETLDataQuality;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

def transform_customers(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["customer_name"] = df["customer_name"].str.strip()
    df["email"] = df["email"].str.strip().str.lower()
    df["city"] = df["city"].str.strip()
    df["province"] = df["province"].str.upper().str.strip()
    return df

def transform_orders(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["status"] = df["status"].str.strip().str.title()
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    return df

def main():
    customers = pd.read_csv(DATA / "customers.csv")
    orders = pd.read_csv(DATA / "orders.csv")

    customers = transform_customers(customers)
    orders = transform_orders(orders)

    print("Customers extracted:", len(customers))
    print("Orders extracted:", len(orders))
    print("Orders with missing dates:", orders["order_date"].isna().sum())
    print("Orders with non-positive amounts:", (orders["amount"] <= 0).sum())
    print("Duplicate order IDs:", orders["order_id"].duplicated().sum())

    with pyodbc.connect(CONNECTION_STRING) as conn:
        cursor = conn.cursor()

        cursor.execute("TRUNCATE TABLE dbo.stg_customers;")
        cursor.execute("TRUNCATE TABLE dbo.stg_orders;")

        for row in customers.itertuples(index=False, name=None):
            cursor.execute(
                """INSERT INTO dbo.stg_customers
                   (customer_id, customer_name, email, city, province)
                   VALUES (?, ?, ?, ?, ?)""", row
            )

        for row in orders.itertuples(index=False, name=None):
            cursor.execute(
                """INSERT INTO dbo.stg_orders
                   (order_id, customer_id, order_date, status, amount)
                   VALUES (?, ?, ?, ?, ?)""", row
            )

        conn.commit()

    print("ETL load completed successfully.")

if __name__ == "__main__":
    main()
