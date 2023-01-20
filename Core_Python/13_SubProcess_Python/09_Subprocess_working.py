"""
    Here we have checked while changing the paths
    checked while creating many folders automatedly with subprocess



"""
import os
import subprocess

def create_subprocess(arg_list=None, input="", execute_path=""):
    try:
        print(f"Current path = {os.getcwd()}")
        print(f"Calling subprocess for : {arg_list}")
        if not execute_path == "":
            print(f"Changing Path to : {execute_path}")
            os.chdir(execute_path)
            print(f"Now current Path : {os.getcwd()} ")

        output = subprocess.check_output(arg_list, shell=True, input=input.encode('utf-8'))

        # Returning output to string format
        str_output = output.decode()

        return True, str_output

    except subprocess.CalledProcessError as sub_error:
        returncode = sub_error.returncode
        passed_command = sub_error.cmd

        print("Exception in calling command : %s" % (sub_error.cmd))
        print(f"Return code = %d , Passed Command = '%s' is Invalid in - {passed_command} !"
                         f"\nPlease check this command... " % (returncode, sub_error.cmd[returncode - 1]))
        return False, f"Subprocess calling failed : [Return Code : {returncode}]  passed_command = {passed_command}"

arg_list = ['dir', '/p']
output = create_subprocess(arg_list = arg_list)
print(f"\n\nnow output \n==={output[1]}===\n")

os.chdir(r'D:\Programming_Practice\Core_Python\13_SubProcess_Python\demo_angular')
print(f">>> {create_subprocess(['cd'])[1]}")

arg_list = ['dir', '/p']
output = create_subprocess(arg_list = arg_list)
print(f"\n\nnow output \n==={output[1]}===\n")

arg_list = [
    ['md', 'folder_1'],
    ['md', 'folder_2'],
    ['md', 'folder_3'],
    ['md', 'folder_4']
]
for each_list in arg_list:
    output = create_subprocess(each_list)
    print("=====================  output  ========================"
          f"\n '{output[1]}'\n"
          f"====================   end   ========================")

arg_list = ['dir', '/p']
output = create_subprocess(arg_list = arg_list)
print(f"\n\nnow output \n==={output[1]}===\n")


"""
Note :  while changing the path you have two ways :
    1. path from beginning 
    2. path from current folder as well
"""