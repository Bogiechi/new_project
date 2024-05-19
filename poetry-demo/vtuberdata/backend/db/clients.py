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


def check_history(
    mysql_conn: engine.base.Connection,
):
    df = pd.read_sql(text("SELECT max(period) as p, max(start_date) as sd FROM VtuberSuperChat"), con=mysql_conn)
    period = df['p'][0]
    start_day = df['sd'][0]

    if not(df['p'][0]):
        period = '1713744000'
        start_day = '4/22/2024'

    return[period, start_day]