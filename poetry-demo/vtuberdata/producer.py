import importlib
import sys

from loguru import logger

from vtuberdata.backend.db import (
    clients,
    router,
)
from vtuberdata.tasks.task import crawler


def Update(dataset: str):
    period_day = clients.check_history(clients.get_mysql_vtuberdata_conn())
    # 拿取每個爬蟲任務的參數列表，
    # 資料來源 data_source，例如 vtsc
    parameter_list = getattr(
        importlib.import_module(f"vtuberdata.crawler.{dataset}"),
        "period_list",
    )(period = period_day[0], start_day = period_day[1])
    # 用 for loop 發送任務
    for parameter in parameter_list:
        logger.info(f"{dataset}, {parameter}")
        task = crawler.s(dataset, parameter)
        # queue 參數，可以指定要發送到特定 queue 列隊中
        task.apply_async(queue=parameter.get("data_source", ""))

    #router.close_connection()


if __name__ == "__main__":
    (
        dataset,
    ) = sys.argv[1:]
    Update(dataset)