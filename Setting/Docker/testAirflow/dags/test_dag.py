
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
import pendulum

local_tz = pendulum.timezone("Asia/Seoul")

default_args = {
    'owner': 'admin',
}

dag = DAG(
    dag_id='test_dag',
    default_args=default_args,
    start_date=days_ago(0.1).replace(tzinfo=local_tz),
    dagrun_timeout=timedelta(hours=30),
    schedule_interval='10 0 * * *',
    catchup=False
)

test1 = BashOperator(
    task_id="test1",
    bash_command=f'python /opt/airflow/dags/pyfile/test1.py',
    dag=dag)

test2 = BashOperator(
    task_id="test2",
    bash_command=f'python /opt/airflow/dags/pyfile/test2.py',
    dag=dag)

test1 >> test2
if __name__ == "__main__":
    dag.cli()
