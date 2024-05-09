import pandas as pd

from vtuberdata.crawler.Vtuber_SuperChat import (
    clean_data,
    col_name,
    crawler_vtsc,
    period_list,
    crawler,
)
from vtuberdata.schema.dataset import (
    check_schema,
)

def test_clean_data():
    df = pd.DataFrame(
        [
            {
                "itemId": "UC-hM6YJuNYVAmUWxeIr9FeA",
                "period": "1709510400",
                "channelPlayCount": 451185838,
                "subscriberCount": 1970000,
                "subscriberFluc": float('NaN'),
                "maxLiveViewer": 149253,
                "donationAmount": 31725.57,
                "donationCount": 2079,
                "index": {
                    "rank": 1,
                    "rankFluc": 7
                },
                "channel": {
                    "channelId": "UC-hM6YJuNYVAmUWxeIr9FeA",
                    "name": "Miko Ch. さくらみこ",
                    "subscriberCount": 2020000,
                    "donationAmount": 1847128.9183273416,
                    "profileImagePath": "https://i.playboard.app/p/gxXHmXJq_kkZ0bvTmz7R1deyOAV44zZr2keaF0ojSq7MeiOGLSzFTCoYgYR4PGDWTCoLR7eK",
                    "keywords": [
                        "ホロライブ",
                        "hololive",
                        "Vtuber",
                        "歌ってみた",
                        "さくらみこ",
                        "兎田ぺこら",
                        "宝鐘マリン",
                        "白上フブキ",
                        "湊あくあ",
                        "星街すいせい",
                        "戌神ころね",
                        "大神ミオ",
                        "博衣こより",
                        "大空スバル",
                        "風真いろは",
                        "猫又おかゆ",
                        "ショート動画",
                        "ショート",
                        "TikTok",
                        "ブイチューバー",
                        "踊ってみた",
                        "Short",
                        "ダンス",
                        "切り抜き",
                        "3d",
                        "live",
                        "ストリーマー",
                        "cover",
                        "桃鈴ねね",
                        "雪花ラミィ",
                        "Kobo",
                        "Kanaeru",
                        "Gawr",
                        "Gura",
                        "Fuwamoco",
                        "リグロス",
                        "火威青",
                        "ゲーム実況",
                        "ゲーム",
                        "生放送",
                        "配信",
                        "バーチャル",
                        "ホロライブ 切り抜き",
                        "さくらみこ 切り抜き"
                    ]
                },
                "date": "03/04/2024 - 03/10",
            },
            {
                "itemId": "UC8rcEBzJSleTkf_-agPM20g",
                "period": "1709510400",
                "channelPlayCount": 79977036,
                "subscriberCount": 1000000,
                "subscriberFluc": 9000,
                "maxLiveViewer": 63119,
                "donationAmount": 25648.18,
                "donationCount": 1130,
                "index": {
                    "rank": 2,
                },
                "channel": {
                    "channelId": "UC8rcEBzJSleTkf_-agPM20g",
                    "name": "IRyS Ch. hololive-EN",
                    "subscriberCount": 1010000,
                    "donationAmount": 738830.5289121951,
                    "profileImagePath": "https://i.playboard.app/p/cDSMiVy3Xa49Ci_YyouVNzfCwVXKRYmOeywWQ_UFKzvAp6tvyeMtXMyzWzQ2u8ft4EENsJKt7A",
                    "keywords": [
                        "ホロライブ",
                        "Vtuber",
                        "hololive",
                        "ホロライブゲーマーズ",
                        "歌ってみた",
                        "ゲーム実況",
                        "実況",
                        "バーチャルyoutuber",
                        "VR",
                        "3D",
                        "ときのそら",
                        "ロボ子さん",
                        "夜空メル",
                        "アキ・ローゼンタール",
                        "赤井はあと",
                        "白上フブキ",
                        "夏色まつり",
                        "湊あくあ",
                        "紫咲シオン",
                        "百鬼あやめ",
                        "癒月ちょこ",
                        "大空スバル",
                        "大神ミオ",
                        "さくらみこ",
                        "猫又おかゆ",
                        "戌神ころね",
                        "兎田ぺこら",
                        "潤羽るしあ",
                        "不知火フレア",
                        "宝鐘マリン",
                        "白銀ノエル",
                        "AZKi",
                        "星街すいせい",
                        "hololive production",
                        "COVER Corp",
                        "hololive English",
                        "hololive EN",
                        "holoEN",
                        "Mori",
                        "Calliope",
                        "Takanashi",
                        "Kiara",
                        "Ninomae",
                        "Ina'nis",
                        "Gawr",
                        "Gura",
                        "Watson",
                        "Amelia",
                        "がうる・ぐら",
                        "わとそん・あめりあ",
                        "ホロライブEN",
                        "ホロライブプロダクション",
                        "holoMyth",
                        "森美声",
                        "小鳥遊キアラ",
                        "一伊那尓栖",
                        "ワトソン・アメリア",
                        "irys",
                        "vsinger",
                        "hope",
                        "アイリス"
                    ]
                },
                "date": "03/04/2024 - 03/10",
            },
            {
                "itemId": "UC-6rZgmxZSIbq786j3RD5ow",
                "period": "1709510400",
                "channelPlayCount": 81901244,
                "subscriberCount": float('NaN'),
                "subscriberFluc": -1000,
                "maxLiveViewer": 5781,
                "donationAmount": 25119.3,
                "donationCount": 892,
                "index": {
                    "rank": 3,
                    "rankFluc": -1
                },
                "channel": {
                    "channelId": "UC-6rZgmxZSIbq786j3RD5ow",
                    "name": "レオス・ヴィンセント / Leos.Vincent【にじさんじ】",
                    "subscriberCount": 414000,
                    "donationAmount": 919275.8246569335,
                    "profileImagePath": "https://i.playboard.app/p/6ea8e601d7865cf26ab5ad9446e0b4a9",
                    "keywords": [
                        "にじさんじ",
                        "VTuber",
                        "anime",
                        "アニメ",
                        "雑談",
                        "game",
                        "ゲーム",
                        "レオス・ヴィンセント",
                        "イラスト",
                        "nijisanji",
                        "japan",
                        "切り抜き",
                        "実況",
                        "歌ってみた",
                        "れおす・ヴぃんせんと",
                        "leos",
                        "vincent",
                        "nijisannji",
                        "leosvincent",
                        "まめねこ",
                        "mameneko",
                        "モンハンワールド",
                        "モンスターハンター：ワールド",
                        "MHW",
                        "CAPCOM",
                        "マリオカート8DX"
                    ]
                },
                "date": "03/04/2024 - 03/10",
            },
        ]
    )
    result_df = clean_data(
        df.copy()
    )  # 輸入函數, 得到結果
    expected_df = pd.DataFrame(
        [
            {
                "itemId": "UC-hM6YJuNYVAmUWxeIr9FeA",
                "period": "1709510400",
                "channelPlayCount": 451185838,
                "subscriberCount": 1970000,
                "subscriberFluc": 0.0,
                "maxLiveViewer": 149253,
                "donationAmount": 31725.57,
                "donationCount": 2079,
                "rank": 1,
                "rankFluc": "7",
                "name": "Miko Ch. さくらみこ",
                "start_date": "03/04/2024",
                "end_date": "03/10/2024",
            },
            {
                "itemId": "UC8rcEBzJSleTkf_-agPM20g",
                "period": "1709510400",
                "channelPlayCount": 79977036,
                "subscriberCount": 1000000,
                "subscriberFluc": 9000,
                "maxLiveViewer": 63119,
                "donationAmount": 25648.18,
                "donationCount": 1130,
                "rank": 2,
                "rankFluc": "nope",
                "name": "IRyS Ch. hololive-EN",
                "start_date": "03/04/2024",
                "end_date": "03/10/2024",
            },
            {
                "itemId": "UC-6rZgmxZSIbq786j3RD5ow",
                "period": "1709510400",
                "channelPlayCount": 81901244,
                "subscriberCount": 0.0,
                "subscriberFluc": -1000,
                "maxLiveViewer": 5781,
                "donationAmount": 25119.3,
                "donationCount": 892,
                "rank": 3,
                "rankFluc": "-1",
                "name": "レオス・ヴィンセント / Leos.Vincent【にじさんじ】",
                "start_date": "03/04/2024",
                "end_date": "03/10/2024",
            },
        ]
    )
    # 預期結果, 做完資料清理
    # 將原先的會計數字, 如 1,536,598
    # 轉換為一般數字 1536598
    assert (
        pd.testing.assert_frame_equal(
            result_df, expected_df
        )
        is None
    )  # 檢查, 執行結果 == 預期結果


def test_col_name():
     #  準備好 input 的假資料
    result_df = pd.DataFrame(
        [
            {
                "itemId": "UC-hM6YJuNYVAmUWxeIr9FeA",
                "period": 1709510400,
                "pscore": 5018235.6,
                "pplay": 3921327,
                "plike": 327558,
                "pdislike": 0,
                "channelPlayCount": 451185838,
                "channelPlayFluc": 5035539,
                "subscriberCount": 1970000,
                "subscriberFluc": 10000,
                "maxLiveViewer": 149253,
                "donationAmount": 31725.57,
                "donationCount": 2079,
                "index": {
                    "rank": 1,
                    "rankFluc": 7
                },
                "channel": {
                    "channelId": "UC-hM6YJuNYVAmUWxeIr9FeA",
                    "name": "Miko Ch. さくらみこ",
                    "subscriberCount": 2020000,
                    "donationAmount": 1847128.9183273416,
                    "profileImagePath": "https://i.playboard.app/p/gxXHmXJq_kkZ0bvTmz7R1deyOAV44zZr2keaF0ojSq7MeiOGLSzFTCoYgYR4PGDWTCoLR7eK",
                    "keywords": [
                        "ホロライブ",
                        "hololive",
                        "Vtuber",
                        "歌ってみた",
                        "さくらみこ",
                        "兎田ぺこら",
                        "宝鐘マリン",
                        "白上フブキ",
                        "湊あくあ",
                        "星街すいせい",
                        "戌神ころね",
                        "大神ミオ",
                        "博衣こより",
                        "大空スバル",
                        "風真いろは",
                        "猫又おかゆ",
                        "ショート動画",
                        "ショート",
                        "TikTok",
                        "ブイチューバー",
                        "踊ってみた",
                        "Short",
                        "ダンス",
                        "切り抜き",
                        "3d",
                        "live",
                        "ストリーマー",
                        "cover",
                        "桃鈴ねね",
                        "雪花ラミィ",
                        "Kobo",
                        "Kanaeru",
                        "Gawr",
                        "Gura",
                        "Fuwamoco",
                        "リグロス",
                        "火威青",
                        "ゲーム実況",
                        "ゲーム",
                        "生放送",
                        "配信",
                        "バーチャル",
                        "ホロライブ 切り抜き",
                        "さくらみこ 切り抜き"
                    ]
                },
                "videos": [
                    {
                        "videoId": "MO0gz82jGIE",
                        "title": "【 誕生日カウントダウン】明日は生誕ライブ‼🎉誕生日みんなと迎えるにぇぇぇええ‼【ホロライブ/さくらみこ】",
                        "isAd": "false",
                        "playCount": 258420
                    },
                    {
                        "videoId": "5QbfFvgT8OY",
                        "title": "【3D LIVE】新衣装お披露目あり🎉きゅんきゅん生誕祭2024💖【#さくらみこ生誕祭】",
                        "isAd": "false",
                        "playCount": 975126
                    }
                ],
            },
            {
                "itemId": "UC8rcEBzJSleTkf_-agPM20g",
                "period": 1709510400,
                "pscore": 1569990,
                "pplay": 760093,
                "plike": 89939,
                "pdislike": 0,
                "channelPlayCount": 79977036,
                "channelPlayFluc": 711284,
                "subscriberCount": 1000000,
                "subscriberFluc": 9000,
                "maxLiveViewer": 63119,
                "donationAmount": 25648.18,
                "donationCount": 1130,
                "index": {
                    "rank": 2,
                    "rankFluc": 14
                },
                "channel": {
                    "channelId": "UC8rcEBzJSleTkf_-agPM20g",
                    "name": "IRyS Ch. hololive-EN",
                    "subscriberCount": 1010000,
                    "donationAmount": 738566.3558861102,
                    "profileImagePath": "https://i.playboard.app/p/cDSMiVy3Xa49Ci_YyouVNzfCwVXKRYmOeywWQ_UFKzvAp6tvyeMtXMyzWzQ2u8ft4EENsJKt7A",
                    "keywords": [
                        "ホロライブ",
                        "Vtuber",
                        "hololive",
                        "ホロライブゲーマーズ",
                        "歌ってみた",
                        "ゲーム実況",
                        "実況",
                        "バーチャルyoutuber",
                        "VR",
                        "3D",
                        "ときのそら",
                        "ロボ子さん",
                        "夜空メル",
                        "アキ・ローゼンタール",
                        "赤井はあと",
                        "白上フブキ",
                        "夏色まつり",
                        "湊あくあ",
                        "紫咲シオン",
                        "百鬼あやめ",
                        "癒月ちょこ",
                        "大空スバル",
                        "大神ミオ",
                        "さくらみこ",
                        "猫又おかゆ",
                        "戌神ころね",
                        "兎田ぺこら",
                        "潤羽るしあ",
                        "不知火フレア",
                        "宝鐘マリン",
                        "白銀ノエル",
                        "AZKi",
                        "星街すいせい",
                        "hololive production",
                        "COVER Corp",
                        "hololive English",
                        "hololive EN",
                        "holoEN",
                        "Mori",
                        "Calliope",
                        "Takanashi",
                        "Kiara",
                        "Ninomae",
                        "Ina'nis",
                        "Gawr",
                        "Gura",
                        "Watson",
                        "Amelia",
                        "がうる・ぐら",
                        "わとそん・あめりあ",
                        "ホロライブEN",
                        "ホロライブプロダクション",
                        "holoMyth",
                        "森美声",
                        "小鳥遊キアラ",
                        "一伊那尓栖",
                        "ワトソン・アメリア",
                        "irys",
                        "vsinger",
                        "hope",
                        "アイリス"
                    ]
                },
                "videos": [
                    {
                        "videoId": "u4hBuNLzjkA",
                        "title": "【KARAOKE / 耐久歌枠】 1 MILLION ENDURANCE VERTICAL KARAOKE & BIRTHDAY COUNTDOWN! #shorts",
                        "isAd": "false",
                        "playCount": 267413
                    },
                    {
                        "videoId": "cc5SQqswwMM",
                        "title": "【HOPE TO THE FUTURE 3D LIVE】 IRyS 2024 Birthday Live! #IRySBDay",
                        "isAd": "false",
                        "playCount": 365659
                    }
                ],
            },
        ]
    )
    colname = [
        "itemId",
        "period",
        "pscore",
        "pplay",
        "plike",
        "pdislike",
        "channelPlayCount",
        "channelPlayFluc",
        "subscriberCount",
        "subscriberFluc",
        "maxLiveViewer",
        "donationAmount",
        "donationCount",
        "index",
        "channel",
        "videos",
    ]
    result_df = col_name(
        result_df.copy(), colname
    )  # 輸入函數, 得到結果
    expected_df = pd.DataFrame(
        [
            {
                "itemId": "UC-hM6YJuNYVAmUWxeIr9FeA",
                "period": 1709510400,
                "channelPlayCount": 451185838,
                "subscriberCount": 1970000,
                "subscriberFluc": 10000,
                "maxLiveViewer": 149253,
                "donationAmount": 31725.57,
                "donationCount": 2079,
                "index": {
                    "rank": 1,
                    "rankFluc": 7
                },
                "channel": {
                    "channelId": "UC-hM6YJuNYVAmUWxeIr9FeA",
                    "name": "Miko Ch. さくらみこ",
                    "subscriberCount": 2020000,
                    "donationAmount": 1847128.9183273416,
                    "profileImagePath": "https://i.playboard.app/p/gxXHmXJq_kkZ0bvTmz7R1deyOAV44zZr2keaF0ojSq7MeiOGLSzFTCoYgYR4PGDWTCoLR7eK",
                    "keywords": [
                        "ホロライブ",
                        "hololive",
                        "Vtuber",
                        "歌ってみた",
                        "さくらみこ",
                        "兎田ぺこら",
                        "宝鐘マリン",
                        "白上フブキ",
                        "湊あくあ",
                        "星街すいせい",
                        "戌神ころね",
                        "大神ミオ",
                        "博衣こより",
                        "大空スバル",
                        "風真いろは",
                        "猫又おかゆ",
                        "ショート動画",
                        "ショート",
                        "TikTok",
                        "ブイチューバー",
                        "踊ってみた",
                        "Short",
                        "ダンス",
                        "切り抜き",
                        "3d",
                        "live",
                        "ストリーマー",
                        "cover",
                        "桃鈴ねね",
                        "雪花ラミィ",
                        "Kobo",
                        "Kanaeru",
                        "Gawr",
                        "Gura",
                        "Fuwamoco",
                        "リグロス",
                        "火威青",
                        "ゲーム実況",
                        "ゲーム",
                        "生放送",
                        "配信",
                        "バーチャル",
                        "ホロライブ 切り抜き",
                        "さくらみこ 切り抜き"
                    ]
                },
            },
            {
                "itemId": "UC8rcEBzJSleTkf_-agPM20g",
                "period": 1709510400,
                "channelPlayCount": 79977036,
                "subscriberCount": 1000000,
                "subscriberFluc": 9000,
                "maxLiveViewer": 63119,
                "donationAmount": 25648.18,
                "donationCount": 1130,
                "index": {
                    "rank": 2,
                    "rankFluc": 14
                },
                "channel": {
                    "channelId": "UC8rcEBzJSleTkf_-agPM20g",
                    "name": "IRyS Ch. hololive-EN",
                    "subscriberCount": 1010000,
                    "donationAmount": 738566.3558861102,
                    "profileImagePath": "https://i.playboard.app/p/cDSMiVy3Xa49Ci_YyouVNzfCwVXKRYmOeywWQ_UFKzvAp6tvyeMtXMyzWzQ2u8ft4EENsJKt7A",
                    "keywords": [
                        "ホロライブ",
                        "Vtuber",
                        "hololive",
                        "ホロライブゲーマーズ",
                        "歌ってみた",
                        "ゲーム実況",
                        "実況",
                        "バーチャルyoutuber",
                        "VR",
                        "3D",
                        "ときのそら",
                        "ロボ子さん",
                        "夜空メル",
                        "アキ・ローゼンタール",
                        "赤井はあと",
                        "白上フブキ",
                        "夏色まつり",
                        "湊あくあ",
                        "紫咲シオン",
                        "百鬼あやめ",
                        "癒月ちょこ",
                        "大空スバル",
                        "大神ミオ",
                        "さくらみこ",
                        "猫又おかゆ",
                        "戌神ころね",
                        "兎田ぺこら",
                        "潤羽るしあ",
                        "不知火フレア",
                        "宝鐘マリン",
                        "白銀ノエル",
                        "AZKi",
                        "星街すいせい",
                        "hololive production",
                        "COVER Corp",
                        "hololive English",
                        "hololive EN",
                        "holoEN",
                        "Mori",
                        "Calliope",
                        "Takanashi",
                        "Kiara",
                        "Ninomae",
                        "Ina'nis",
                        "Gawr",
                        "Gura",
                        "Watson",
                        "Amelia",
                        "がうる・ぐら",
                        "わとそん・あめりあ",
                        "ホロライブEN",
                        "ホロライブプロダクション",
                        "holoMyth",
                        "森美声",
                        "小鳥遊キアラ",
                        "一伊那尓栖",
                        "ワトソン・アメリア",
                        "irys",
                        "vsinger",
                        "hope",
                        "アイリス"
                    ]
                },
            },
        ]
    )
    # 預期結果, 將 raw data , 包含中文欄位,
    # 轉換成英文欄位, 以便存進資料庫
    assert (
        pd.testing.assert_frame_equal(
            result_df, expected_df
        )
        is None
    )  # 檢查, 執行結果 == 預期結果
    

def test_crawler_vtsc_no_data():
    """
    測試沒 data 的時間點, 爬蟲是否正常
    """
    result_df = crawler_vtsc(
        period="1610323200"
    )
    assert (
        len(result_df) == 0
    )  # 沒 data, 回傳 0
    # 沒 data, 一樣要回傳 pd.DataFrame 型態
    assert isinstance(
        result_df, pd.DataFrame
    )


def test_crawler_vtsc_error(mocker):
    """
    測試對方網站回傳例外狀況時, 或是被 ban IP 時, 爬蟲是否會失敗

    這邊使用特別的技巧, mocker,
    因為在測試階段, 無法保證對方一定會給錯誤的結果
    因此使用 mocker, 對 requests 做"替換", 換成我們設定的結果
    如下
    """
    # 將特定路徑下的 requests 替換掉
    mock_requests = mocker.patch(
        "vtuberdata.crawler.Vtuber_SuperChat.HTMLSession"
    )
    # 將 requests.get 的回傳值 response, 替換掉成 ""
    # 如此一來, 當我們在測試爬蟲時,
    # 發送 requests 得到的 response, 就會是 ""
    mock_requests.get.return_value = ""
    result_df = crawler_vtsc(
        period="1610323200"
    )
    assert (
        len(result_df) == 0
    )  # 沒 data, 回傳 0
    # 沒 data, 一樣要回傳 pd.DataFrame 型態
    assert isinstance(
        result_df, pd.DataFrame
    )


def test_crawler_vtsc_success():
    """
    測試櫃買中心, 爬蟲成功時的狀況
    """
    result_df = crawler_vtsc(
        period="1709510400"
    )  # 執行結果
    assert (
        len(result_df) == 20
    )  # 檢查, 資料量是否正確
    assert list(result_df.columns) == [
        "itemId",
        "period",
        "channelPlayCount",
        "subscriberCount",
        "subscriberFluc",
        "maxLiveViewer",
        "donationAmount",
        "donationCount",
        "rank",
        "rankFluc",
        "name",
        "start_date",
        "end_date",
    ]

def test_period_list():
    """
    測試建立 task 參數列表, 2021-01-01 ~ 2021-01-05
    """
    result = period_list(
        period = "1708905600",
        start_day = "2/26/2024"
    )  # 執行結果
    expected = [
        {
            "period": "1709510400",
            "data_source": "vtsc",
        },
        {
            "period": "1710115200",
            "data_source": "vtsc",
        },
        {
            "period": "1710720000",
            "data_source": "vtsc",
        },
        {
            "period": "1711324800",
            "data_source": "vtsc",
        },
        {
            "period": "1711929600",
            "data_source": "vtsc",
        },
        {
            "period": "1712534400",
            "data_source": "vtsc",
        },
        {
            "period": "1713139200",
            "data_source": "vtsc",
        },
        {
            "period": "1713744000",
            "data_source": "vtsc",
        },
        {
            "period": "1714348800",
            "data_source": "vtsc",
        },
    ]
    # 預期得到 2021-01-01 ~ 2021-01-05 的任務參數列表
    # 再發送這些參數到 rabbitmq, 給每個 worker 單獨執行爬蟲
    assert (
        result == expected
    )  # 檢查, 執行結果 == 預期結果

def test_crawler_vtsc():
    # 測試證交所爬蟲, end to end test
    result_df = crawler(
        parameter={
            "period": "1709510400",
            "data_source": "vtsc",
        }
    )
    result_df = check_schema(
        result_df, "VtuberSuperChat"
    )
    assert len(result_df) > 0