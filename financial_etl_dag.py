from airflow import DAG
from datetime import datetime
with DAG('financial_etl_pipeline', start_date=datetime(2026,1,1), schedule='@daily'):
    pass
