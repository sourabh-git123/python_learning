"""
    With this file it will print the log message in the console as well

"""
import logging

class LoggerDemoConsole():

    def testLog(self):

        # logging.basicConfig(format = '[%(asctime)s] %(levelname)s [%(filename)s: (line %(lineno)d) ] - %(message)s', datefmt= '%d/%m/%y %I:%M:%S %p', level= logging.DEBUG)

        # Creating logger
        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.INFO)

        # Creating console handler and setting the level
        con_handler = logging.StreamHandler()
        con_handler.setLevel(logging.INFO)

        # Now Creating the Formatter and calling formatter method
        log_formatter = logging.Formatter('[%(asctime)s] %(levelname)s [%(filename)s: (line %(lineno)d) ] - %(message)s')

        # Now adding formatter to console handler
        con_handler.setFormatter(log_formatter)

        # Adding console handler to the logger
        logger.addHandler(con_handler)

        # Now we will print this console message
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warning message')
        logger.error('error message')
        logger.critical('critical message')


def main():

    print("From main...")
    obj = LoggerDemoConsole()
    obj.testLog()

    print("Ending from main")

if __name__ == '__main__':
    main()

