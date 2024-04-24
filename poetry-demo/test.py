from sqlalchemy import (
    create_engine,
    engine,
    text,
)

import pandas as pd
import datetime
import datetime
import time
import typing

def get_mysql_financialdata_conn() -> engine.base.Connection:
    address = "mysql+pymysql://root:test@localhost:3306/vtuberdata"
    engine = create_engine(address)
    connect = engine.connect()
    return connect


def check_history(
    mysql_conn: engine.base.Connection,
):
    df = pd.read_sql(text("SELECT max(period) as p, max(start_date) as sd FROM VtuberSuperChat"), con=mysql_conn)
    period = df['p'][0]
    start_day = df['sd'][0]
    print("y")
    print(period)
    if not(df['p'][0]):
        period = '1708905600'
        start_day = '2/26/2024'
        print("n")
    date_format = '%m/%d/%Y'
    start_day = datetime.datetime.strptime(start_day, date_format)
    
    today = datetime.datetime.today()
    result = today - start_day
    w = int(result.days)//7
    day_list = [
        int(period) + week*604800
        for week in range(1, w)
    ]
    date_list = [
        dict(
            period = str(d),
            data_source = data_source,
        )
        for d in day_list
        for data_source in [
            "vtsc",
        ]
    ]
    print(date_list)

if __name__ == "__main__":
    check_history(get_mysql_financialdata_conn())