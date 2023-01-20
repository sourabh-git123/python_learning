"""

    Logger Format - In which type we want to dump the log we deside and give the format
        https://docs.python.org/3/library/logging.html#logrecord-attributes

    Expectation of log :
        [date_time, code_line] INFO [filename]:root: Info message

    Example :

"""
import logging

# Logging with info and message
# out - INFO : Info message with format
# logging.basicConfig(format='%(levelname)s : %(message)s' , level=logging.DEBUG)
# logging.info("Info message with format ")

# Logging with time :  ( Logging actual format as of out TAF logger )

# out - [2022-08-05 16:05:31,190] INFO [01_Git_Automation.py: (line 56) ] - Cloning Done...
# logging.basicConfig(format = '[%(asctime)s] %(levelname)s [%(filename)s: (line %(lineno)d) ] - %(message)s', level=logging.DEBUG)
# logging.info("Info message with time and label")

# lets set time format also
# out - [05/08/22 04:24:13 PM] INFO [02_Changing_format_log.py: (line 30) ] - Info message with time and label

logging.basicConfig(format = '[%(asctime)s] %(levelname)s [%(filename)s: (line %(lineno)d) ] - %(message)s', datefmt= '%d/%m/%y %I:%M:%S %p', level= logging.DEBUG )
logging.info("Info message with time and label ")








