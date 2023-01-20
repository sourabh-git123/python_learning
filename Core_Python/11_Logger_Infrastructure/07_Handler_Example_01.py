
import logging
import logging.config

# logging.config.dictConfig('logging2.conf')
# logger = logging.getLogger('simpleExample')
# logger.debug('This is a debug message from main')

"""
    In this handler Example we can :
        a. Setted max file limit and after that we can also set for the max number of 
            files to catch the log
        
"""

def logging_exception():
    try:
        a = [1, 2, 3]
        val = a[4]

    except:
        import traceback
        print("inside exception : ")
        logging.basicConfig(filename='logs/abc.log', format='%(asctime)s - %(message)s')
        logging.error(f'This error is from %s ' %(traceback.format_exc()))

def handler_example():

    from logging.handlers import RotatingFileHandler

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    """
        Here we will set :
            a. maxBytes     = 2000
            b. backupCount  = 5
    """
    handler = RotatingFileHandler('logs/new_app.log', maxBytes=20000, backupCount=10)

    # handler = TimedRotatingFileHandler('logs/timed_tesr__.log', when='s', interval=2, backupCount=10)


    logger.addHandler(handler)

    for _ in range(100000):
        logger.info('>>> Hello, world! Welcome to The ')

print("Calling handler_example()...")
handler_example()





