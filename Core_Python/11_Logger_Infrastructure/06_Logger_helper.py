"""
    This will only dump error log in the file
    using logging file : happy_loggin.conf
"""
import logging

logger = logging.getLogger(__name__)
logger.info('This is from logger Helper')

# Creating handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('logs/file_file.log')

# level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s  -  %(levelname)s  -   %(message)s')

stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(file_h)
logger.addHandler(stream_h)

logger.warning('This is a warning of logger')
logger.error('This is a error')














