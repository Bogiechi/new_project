import importlib
import typing

from vtuberdata.backend.db import db
from vtuberdata.backend.db import clients
from vtuberdata.tasks.worker import app


# 註冊 task, 有註冊的 task 才可以變成任務發送給 rabbitmq
@app.task()
def crawler(dataset: str, parameter: typing.Dict[str, str]):
    # 使用 getattr, importlib,
    # 根據不同 dataset, 使用相對應的 crawler 收集資料
    # 爬蟲
    df = getattr(
        importlib.import_module(f"vtuberdata.crawler.{dataset}"),
        "crawler",
    )(parameter=parameter)
    # 上傳資料庫
    db_dataset = dict(
        Vtuber_SuperChat="VtuberSuperChat",
    )
    db.upload_data(df, db_dataset.get(dataset), clients.get_mysql_vtuberdata_conn())