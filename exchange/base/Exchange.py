# Author: Tao Hu <taohu620@gmail.com>

from enum import Enum


class BaseContext(object):
    def __init__(self):
        pass

class Exchange():
    def __init__(self):
        pass

    def sell(self):
        raise NotImplementedError()

    def buy(self):
        raise NotImplementedError()

    def get_ticker(self,symbol):
        raise NotImplementedError()

    def get_trade(self,symbol):
        raise NotImplementedError()

    def get_records(self,period):
        raise NotImplementedError()

    def get_balance(self,currency):
        raise NotImplementedError()



