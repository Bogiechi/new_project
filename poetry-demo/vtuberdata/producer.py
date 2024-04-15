import importlib
import sys

from loguru import logger

from vtuberdata.backend import db
from vtuberdata.tasks.task import crawler


def Update(dataset: str):
    period_day = db.clients.check_history(get_mysql_financialdata_conn())
    # 拿取每個爬蟲任務的參數列表，
    # 包含爬蟲資料的日期 date，例如 2021-04-10 的台股股價，
    # 資料來源 data_source，例如 twse 證交所、tpex 櫃買中心
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


if __name__ == "__main__":
    dataset = sys.argv[1:]
    Update(dataset)