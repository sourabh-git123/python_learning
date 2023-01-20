import logging
import subprocess
"""
      Logger configuration that will configure the logs and will put into the file
      that is provided as filename with time and more details 
"""
def logger_config():
      import logging

      # Code to resolution when file not being created - Solved
      for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

      # Code to format logger as of TAF
      logging.basicConfig(format='[%(asctime)s] %(levelname)s [%(filename)s: (line %(lineno)d) ] - %(message)s',
                          level=logging.DEBUG, filename="subprocess_log.txt", datefmt='%d/%m/%y %I:%M:%S %p')


def subprocess_check():
    logger_config()

    # cmd_arg = ['ping', 'google.com']
    # cmd_arg = ['dir', '/p']
    cmd_arg = ['python', 'prime_check.py']
    shell_out = subprocess.check_output(cmd_arg, shell=True)

    # converting output to string format
    string_shell_out = shell_out.decode()

    print(f" shell output = \n"
          f"'{string_shell_out}'")
    print(f"len = {len(string_shell_out)}")

    return string_shell_out


# Like main work
logger_config()
return_str = subprocess_check()

# Dumping log to file
logging.info(return_str)
