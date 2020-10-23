import config
from binance.client import Client
client = Client(config.API_KEY, config.API_SECRET)
account = client.get_account()

klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "12 Aug, 2020", "27 Aug, 2020")
for k in klines:
    print(k)