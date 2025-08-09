import pandas as pd
import psycopg2
import os

BASE_PATH = "/opt/airflow/data"

def main():
    processed_file = os.path.join(BASE_PATH, "processed", "ibge_clean.csv")
    df = pd.read_csv(processed_file)

    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB", "agroweather"),
        user=os.getenv("POSTGRES_USER", "admin"),
        password=os.getenv("POSTGRES_PASSWORD", "admin"),
        host="postgres",  # service name in docker-compose
        port="5432"
    )

    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS agricultural_production (
        year INT,
        municipality VARCHAR,
        state CHAR(2),
        crop VARCHAR,
        harvested_area_ha FLOAT,
        production_ton FLOAT,
        value_thousand_reais FLOAT
    );
    """)

    for _, row in df.iterrows():
        cur.execute("""
        INSERT INTO agricultural_production (year, municipality, state, crop, harvested_area_ha, production_ton, value_thousand_reais)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, tuple(row))

    conn.commit()
    cur.close()
    conn.close()

    print("Data loaded into PostgreSQL.")
