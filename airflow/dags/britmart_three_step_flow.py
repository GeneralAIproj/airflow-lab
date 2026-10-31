from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
 
with DAG(
    dag_id="britmart_three_step_flow",
    start_date=datetime(2026, 8, 1),
    schedule=None,
    catchup=False,
) as dag:
 
    extract = BashOperator(
        task_id="extract",
        bash_command="echo extract",
    )
 
    clean = BashOperator(
        task_id="clean",
        bash_command="echo clean",
    )
 
    report = BashOperator(
        task_id="report",
        bash_command="echo report",
    )
 
    extract >> clean >> report