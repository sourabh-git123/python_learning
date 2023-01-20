"""
    In this with subprocess we can launch program,
    facing output issue in string with windows platform

"""

import subprocess

cmd_arg_w = ['dir', '/p']
console_out = subprocess.run(cmd_arg_w, shell=True)

print("console output = %s" %(console_out.returncode))


# Return in case of failure
print("Return in case of failure : ")
cmd_arg_w = ['dirr', '/p']
console_out = subprocess.run(cmd_arg_w, shell=True)
print("console output = %s" %(console_out.returncode))


# Taking output of string
print(">> Taking list of files : ")
cmd_arg_w = ['dir', '/p']

# For linux
# list_of_files = subprocess.run(cmd_arg_w, capture_output=True, text=True)

list_of_files = subprocess.run(cmd_arg_w, shell=True, text=True)
print(f"list of files = {type(list_of_files.stdout)}")

# Lounching jupitet
print("Launching jupiter >>>>>>>>")
# subprocess.run(['python', '-m', 'notebook'], shell=True)   # not working

print("Launching vs code >>>>>>")
subprocess.call(['code', '.'], shell=True)







