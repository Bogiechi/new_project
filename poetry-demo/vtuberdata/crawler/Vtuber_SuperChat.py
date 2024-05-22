import datetime
import time
import typing

import pandas as pd
from requests_html import HTMLSession
from loguru import logger
from tqdm import tqdm
from vtuberdata.schema.dataset import (
    check_schema,
)

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
    df = df.drop(["date"], axis=1)
    df = df.fillna(0.0)
    df['period'] = [
        str(df["period"][col])
        for col in df.index
    ]

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
        "channelPlayFluc": "channelPlayFluc",
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

def crawler_vtmv(
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
    df = clean_data(df.copy())
    return df

def crawler_vtsc(
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
    df = clean_data(df.copy())
    return df

def period_list(
    period: str,
    start_day: str
) -> typing.List[str]:
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
    return date_list

def crawler(
    parameter: typing.Dict[
        str,
        typing.List[
            typing.Union[
                str, int, float
            ]
        ],
    ]
) -> pd.DataFrame:
    logger.info(parameter)
    period = parameter.get("period", "")
    data_source = parameter.get(
        "data_source", ""
    )
    if data_source == "vtsc":
        df = crawler_vtsc(period)
        df = check_schema(
            df.copy(),
            dataset="VtuberSuperChat",
        )
    if data_source == "vtmv":
        df = crawler_vtsc(period)
        df = check_schema(
            df.copy(),
            dataset="VtuberSuperChat",
        )
    return df