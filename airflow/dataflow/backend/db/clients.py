from vtuberdata.config import (
    MYSQL_DATA_USER,
    MYSQL_DATA_PASSWORD,
    MYSQL_DATA_HOST,
    MYSQL_DATA_PORT,
    MYSQL_DATA_DATABASE,
)
from sqlalchemy import (
    create_engine,
    engine,
    text,
)

import pandas as pd
import datetime


def get_mysql_vtuberdata_conn() -> engine.base.Connection:
    address = (
        f"mysql+pymysql://{MYSQL_DATA_USER}:{MYSQL_DATA_PASSWORD}"
        f"@{MYSQL_DATA_HOST}:{MYSQL_DATA_PORT}/{MYSQL_DATA_DATABASE}"
    )
    engine = create_engine(address)
    connect = engine.connect()
    return connect