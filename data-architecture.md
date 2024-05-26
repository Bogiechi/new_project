# 數據架構

## 數據源

- **來源**: https://playboard.co/en/youtube-ranking/most-superchatted-v-tuber-channels-in-japan-weekly
- **爬取工具**: Python, RabbitMQ, Celery

## 數據庫結構

### VtuberSuperChat表

| Field       		| Type         | Null | Key | Default | Extra          |
|-------------------|--------------|------|-----|---------|----------------|
| itemId      		| varchar(50)  | NO   |     | NULL    |                |
| period      		| varchar(50)  | NO   |     | NULL    |                |
| channelPlayCount  | float        | NO   |     | NULL    |                |
| channelPlayFluc   | float        | NO   |     | NULL    |                |
| subscriberCount   | float        | NO   |     | NULL    |                |
| subscriberFluc    | float        | NO   |     | NULL    |                |
| maxLiveViewer     | float        | NO   |     | NULL    |                |
| donationAmount    | float        | NO   |     | NULL    |                |
| donationCount		| int          | NO   |     | NULL    |                |
| rank        		| int          | NO   |     | NULL    |                |
| rankFluc   		| varchar(10)  | NO   |     | NULL    |                |
| start_date 		| varchar(50)  | NO   |     | NULL    |                |
| end_date   		| varchar(50)  | NO   |     | NULL    |                |
| name        		| varchar(50)  | NO   |     | NULL    |                |