import numpy
import talib
import rsiconfig
from numpy import genfromtxt

my_data = genfromtxt('1-JAN-27-AUG-2020-1DAY.csv', delimiter=',')
close = [my_data[:,4]]
#numpy.append(close, 222)
close.append('ssss')
print(close)
print('--------')
print(close[-1])
print('--------')
print(close[-2][1])