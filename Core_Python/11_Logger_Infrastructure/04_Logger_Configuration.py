
import logging
import logging.config

class LoggerDemoConf():

    def testLog(self):
        try:

            # Creating logger and loading logging configuration
            logging.config.fileConfig('logs/logging.conf')
            logger = logging.getLogger(LoggerDemoConf.__name__)

            # Some logging message
            logger.info("Info message")
            logger.debug("Debug message")
            logger.warning("Warning message")
            logger.error("Error message")
            logger.critical("Critical message")

        except Exception as e:
            import traceback
            print(f"exception in testLog : {traceback.format_exception()} ")


def main():

    print("From main..")
    loggerDemoConf_obj = LoggerDemoConf()
    loggerDemoConf_obj.testLog()


if __name__ == '__main__':
    main()


