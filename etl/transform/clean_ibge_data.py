import pandas as pd
import os

def main():
    df = pd.read_csv("data/raw/ibge_fake.csv")
    df.columns = [col.lower().strip() for col in df.columns]
    df.to_csv("/opt/airflow/data/processed/ibge_clean.csv", index=False)
    print("IBGE data cleaned and saved.")
