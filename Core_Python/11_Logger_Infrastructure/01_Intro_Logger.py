"""
Logger Levels :
    DEBUG
    INFO
    WARNING
    ERROR
    CRITICAL


    DEBUG   -
    INFO    - We use it to pass the information that we are doing
    WARNING - Error may happened in the future
    ERROR   - Series problem
    CRITICAL - More series error

    Current Log :
        INFO:root: Info message

    Logger Format :
        [date_time, code_line] INFO [filename]:root: Info message


"""

import logging

logging.warning(" Warning Message")
logging.info(" Info message")          # It will not print threshold set to warning
logging.error(" error message")

"""
     Lets put it into the file
"""

import os
log_path = os.getcwd() + '/logging_file.log'
print(log_path)

# Issue resolution for not generation of the logging file
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(filename="logs/log_file.log", level=logging.DEBUG)

logging.warning(" Warning Message")
logging.info(" Info message")          # It will not print threshold set to warning
logging.error(" error message")



















