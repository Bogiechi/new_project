import datetime

from airflow.operators.python_operator import (
    PythonOperator,
)

from dataflow.backend import db
from dataflow.crawler.Vtuber_SuperChat import (
    crawler,
)


def crawler_Vtuber_SuperChat_vtsc():
    # 進行爬蟲
    df = crawler()
    # 資料上傳資料庫
    db.upload_data(
        df,
        "VtuberSuperChat",
        db.clients.get_mysql_vtuberdata_conn(),
    )

def create_crawler_Vtuber_SuperChat_task() -> PythonOperator:
    return [
        # 建立任務
        PythonOperator(
            task_id="Vtuber_SuperChat_vtsc",
            python_callable=crawler_Vtuber_SuperChat_vtsc,
            queue="vtsc",
            provide_context=True,
        ),
    ]