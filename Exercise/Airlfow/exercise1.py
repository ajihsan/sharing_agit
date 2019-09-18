"""
Buat Airflow DAG dengan nama: exercise1_{nama}
yang dimulai pada tanggal: 27 September 2019 
Schedule akan berjalan pada: jam setengah 4 pagi di hari kerja saja
dengan bentuk DAG seperti DAG_exercise1.PNG
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

dag = DAG('exercise1_{nama}', default_args=default_args, schedule_interval='')