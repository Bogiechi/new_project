import typing

import pandas as pd
import pymysql
from loguru import logger
from sqlalchemy import engine


def update2mysql_by_pandas(
    df: pd.DataFrame,
    table: str,
    mysql_conn: engine.base.Connection,
):
    if len(df) > 0:
        try:
            df.to_sql(
                name=table,
                con=mysql_conn,
                if_exists="append",
                index=False,
                chunksize=1000,
            )
        except Exception as e:
            logger.info(e)
            return False
    return True

def upload_data(
    df: pd.DataFrame,
    table: str,
    mysql_conn: engine.base.Connection,
):
    if len(df) > 0:
        # 直接上傳
        update2mysql_by_pandas(
            df=df,
            table=table,
            mysql_conn=mysql_conn,
        )