import time
import datetime

from apscheduler.schedulers.background import (
    BackgroundScheduler,
)
from vtuberdata.producer import (
    Update,
)
from loguru import logger


def sent_crawler_task():
    # 將此段，改成發送任務的程式碼
    # logger.info(f"sent_crawler_task {dataset}")
    Update(
        dataset="Vtuber_SuperChat",
    )


def main():
    scheduler = BackgroundScheduler(
        timezone="Asia/Taipei"
    )
    # 與 crontab 類似，設定何時執行，有小時、分鐘、秒參數，* 星號代表任意時間點
    scheduler.add_job(
        id="sent_crawler_task",
        func=sent_crawler_task,
        trigger="cron",
        hour="15",
        minute="0",
        day_of_week="0",
    )
    logger.info("sent_crawler_task")
    scheduler.start()


if __name__ == "__main__":
    main()
    while True:
        time.sleep(600)