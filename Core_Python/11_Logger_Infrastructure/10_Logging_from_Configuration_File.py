
"""
    Using yaml configuration
        - Prob on using

"""
import logging
import logging.config
import yaml

with open('logging_conf_file.yml', 'r') as file_p:
    config = yaml.safe_load(file_p.read())
    logging.config.dictConfig(config)

# print(f"Reading from configuration file : \n", config)

# Instantiating logger
sampleLogger = logging.getLogger(__name__)

# Checking with Handler
c_handler = logging.StreamHandler()

sampleLogger.debug('This is debug message...')
sampleLogger.info('This is info message...')
sampleLogger.warning('This is warning message...')
sampleLogger.error('This is error message...')
sampleLogger.critical('This is critical message...')





