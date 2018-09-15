# Author: Tao Hu <taohu620@gmail.com>

from __future__ import absolute_import, unicode_literals
from datetime import datetime,date,time,timedelta
from apscheduler.schedulers.tornado import TornadoScheduler
from apscheduler.triggers.interval import IntervalTrigger
import tornado.ioloop


from mylogger.mylogger import logger
import logging

def testfunc(a, b, c):
    logger.info('dongzhuoyao DOING: %s' % locals())

if __name__ == '__main__':
    sched = TornadoScheduler()
    sched.add_job(
        func=testfunc,
        args=(1, 2, 3),
        trigger=IntervalTrigger(
            start_date=datetime.combine(date.today(), time.max),#today 23:59
            end_date=date.today() + timedelta(days=1e3), #datetime.now() + timedelta(days=1),
            days=1,
        ),
        name='testfunc')

    sched.start()
    try:
        tornado.ioloop.IOLoop.current().start()
    except (KeyboardInterrupt, SystemExit) as e:
        logging.exception("exception occurs: ")
        sched.shutdown()
