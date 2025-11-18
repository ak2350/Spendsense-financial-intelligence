import duckdb
import os

# Connect or create DB in project root
con = duckdb.connect("spendsense.duckdb")

# Load CSV into DuckDB
con.execute("""
    CREATE TABLE IF NOT EXISTS transactions AS
    SELECT *
    FROM read_csv_auto('data/raw/synthetic_financial_data.csv', header=True);
""")

print("DuckDB setup complete. Table 'transactions' created.")

