import pandas as pd
import os

BASE_PATH = "/opt/airflow/data"

def main():
    raw_path = os.path.join(BASE_PATH, "raw")
    file_path = os.path.join(raw_path, "ibge_fake.csv")
    
    df = pd.read_csv(file_path)
    print(f"IBGE data read from {file_path} with {len(df)} records")
