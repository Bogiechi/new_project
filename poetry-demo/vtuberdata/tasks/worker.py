from celery import Celery
from vtuberdata.config import (
    WORKER_ACCOUNT,
    WORKER_PASSWORD,
    MESSAGE_QUEUE_HOST,
    MESSAGE_QUEUE_PORT,
)

broker = (
    f"pyamqp://{WORKER_ACCOUNT}:{WORKER_PASSWORD}@"
    f"{MESSAGE_QUEUE_HOST}:{MESSAGE_QUEUE_PORT}/"
)
app = Celery(
    "task",
    include=["vtuberdata.tasks.task"],
    broker=broker,
)