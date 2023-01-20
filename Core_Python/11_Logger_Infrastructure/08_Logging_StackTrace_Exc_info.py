
import logging

a = 7
b = 0

logging.basicConfig(filename="logger_demo.log", format="%(asctime)s - %(message)s", level=logging.DEBUG, filemode='a')

try:

    c = a/b
    print(c)

except Exception as e:

    logging.error(f"Exception on dividing :", exc_info=True)

