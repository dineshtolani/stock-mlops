from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Import your pipeline functions
from src.data_ingestion import download_stock_data
from src.data_cleaning import clean_stock_data
from src.feature_engineering import add_features
from src.train_model import train_model

# Default DAG arguments
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2020, 1, 1),
    "retries": 1,
}

# Define DAG
with DAG(
    dag_id="stock_pipeline",
    default_args=default_args,
    schedule_interval="@daily",  # Run daily
    catchup=False,
) as dag:

    # Task 1: Ingest data
    ingest_task = PythonOperator(
        task_id="ingest_data",
        python_callable=download_stock_data,
        op_kwargs={"symbol": "RELIANCE.NS", "start": "2020-01-01"},
    )

    # Task 2: Clean data
    clean_task = PythonOperator(
        task_id="clean_data",
        python_callable=clean_stock_data,
        op_kwargs={"filepath": "data/raw/RELIANCE.NS.csv"},
    )

    # Task 3: Feature engineering
    feature_task = PythonOperator(
        task_id="feature_engineering",
        python_callable=add_features,
        op_kwargs={"filepath": "data/processed/RELIANCE.NS_clean.csv"},
    )

    # Task 4: Train model
    train_task = PythonOperator(
        task_id="train_model",
        python_callable=train_model,
        op_kwargs={"filepath": "data/features/RELIANCE.NS_features.csv"},
    )

    # Define pipeline order
    ingest_task >> clean_task >> feature_task >> train_task
