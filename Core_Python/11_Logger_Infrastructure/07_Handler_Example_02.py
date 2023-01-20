
"""
    This will create the log and also make file name according to the time naming embedded in the filename

    Use Time like :
        s
        m
        h
        d
        midnight
        w
"""
import logging
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


handler = TimedRotatingFileHandler('logs/timed_tesr__.log', when='s', interval=2, backupCount=10)
logger.addHandler(handler)

for _ in range(10000):
    logger.info('Hello, world !')
    time.sleep(2)









