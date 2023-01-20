
import subprocess

print("From Python File Running C Program...")

# The first program that to start and second is the command line
# argument like -  gcc c_file.c

# """
    # TODO:- we have to call python subprocess with calling shell script
# """ cccccccc

# cmd_list = ['gcc', 'c_file.c']
cmd_list = ['python', 'prime_check.py']
console_out = subprocess.call(cmd_list)
# subprocess.call("./a.out")

print("Running Program Done...")

print("Printing Console output : ")
print()






