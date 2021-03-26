# Dat Schedulada para dados do Titanic
# Primeira DAG com Airflow

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.python_operator import BranchPythonOperator
from datetime import datetime, timedelta
import pandas  as pd
import random

# Argumentos Default
default_args = {
    'owner': 'Laís - IGTI',
    'depends_on_past': False,
    'start_date': datetime(2021, 3, 15, 23, 50),
    'email': ['lais.teles@hotmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

# Definição da DAG - Fluxo
dag = DAG(
    "treino-03",
    description="Paralelismos",
    default_args=default_args,
    schedule_interval='*/ * * * *'
)

start_preprocessing = BashOperator(
    task_id='start_preprocessing',
    bash_command='echo "Start Preprocessing ! Vai !"',
    dag=dag
)