
import subprocess

# run can run parallel many process
subprocess.run("ls -la", shell = True)      # not supported in windows
subprocess.run("dir /p", shell = True)      # for windows

# we can pass a list seperating by space
print("For windows...")
cmd = ["ls", "-la"]
cmd_w = ["dir", "/p"]
subprocess.run(cmd_w, shell=True)



