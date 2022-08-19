"""
Logger
"""

import os
import logging
import logging.config

from configs import config

LOGLEVEL = config.get('default', 'log_level')
LOGNAME = config.get('default', 'log_name')
LOGDIR = os.path.dirname(os.path.abspath(__file__))
LOGFILE = os.path.join(LOGDIR, f'{LOGLEVEL}.log')
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(lineno)d %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'console': {
            'format': '%(asctime)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers':{
        'fileHandler':{
            'class':'logging.handlers.RotatingFileHandler',
            'filename': LOGFILE,
            'formatter': 'standard',
            'mode': 'a',
            'maxBytes': 1024*1024*10,
            'backupCount': 10,
            'encoding': 'utf-8'
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        }
    },
    'loggers': {
        LOGNAME: {
            'level': LOGLEVEL.upper(),
            'handlers': ['fileHandler', 'console'],
            'propagate': False
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(LOGNAME)
