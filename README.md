CO2 Sender
==

[CO2モニター](https://www.amazon.co.jp/dp/B00I3XJ9LM)から取得した温度とCO2濃度のデータをZabbixに送信する。


インストール
--

### docker-compose

```sh
cp .env.sample .env

vim .env

docker-compose up -d
```

環境変数
--

- CO2SENDER_ZABBIX_SERVER
  - 送信先のZabbix Server

- CO2SENDER_HOST
  - 送信元ホスト名。Zabbixの設定と合わせる。


