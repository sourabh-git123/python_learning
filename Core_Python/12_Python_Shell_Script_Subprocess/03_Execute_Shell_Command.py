
import subprocess

cmd_list = ['ping', 'google.com']
# cmd_list = ['python', 'prime_check.py']
process = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, universal_newlines=True)

# output = process.stdout.readline()

# print(f"output = %s" %(output.strip()))

# return_code = process.poll()

# print(f"return code = {return_code} ")

while True:
    output = process.stdout.readline()
    print(output.strip())

    code = process.poll()
    if not code == None:
        print(f"return code = {code} ")

        for output in process.stdout.readlines():
            print(output.strip())
        break