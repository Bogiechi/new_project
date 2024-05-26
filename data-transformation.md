# 數據轉換過程

## 資料爬取

使用 Python 和分散式爬蟲工具（RabbitMQ 和 Celery）從 playboard.co 爬取 SuperChat 資料。

## 資料清洗

### 原始資料格式
```json
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
            }
```

### 清洗後資料格式

```json
{
                "itemId": "UC-hM6YJuNYVAmUWxeIr9FeA",
                "period": "1709510400",
                "channelPlayCount": 451185838,
                "channelPlayFluc": 5035539,
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
            }
```

## 清洗過程
- 篩掉無用資料
- 將空值轉換為0.0
- 自行增加date資料並轉換為str格式

## 數據存儲
- 使用 SQLAlchemy 清洗後的數據存儲到 MySQL 數據庫中。

## 數據展示
- 在 Redash 中創建數據儀表板，使用 SQL 查詢從 MySQL 數據庫中提取數據，並以圖表形式展示。
數據儀表板 : http://chidashboard.ddns.net/public/dashboards/yjlyFqmtEWUbu7hU9Q0tbNAErF0fiPglcTpMBMMV?org_slug=default

## 技術細節

### 分散式爬蟲：RabbitMQ 作為消息隊列，Celery 作為任務隊列，分發和執行爬蟲任務，實現高效的分散式數據爬取，同時避免頻繁爬蟲被ban ip。
### 數據庫：使用 MySQL 資料庫存儲和管理清洗後的數據，確保數據的一致性和可靠性。
### 數據可視化：Redash 創建的數據儀表板，提供豐富的可視化圖表和報告，幫助用戶理解和分析數據。
### 容器化部署：使用 Docker 容器化應用，通過 Docker Swarm 管理容器的調度和運行，實現應用的高可用性和可擴展性。
### CI/CD：配置 GitLab CI/CD pipeline，實現程式碼的自動化測試和部署，確保應用的穩定性和可靠性。