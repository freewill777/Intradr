![](https://raw.githubusercontent.com/IntraTradr/tradr/beta-version/logo.png?token=AQYSQ6U2OVKIXLPZZKI3XVC7JWZK4)

wss://stream.binance.com:9443
wss://stream.binance.com:9443/ws/btcusdt@trade

## wscat -c wss://stream.binance.com:9443/ws/btcusdt@trade 
{
    "e": "trade",
    "E": 1598353655165,
    "s": "BTCUSDT",
    "t": 394374079,
    "p": "11649.25000000",
    "q": "0.00100000",
    "b": 3026544207,
    "a": 3026544140,
    "T": 1598353655164,
    "m": false,
    "M": true
}

## wscat -c wss://stream.binance.com:9443/ws/btcusdt@kline_5m
{
    "e": "kline",
    "E": 1598362403789,
    "s": "BTCUSDT",
    "k": {
        "t": 1598362200000,
        "T": 1598362499999,
        "s": "BTCUSDT",
        "i": "5m",
        "f": 394496169,
        "L": 394498931,
        "o": "11508.20000000",
        "c": "11490.54000000",
        "h": "11508.22000000",
        "l": "11475.67000000",
        "v": "217.30502600",
        "n": 2763,
        "x": false,
        "q": "2497343.11698196",
        "V": "77.57221400",
        "Q": "891312.63572457",
        "B": "0"
    }
}

{
    "e": "kline",
    "E": 1598362403789,
    "s": "BTCUSDT",
    "k": {
        "t": 1598362200000,
        "T": 1598362499999,
        "s": "BTCUSDT",
        "i": "5m",
        "f": 394496169,
        "L": 394498931,
        "o": "11508.20000000",
        "c": "11490.54000000",
        "h": "11508.22000000",
        "l": "11475.67000000",
        "v": "217.30502600",
        "n": 2763,
        "x": false,
        "q": "2497343.11698196",
        "V": "77.57221400",
        "Q": "891312.63572457",
        "B": "0"
    }
} 
