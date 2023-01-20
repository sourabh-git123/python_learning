
import logging

"""
Note : INFO message is not displayed
"""

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.warning("This is info from root logger..")

# With custom logger
cust_logger = logging.getLogger('example logger')
cust_logger.warning('From Custom logger ')




