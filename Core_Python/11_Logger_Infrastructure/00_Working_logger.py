
"""
    This logging module we will use in our project
"""
import logging


class Custom_loger():
    def __init__(self):
        pass
        # self.message = message
        # self.logger = logging.basicConfig(format = '[%(asctime)s] %(levelname)s [%(filename)s: (line %(lineno)d) ] - %(message)s', level=logging.DEBUG)

    # def logger(self):
    #
    #     # logging.basicConfig(format = '[%(asctime)s] %(levelname)s [%(filename)s: (line %(lineno)d) ] - %(message)s', level=logging.DEBUG)
    #     # logging.info("Info message with time and label")
    #     pass

    def print_logger(self):
        self.logger.info("Hello")

    # class logger():
    #     def __init__(self):
    #         pass
    #
    #     def info(self):
    #         logging.basicConfig(format='[%(asctime)s] %(levelname)s [%(filename)s: (line %(lineno)d) ] - %(message)s',
    #                             level=logging.DEBUG)
    #         logging.info(self.message)
    #
    """
        This is working logger that we will use in out Build Automation Project
    """
    def logger(self):
        pass

def main():
    obj = Custom_loger()
    # obj.logger().
    obj.print_logger()


if __name__ == '__main__':
    main()


