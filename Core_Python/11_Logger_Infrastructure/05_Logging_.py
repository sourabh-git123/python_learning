"""
    Start with Root Logger


"""

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%y %H:%M:%S %p')

logging.info("Logging Information ")