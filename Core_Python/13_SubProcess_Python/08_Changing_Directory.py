
import subprocess
def create_subprocess(self, arg_list=None, input=""):
    try:
        output = subprocess.check_output(arg_list, shell=True, input=input.encode('utf-8'))
        str_output = output.decode()

        return str_output
    except subprocess.CalledProcessError as sub_error:
        returncode = sub_error.returncode
        passed_command = sub_error.cmd

        print("Exception in calling command : %s" % (sub_error.cmd))
        print(f"Return code = %d , Passed Command = '%s' is Invalid in - {passed_command} !"
              f"\nPlease check this command... " % (returncode, sub_error.cmd[returncode - 1]))
        return f"Subprocess calling failed : [Return Code : {returncode}]  passed_command = {passed_command}"


import os
path = 'D:/git_clones/latest_checkout/Angular_Project1__2022-08-12_11_33_07'
print(f"current path = {os.getcwd()}")

os.chdir(path)
print(f"NOw current path = {os.getcwd()}")

