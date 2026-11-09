from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from warehouse import initialize, load, aggregate

with DAG('daily_orders_warehouse',start_date=datetime(2026,1,1),schedule='@daily',catchup=False,
         tags=['data-engineering','portfolio']) as dag:
    init=PythonOperator(task_id='initialize',python_callable=initialize)
    stage=PythonOperator(task_id='load',python_callable=load)
    mart=PythonOperator(task_id='aggregate',python_callable=aggregate)
    init >> stage >> mart
