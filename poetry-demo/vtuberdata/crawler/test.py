import datetime
import time
import typing
from pydantic import BaseModel

import pandas as pd
from requests_html import HTMLSession
from loguru import logger
from tqdm import tqdm
from vtuberdata.backend.db.clients import get_mysql_financialdata_conn

class VtuberSuperChat(BaseModel):
    itemId: str
    period: int
    channelPlayCount: float
    subscriberCount: float
    subscriberFluc: float
    maxLiveViewer: float
    donationAmount: float
    donationCount: int
    rank: int
    rankFluc: str
    start_date: str
    end_date: str
    name: str

def check_schema(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """檢查資料型態, 確保每次要上傳資料庫前, 型態正確"""
    df_dict = df.to_dict("records")
    df_schema = [
        VtuberSuperChat(**dd).__dict__ # **字典的意思
        for dd in df_dict
    ]
    df = pd.DataFrame(df_schema)
    return df

def clean_data(
    df: pd.DataFrame,
) -> pd.DataFrame:

    df["rank"] = [
        df["index"][col]["rank"]
        for col in df.index
    ]
    
    key_to_check = "rankFluc"

    df["rankFluc"] = [
        str(df["index"][col]["rankFluc"])
        if key_to_check in df["index"][col]
        else
        'nope'
        for col in df.index
    ]

    df["name"] = [
        df["channel"][col]["name"]
        for col in df.index
    ]

    df["start_date"] = (
        df["date"]
        .str.split(" ")
        .str[0]
    )
    df["end_date"] = (
        df["date"]
        .str.split(" ")
        .str[2]
    )
    a = df["start_date"].str.split("/").str[2]
    b = df["end_date"] 
    if len(b[0])< 10:
        df["end_date"] = b+"/"+a
    
    df = df.drop(["index"], axis=1)
    df = df.drop(["channel"], axis=1)
    df = df.fillna(0.0)

    return df

def col_name(
    df: pd.DataFrame,
    colname: typing.List[str],
) -> pd.DataFrame:
    vtuber_data = {
        "itemId": "itemId",
        "period": "period",
        "pscore": "",
        "pplay": "",
        "plike": "",
        "pdislike": "",
        "channelPlayCount": "channelPlayCount",
        "channelPlayFluc": "",
        "subscriberCount": "subscriberCount",
        "subscriberFluc": "subscriberFluc",
        "maxLiveViewer": "maxLiveViewer",
        "donationAmount": "donationAmount",
        "donationCount": "donationCount",
        "index": "index",
        "channel": "channel",
        "videos": "",
    }
    df.columns = [
        vtuber_data[col]
        for col in colname
    ]
    df = df.drop([""], axis=1)
    return df

def crawler_twse(
    period: str,
) -> pd.DataFrame:
    # headers 中的 Request url
    url = (
            "https://api.playboard.co/v1/chart/channel"
            "?locale=en&countryCode=TW&period={period}&size=20&chartTypeId=10&periodTypeId=3&indexDimensionId=41&indexTypeId=3&indexTarget=v-tuber&indexCountryCode=JP"
        )
    url_date = (
            "https://playboard.co/en/youtube-ranking/most-superchatted-v-tuber-channels-in-japan-weekly?period={period}"
        )
    url = url.format(
        period = period
    )
    url_date = url_date.format(
        period = period
    )
    # request method
    session = HTMLSession()
    r = session.get(url)
    time.sleep(5)

    try:
        df = pd.DataFrame(r.json()["list"])# dataframe注意大小寫
        colname = df.columns
    except BaseException:
        return pd.DataFrame()
    
    if len(df) == 0:
        return pd.DataFrame()
    
    df = col_name(
        df.copy(), colname
    )

    r = session.get(url_date)
    df["date"] = [
            r.html.xpath(
                '/html/body/div/div/div/div[1]/main/div[2]/div[2]/div[1]/div/div[1]'
                )[0].text
        for index in df.index
    ]
    return df

def period_list(
    period: int,
    start_day: str
) -> typing.List[str]:
    
    today = datetime.date.today()
    result = today - start_day
    w = int(result.days)//7
    date_list = [
        dict(
            period =
                str(
                    period + (week*604800)
                ),
            data_source=data_source,
        )
        for week in range(1, w)
        for data_source in [
            "vtsc",
        ]
    ]
    return date_list

def main():
    
    
        
    df = crawler_twse(period=1711324800)
    if len(df) > 0:
        # 資料清理
        df = clean_data(df.copy())
        # 檢查資料型態
        df = check_schema(df.copy())
        print(df)
            
        # upload db
        try:
            df.to_sql(
                name="VtuberSuperChat",
                con=get_mysql_financialdata_conn(),
                if_exists="append",
                index=False,
                chunksize=1000,
            )
        except Exception as e:
            logger.info(e)
            

if __name__ == "__main__":
    main()