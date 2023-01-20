"""
    In this custom logger file code we can create own custom logger that will dump log on
    a. Console
    b. Log File also

"""
import yaml
import logging.config


def console_file():
    import logging

    with open('logging_conf_file.yml', 'r') as file_p:
        config = yaml.safe_load(file_p.read())
        logging.config.dictConfig(config)

    print(f"Reading from configuration file : \n", config)

    try:

        # Create a custom logger
        cust_logger = logging.getLogger(__name__)
        cust_logger.setLevel(logging.DEBUG)

        # 0 Creating Level

        # 1. Creating Formatter  - For Console and File
        simple = logging.Formatter('%(name)s - %(asctime)s - %(message)s')
        cons_formatter = logging.Formatter('%(name)s - %(asctime)s - %(message)s')
        file_formatter = logging.Formatter('%(name)s - %(asctime)s - %(message)s')

        # 2. Creating Handler
        cons_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(filename='abc_file_log.log', mode='w')

        # 3. Setting formatter to handlers - Console and File
        cons_handler.setFormatter(simple)
        file_handler.setFormatter(file_formatter)

        # 3.2 Setting Level to the handler
        # cons_handler.setLevel(logging.INFO)
        # file_handler.setLevel(logging.DEBUG)

        # 4. Now Finally adding handler to the logger
        cust_logger.addHandler(cons_handler)
        cust_logger.addHandler(file_handler)


        # for handler in logging.root.handlers[:]:
        #     logging.root.removeHandler(handler)

        # >> Using logging Now as set
        cust_logger.warning("This is log warning after custom changes")
        cust_logger.error("This is log error after custom changes")
        cust_logger.debug("This is log debug after custom changes")
        cust_logger.info("This is log info after custom changes")
        cust_logger.critical("This is log critical after custom changes")

    except Exception as e:
        import traceback
        print("Exception in console_file1..."
              f"{traceback.print_exc()}")


def console_file1():

    import logging

    cust_logger = logging.getLogger(__name__)

    # Formatter
    file_formatter = logging.Formatter('%(asctime)s - %(message)s')
    cons_formatter = logging.Formatter('%(asctime)s - %(message)s')

    # creating handler
    cons_handler = logging.StreamHandler()
    file_handler = logging.FileHandler('abc_log.log')


    # Adding formatter to the handler
    cons_handler.setFormatter(cons_formatter)
    file_handler.setFormatter(file_formatter)

    # Adding handler to the logger
    cust_logger.addHandler(cons_handler)
    cust_logger.addHandler(file_handler)


    # Checking with example


print("From main...")
console_file()




