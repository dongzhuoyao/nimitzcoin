# Author: Tao Hu <taohu620@gmail.com>

from __future__ import absolute_import, unicode_literals
from datetime import datetime,date,time,timedelta
from apscheduler.schedulers.tornado import TornadoScheduler
from apscheduler.triggers.interval import IntervalTrigger
import tornado.ioloop

from exchange.huobi import HuobiServices

from mylogger.mylogger import logger
import logging

mysymbol = 'rdneth'
#start_date = '2018-09-15'
#end_date = '2019-09-15'

#######global variable############
larger_than_past_x_then_buy = 20
smaller_than_past_x_then_sell  = 10
trade_signal = "start"
pre_trade_signal = ""
units_hold_max = 4
units_hold = 0
quantity = 0
max_add = 0
first_open_price = 0
#######global variable############

def haigui():
    from exchange.base.huobi import Huobi



    #result = HuobiServices.get_kline(symbol=mysymbol, period='1day', size=150)
    #buy_thres = max([result['data'][i]['high'] for i in range(larger_than_past_x_then_buy)])
    #sell_thres = min([result['data'][i]['low'] for i in range(smaller_than_past_x_then_sell)])
    #result = HuobiServices.get_trade(symbol=mysymbol)
    #current_price = result['tick']['data'][0]['price']

    #calculate max, min, unit size




    print(result)

if __name__ == '__main__':
    haigui()
    sched = TornadoScheduler()
    sched.add_job(
        func=haigui,
        trigger=IntervalTrigger(
            start_date=datetime.combine(date.today(), time.max),#today 23:59
            end_date=date.today() + timedelta(days=1e3), #datetime.now() + timedelta(days=1),
            #days=1,
            seconds=5,
        ),
        name='haigui')

    sched.start()
    try:
        tornado.ioloop.IOLoop.current().start()
    except (KeyboardInterrupt, SystemExit) as e:
        logging.exception("exception occurs: ")
        sched.shutdown()
