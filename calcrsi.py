import numpy
import talib
from numpy import genfromtxt

my_data = genfromtxt('price-ledger-daily.txt', delimiter='\n')
rsi = talib.RSI(my_data,timeperiod=14)
for k in rsi:
    print(k)





