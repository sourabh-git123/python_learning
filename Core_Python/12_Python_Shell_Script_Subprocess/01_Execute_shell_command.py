"""
    OS Module :

    res =
        0 - Success
        1 - Failure

"""
import os

cmd = "ping facebook.com"
# cmd = "dir"

# os.system will return response of 0/1 of status of running of the command
cmd_res = os.system(cmd)
print(cmd_res)

# To take output in the var we use os.popen(cmd)
output_console = os.popen(cmd)
print(f"output = '%s'  len = %s" % (output_console.read(), type(output_console.read())))















