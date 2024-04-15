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


def get_mysql_financialdata_conn() -> engine.base.Connection:
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
    df = pd.read_sql(text("SELECT max(period) as p FROM VtuberSC"), con=mysql_conn)
    if not(df['p'][0]):
        period = 1610928000
        start_day = datetime.date(2021, 1, 18)
    period = df[]
    start_day = df[]
    return[period, start_day]