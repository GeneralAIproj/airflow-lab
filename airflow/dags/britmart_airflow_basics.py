from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
 
with DAG(
    dag_id="britmart_airflow_basics",
    start_date=datetime(2026, 8, 1),
    schedule=None,
    catchup=False,
) as dag:
 
    extract_orders = BashOperator(
        task_id="extract_orders",
        bash_command="echo extracting orders",
    )
 
    validate_orders = BashOperator(
        task_id="validate_orders",
        bash_command="echo validating orders",
    )
 
    extract_orders >> validate_orders