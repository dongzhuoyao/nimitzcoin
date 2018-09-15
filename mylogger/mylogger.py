# Author: Tao Hu <taohu620@gmail.com>

import logging
from logging.config import dictConfig

logging_config = dict(
    version = 1,
    formatters = {
        'f': {'format':
              '%(asctime)s %(name)-4s %(levelname)-4s %(message)s'}
        },
    handlers = {
        'h': {'class': 'logging.StreamHandler',
              'formatter': 'f',
              'level': logging.INFO},
        'f_h':{'class': 'logging.FileHandler',
               'filename': 'nimitzcoin.log',
              'formatter': 'f',
              'level': logging.INFO},

        },
    root = {
        'handlers': ['h','f_h'],
        'level': logging.INFO,
        },
)

dictConfig(logging_config)

logger = logging.getLogger()
