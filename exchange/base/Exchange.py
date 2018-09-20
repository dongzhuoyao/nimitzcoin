# Author: Tao Hu <taohu620@gmail.com>

from enum import Enum




class Exchange():
    def __init__(self):
        pass

    def sell(self):
        raise NotImplementedError()

    def buy(self):
        raise NotImplementedError()

    def getTicker(self,symbol):
        raise NotImplementedError()

    def getRecords(self,period):
        raise NotImplementedError()


