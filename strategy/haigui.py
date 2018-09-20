# Author: Tao Hu <taohu620@gmail.com>

from __future__ import absolute_import, unicode_literals
from datetime import datetime,date,time,timedelta
from apscheduler.schedulers.tornado import TornadoScheduler
from apscheduler.triggers.interval import IntervalTrigger
import tornado.ioloop
import talib
import numpy as np

from exchange.huobi import HuobiServices

from mylogger.mylogger import logger
import logging


#start_date = '2018-09-15'
#end_date = '2019-09-15'

#######global variable############
def init(context):
    pass
#######global variable############

def haigui():
    #https://www.ricequant.com/api/python/chn#python-sample-strategy-turtle
    from exchange.base.Exchange import BaseContext
    context = BaseContext()
    #init(context)

    from exchange.base.huobi import Huobi
    huobi = Huobi()

    context.mysymbol = 'rdneth'
    context.mysymbol_from = "eth"
    context.mysymbol_to = "rdn"
    context.larger_than_past_x_then_buy = 3
    context.smaller_than_past_x_then_sell = 10
    context.trade_signal = "start"
    context.pre_trade_signal = ""
    context.units_hold_max = 4
    context.units_hold = 0
    context.unit_size = 0
    context.quantity = 0
    context.max_add = 0
    context.first_open_price = 0

    context.last_price = huobi.get_trade(symbol=context.mysymbol)['price']







    # calculate max, min, unit size
    from exchange.base.huobi import Huobi
    huobi = Huobi()
    k_line_max = huobi.get_record(symbol=context.mysymbol, period=Huobi.Period.PERIOD_D1, size=context.larger_than_past_x_then_buy)
    k_line_min = huobi.get_record(symbol=context.mysymbol, period=Huobi.Period.PERIOD_D1, size=context.smaller_than_past_x_then_sell)

    buy_thres = max([k_line_max['record'][i]['high'] for i in range(context.larger_than_past_x_then_buy)])
    sell_thres = min([k_line_min['record'][i]['low'] for i in range(context.smaller_than_past_x_then_sell)])

    atr_input = huobi.get_record(symbol=context.mysymbol, period=Huobi.Period.PERIOD_D1, size=context.larger_than_past_x_then_buy)
    max_list = np.array([atr_input['record'][i]['high'] for i in range(context.larger_than_past_x_then_buy)])
    min_list = np.array([atr_input['record'][i]['low'] for i in range(context.larger_than_past_x_then_buy)])
    close_list = np.array([atr_input['record'][i]['close'] for i in range(context.larger_than_past_x_then_buy)])
    atr_output = talib.ATR(high=max_list, low=min_list, close=close_list, timeperiod=context.larger_than_past_x_then_buy)
    atr_thres = atr_output[-1]

    def get_stop_price(first_open_price, units_hold, atr):
        return first_open_price - 2 * atr + (units_hold - 1) * 0.5 * atr

    def get_unit_size(atr, total_value):
        return 0.1 * total_value / atr


    if context.trade_signal == "start":
        context.max_add = context.last_price
    else:
        context.max_add += 0.5*atr_thres


    current_position = huobi.get_balance(currency=context.mysymbol_to)
    avaibable_cash = huobi.get_balance(currency=context.mysymbol_from)

    if current_position > 0 and \
            context.last_price < get_stop_price(context.first_open_price, context.units_hold, atr_thres):
        context.trade_signal = "stop"

    elif context.last_price > context.max_add and \
            context.units_hold != 0 and \
            context.units_hold < context.units_hold_max and \
            avaibable_cash > context.last_price * context.unit_size:
        context.trade_signal = "entry_add"

    elif context.last_price > buy_thres and \
    context.units_hold == 0 and \
    context.max_add == context.last_price:
        context.trade_signal = "entry"

    else:
        pass

    #TODO update context.unit_size every week~

    if context.trade_signal != context.pre_trade_signal or \
            (context.units_hold < context.units_hold_max and context.units_hold > 1) or \
        context.trade_signal == "stop":
        if context.trade_signal == "entry":







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
