import currentprice

def main():
  print("starting trading system...")
  
main()
#currentprice.spinner()
#close price rsi 
print('updating the price ledger ...')
currentprice.add_today_price_to_ledger()
print('calculating rsi for today ...')
currentprice.add_rsi_to_ledger()
currentprice.check_rsi_buy_sell('BTCUSDT')


