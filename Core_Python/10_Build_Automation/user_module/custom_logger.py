
import os
import yaml
from logging.config import dictConfig
from datetime import datetime


class custom_logger():

    def __init__(self, conf_file = r'D:\Programming_Practice\Core_Python\10_Build_Automation\configuration_file\logging_conf.yml', logger_name = "simpleLogger"):
        self.log_conf_file = 'logging_conf.yml'
        self.name = logger_name


    """
        Logger configuration : 
            This file will read configuration file yml, all information related to configuration changes is 
            written to the file...
            Note : Need to call logger_config first to utilize logger
    """
    def logger_config(self):

        try:
            print("Logging Configuration is under processing...")

            """
                Code to Read YML Configuration file while making changes of date in it...
            """
            log_config_path = self.log_conf_file

            if not os.path.exists(log_config_path):
                raise FileNotFoundError(f"{log_config_path} File not found !"
                                        f"\nPlease provide valid file / path in yml configuration file ! ")

            else:
                with open(log_config_path, 'rt') as file:
                    reading_file = file.read()
                    print("Reading log configuration file...")
                    config_json = yaml.safe_load(reading_file)

                    # print(f"Currently read config json = {config_json} ")

                    # dd mm yyyy time getting
                    today_date = str(datetime.today().strftime('%d-%m-%Y'))

                    log_file_name = config_json['handlers']['file_handler']['filename'][:-4] + '_' + today_date + '.log'
                    print(f"output log_file_name = {log_file_name} ")

                    # Updating log file to the configuration json
                    config_json['handlers']['file_handler']['filename'] = log_file_name

                    # Passing log yml configuration file to the logging constructor via dictConfig
                    dictConfig(config_json)
                    print("Logging configuration Done...\n")

                # Code to check if logger is working
                    import logging
                    logger = logging.getLogger(__name__)
                    logger.setLevel(logging.DEBUG)

                    print(f" \n\ntype = {type(logger)}")

                    # print("Checking for many logs...")
                    for i in range(10):
                        logger.debug("Log debug message...")
                        logger.info("Log info message...")
                        logger.error("Log error message...")
                        logger.warning("Log warning message...")
                        logger.critical("Log critical message...")

                    return True

        except Exception as e:
            import traceback
            # print(f'Exception while logging configuration :  {traceback.format_exception()} ')
            return False


def main():

    print("From main...")

    obj = custom_logger()
    obj.logger_config()



if __name__ == "__main__":
    main()