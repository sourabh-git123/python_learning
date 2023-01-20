
"""
    Logging using .conf configuration file
    Working fine

    Able to read log configuration file : logging.conf

"""
import logging
import logging.config
from datetime import datetime
import yaml

class LoggerDemoConf():

    """
    This will only write to the file not in the console
    Reading with .conf file
    """
    def testLog(self):
        try:
            # super().__init__()
            # Creating logger
            logging.config.fileConfig('configuration_files\logging.conf')
            # logger = logging.getLogger(LoggerDemoConf.__name__)
            logger = logging.getLogger()

            # Logging message
            logger.debug('debug message')
            logger.info('Info message')
            logger.warning('warning message')
            logger.error('error message')
            logger.critical('critical message')

        except Exception as e:
            import traceback
            print(f"Exception in testLog : '{traceback.format_exc()}'  ")

    def testLog_with_Console(self):
        pass

    """
        Working fine...
    """
    def get_current_time(self):
        from datetime import datetime

        # Fetching current time to append in the file name
        current_date_time = str(datetime.now())[:-7]

        # time_list = current_date_time.split(' ')

        def remove_char(string=None, split_char=' '):
            # This will remove with split character and append underscore in place of that

            word_list = string.split(split_char)
            new_str = ''
            for each in word_list:
                new_str = new_str + '_' + each
            return new_str

        # Changing file output name with concatenating time to get new everytime
        current_date_time = remove_char(current_date_time, ' ')
        current_date_time = remove_char(current_date_time, ':')
        print(f"current time : {current_date_time}")

        return current_date_time

    def testLog_yaml(self):
        import logging, platform
        from logging.config import dictConfig
        import os

        try:
            # hostname = platform.node()

            yml_log_path = 'configuration_files\logging_conf_file2.yml'
            if os.path.exists(yml_log_path):
                with open(yml_log_path, 'rt') as f:
                    config_json = yaml.safe_load(f.read())
                    print(f"config = \n={config_json}=  ")

                    # dd mm yyyy time getting
                    today_date = str(datetime.today().strftime('%d-%m-%Y'))

                    filename = config_json['handlers']['file']['filename'][:-4] + '_' + today_date + '.log'
                    print(f"filename = {filename} ")

                    # Updating to the config_json file
                    config_json['handlers']['file']['filename'] = filename

                dictConfig(config_json)
            else:
                print("Configuration YML File does not exist ! ")
                return False

            # Creating logger
            logger = logging.getLogger('sampleLogger')
            # logger.setLevel(logging.DEBUG)



            for i in range(10000):
                # Implementing
                logger.debug("Hello Debug message...")
                logger.info("Hello Info message...")
                logger.warning("Hello Warning message...")
                logger.error("Hello Error message...")
                logger.critical("Hello Critical message...")
                print()

        except Exception as e:
            import traceback
            print(f"testLog_yaml exception :  {traceback.print_exc()}  ")




print(f"From main...")
print("Using yml file for configuration : ")

Logger_Demo_obj = LoggerDemoConf()
Logger_Demo_obj.testLog_yaml()

