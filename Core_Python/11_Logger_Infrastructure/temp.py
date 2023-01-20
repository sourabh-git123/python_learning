
import logging
from logging import config


def logger_implementation1():

    logger = logging.getLogger(__name__)

    config.dictConfig()

    logger.setLevel(logging.WARNING)
    handler = logging.FileHandler('temp_log_file.log')
    formatter = logging.Formatter('%(asctime)s : %(name)s  : %(funcName)s : %(levelname)s : %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # console handler
    c_handler = logging.StreamHandler()
    c_handler.setFormatter(formatter)
    c_handler.setLevel(logging.WARNING)
    logger.addHandler(c_handler)

    logger.debug('A debug message')
    logger.info('An info message')
    logger.warning('There is something wrong')
    logger.error('An error has happened.')
    logger.critical('Fatal error occured. Cannot continue')



def logger_implementation2():
    # Using while importing my own logger module

    print("From logger_implementation2 >>>> ")
    from base_cons_file_logger import cust_logger
    log_obj = cust_logger(__file__)

    log_obj.console_file()



print("Calling from main while importing base logger")
logger_implementation2()