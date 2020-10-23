<<<<<<< HEAD
import config, csv
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET)
account = client.get_account()

def instant_price(ssymbol):
    order_book = client.get_orderbook_ticker(symbol=ssymbol)
    print((order_book)['askPrice'])
    return (order_book)['askPrice']

ssymbol = 'BTCUSDT'

free_balance_btc = client.get_asset_balance(asset='BTC')['free']
free_balance_usdt = client.get_asset_balance(asset='USDT')['free']

#current_price_btc = 

ask_price = client.get_orderbook_ticker(symbol=ssymbol)['askPrice']
ask_qty = client.get_orderbook_ticker(symbol=ssymbol)['askQty']


print(ask_price)
print(ask_qty)

print(free_balance_btc)

if float(free_balance_usdt) < float(ask_price) * float(ask_qty):
    print("plm1")
    order = client.order_limit_buy(
        symbol=ssymbol,
        quantity= float(free_balance_usdt) / float(ask_price),
        price= ask_price

elif float(free_balance_usdt) > float(ask_price) * float(ask_qty):
    print("plm2")
    order = client.order_limit_buy(
        symbol=ssymbol,
        quantity= float(free_balance_usdt) / float(ask_price),
        price= ask_price
    remaining = float(free_balance_usdt) - quantity * price


#order = client.order_market_buy(
    #symbol='BTCUSDT',
    #quantity=100)

#order = client.order_market_sell(
    #symbol='BTCUSDT',
    #quantity=100)


