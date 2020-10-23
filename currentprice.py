import config
from binance.client import Client
import flask
from flask import flash
import numpy
import talib
from numpy import genfromtxt

client = Client(config.API_KEY, config.API_SECRET)
account = client.get_account()

def instant_price(ssymbol):
    order_book = client.get_orderbook_ticker(symbol=ssymbol)
    print((order_book)['askPrice'])
    return (order_book)['askPrice']

def add_today_price_to_ledger():
    klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 day ago UTC")
    with open('price-ledger-daily.txt','a') as fd:
        fd.write('\n')
        fd.write(klines[0][3])
        fd.close()
    print('price ledger updated...')

def add_rsi_to_ledger():
    data = genfromtxt('price-ledger-daily.txt', delimiter='\n')
    rsi = talib.RSI(data,timeperiod=14)
    with open('rsi-ledger-daily.txt','a') as fd:
        fd.write('\n')
        fd.write(str(rsi[-1]))
        fd.close()
    print('rsi ledger updated...')
    
def buy(ssymbol, qquantity):
    order = client.create_order(symbol=ssymbol, side=SIDE_BUY, type=ORDER_TYPE_MARKET, quantity=qquantity)

def check_rsi_buy_sell(ssymbol):
    data = genfromtxt('price-ledger-daily.txt', delimiter='\n')
    open_orders = client.get_open_orders(symbol=ssymbol)
    rsi = talib.RSI(data,timeperiod=14)
    if rsi[-1] < 30: 
        if ssymbol not in open_orders:
            print('buy')
        #buy(ssymbol, 1)
    elif rsi[-1] > 70:
        if ssymbol not in open_orders:
            print('sell')
    else:
        print('waiting for a better day...')
        #sell
            #open_orders.insert(0, symbol)
    return rsi[-1]

def spinner():
    while True:
        import itertools, sys
        spinner = itertools.cycle(['-','-','-', '/','/','/', '|','|','|', '\\', '\\', '\\'])
        while True:
            sys.stdout.write(next(spinner))   
            sys.stdout.flush()                
            sys.stdout.write('\b') 


