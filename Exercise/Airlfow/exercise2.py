"""
Buat Airflow DAG dengan nama: exercise1_{nama}
(Fokus pada dag)

buat 100 task secara serial dengan penamaan dan output di command line:
task_id  | output CLI

task_1   | Ini task nomor 1
task_2   | Ini task nomor 2
...
task_100 | Ini task nomor 100

dengan bentuk DAG seperti DAG_exercise2.PNG
"""

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': '{nama}',
    'depends_on_past': False,
    'start_date': datetime(2019, 9, 18),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
}

dag = DAG('exercise2_{nama}', default_args=default_args, schedule_interval='')