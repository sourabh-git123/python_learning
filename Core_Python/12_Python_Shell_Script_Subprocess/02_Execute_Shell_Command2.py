import os

# Run shell
os.system("echo ")
d_root = os.system("cd d:/")
print("command exit code : %d" %(d_root))

# With subprocess
import subprocess
list_files = subprocess.run(['dir', 'cd d:/'])

print("The exit code of above run command : %s" %(list_files))

subprocess.run(['dir /p', 'dir'], shell=True)






