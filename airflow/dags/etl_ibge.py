from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from etl.extract import fake_ibge_data
from etl.transform import clean_ibge_data
from etl.load import load_to_postgres

with DAG('etl_ibge',
         start_date=datetime(2023, 1, 1),
         schedule_interval='@daily',
         catchup=False) as dag:

    extract = PythonOperator(
        task_id='extract',
        python_callable=fake_ibge_data.main
    )

    transform = PythonOperator(
        task_id='transform',
        python_callable=clean_ibge_data.main
    )

    load = PythonOperator(
        task_id='load',
        python_callable=load_to_postgres.main
    )

    extract >> transform >> load
