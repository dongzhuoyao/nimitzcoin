# Author: Tao Hu <taohu620@gmail.com>

from exchange.huobi.HuobiServices import get_ticker,send_order,get_kline, get_balance,get_trade
from exchange.base import Exchange

class Huobi(Exchange.Exchange):
    class Period():
        #1min, 5min, 15min, 30min, 60min, 1day, 1mon, 1week, 1year
        PERIOD_M1 = "1min"
        PERIOD_M5 = "5min"
        PERIOD_M15 = "15min"
        PERIOD_M30 = "30min"
        PERIOD_H1 = "60min"
        PERIOD_D1 = "1day"
        PERIOD_W1 = "1week"
        PERIOD_MON1 = "1mon"
        PERIOD_Y1 = "1year"


    def __init__(self):
        pass

    def sell(self, symbol, amount):
        result = send_order(amount, symbol, _type="sell-market",source=None)
        ret={}
        ret["info"] = result
        return ret

    def buy(self, symbol, amount):
        result = send_order(amount=amount, symbol=symbol, _type="buy-market", source=None)
        ret={}
        ret["info"] = result
        return ret

    def get_trade(self,symbol):
        result = get_trade(symbol=symbol)
        ret = {}
        ret["info"] = result
        ret['data'] = result['tick']['data'][0]
        return ret

    def get_ticker(self, symbol):
        result = get_ticker(symbol)
        ret = {}
        ret["info"] = result
        ret["high"] = result['tick']['high']
        ret["low"] = result['tick']['low']
        ret["sell"] = result['tick']['ask'][0]
        ret["buy"] = result['tick']['bid'][0]
        ret["open"] = result['tick']['open']
        ret["close"] = result['tick']['close']
        ret["count"] = result['tick']['count']
        ret["vol"] = result['tick']['vol']
        return ret


    def get_record(self,symbol, period, size):
        result = get_kline(symbol, period, size)
        ret = {}
        ret["info"] = result
        ret["record"] = result["data"]
        return ret

    def get_balance(self,currency):
        result = get_balance()
        ret = {}
        ret["info"] = result
        for c in result['data']['list']:
            if c['currency'] == currency and c['type'] == 'trade':
                ret['balance'] =  c['balance']
                return ret

        raise ValueError("unknown currency: {}".format(currency))




if __name__ == '__main__':
    hb = Huobi()
    result = hb.get_trade(symbol="kcashht")
    #result = hb.getRecord(symbol="rdneth",period=Huobi.Period.PERIOD_D1,size=100)
    #result = hb.getBalance(currency="ht")
    #result = hb.buy(symbol="kcashht", amount=1)
    #result = hb.getBalance(currency="kcash")
    pass
