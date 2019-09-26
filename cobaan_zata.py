"""
Buat Airflow DAG dengan nama: exercise_{nama}
yang dimulai pada tanggal: 27 September 2019 
Schedule akan berjalan pada: jam setengah 4 pagi di hari kerja saja
dengan bentuk DAG seperti DAG_exercise2.PNG
"""

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'zataqu',
    'depends_on_past': False,
    'start_date': datetime(2019, 9, 27),
    'email': ['zataqu@ag-it.com'],
    'email_on_failure': False,
    'email_on_retry': False,
}

dag = DAG('exercise_zataqu', default_args=default_args, schedule_interval='30 3 * * 1-5')

t1 = BashOperator(
    task_id='task_1',
    bash_command='ngasal_inimah',
    dag=dag)

i = 0
    
while i < 100:
    BashOperator(
    task_id='task_{}'.format(i),
    bash_command='ngasal_inimah',
    dag=dag)
    i+=1
    