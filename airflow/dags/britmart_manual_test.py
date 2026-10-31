from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
 
with DAG(
    dag_id="britmart_manual_test",
    start_date=datetime(2026, 8, 1),
    schedule=None,
    catchup=False,
) as dag:
 
    show_message = BashOperator(
        task_id="show_message",
        bash_command="echo 'BritMart manual test'",
    )