
"""

    subprocess.CalledProcessError  -
        return code -
            0 - Success
            1 - When 1st arg is raising exception
            2 - When 2nd arg is raising exception
"""

import subprocess

try:

    cmd_arg = ['pythonn', 'prime_check.py']
    output = subprocess.check_output(cmd_arg, shell=True, input=b'18')

    new_output = output.decode()
    print(f"\n new_output = \n'{new_output}'  ")

except subprocess.CalledProcessError as cp_error:

    print("\n\nExc : Error in calling subprocess ")

    # print(f"Exc Name return code : {subprocess.CalledProcessError.returncode}  ")
    print(f"Exc Name return code : =={cp_error.returncode}== ,type = {type(cp_error.returncode)} ") # 2
    print(f"Exc Name return code : =={cp_error.stdout}==  ")     # b''
    print(f"Exc Name return code : =={cp_error.cmd}==  ")        # ['python', 'prime_check.p']
    print(f"Exc Name return code : =={cp_error.stderr}==  ")     # None
    print(f"Exc Name return code : =={cp_error.output}==  ")     # b''
    # print(f"Exc Name : {[subprocess.CalledProcessError]}  ")
    returncode = cp_error.returncode
    print("Return code = %d , command = '%s' is invalid ! \nPlease check this command... " % (returncode, cp_error.cmd[returncode - 1]))

except Exception as e:
    print("Exception in subprocess")


    # abcdefg