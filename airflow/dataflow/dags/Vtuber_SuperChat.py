import airflow

from dataflow.etl.Vtuber_SuperChat import (
    create_crawler_Vtuber_SuperChat_task,
)
from airflow.operators.dummy_operator import (
    DummyOperator,
)

with airflow.DAG(
    dag_id="Vtuber_SuperChat",
    # 設定每天 17:00 執行爬蟲
    schedule_interval="30 15 * * 2",
    max_active_runs=1,
    # 設定參數，Airflow 除了按按鈕，單純的執行外
    # 也可以在按按鈕時，帶入特定參數
    catchup=False,
) as dag:
    start_task = DummyOperator(
        task_id="start_task"
    )
    end_task = DummyOperator(
        task_id="end_task"
    )
    crawler_Vtuber_SuperChat_task = (
        create_crawler_Vtuber_SuperChat_task()
    )
    (
        start_task
        >> crawler_Vtuber_SuperChat_task
        >> end_task
    )