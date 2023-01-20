
import subprocess

"""
    subprocess.call
        return 0 / 1   <-- gives output
        
"""

cmd_arg = ['dir', '/p']
out1 = subprocess.check_output(cmd_arg, shell=True)


"""
       subprocess.check_output
              -> it will 
"""

"""
    Output working fine
        1. use subprocess.check_output
        2. decode byte output to the string format

"""

# Here in out we are receiving in byte format need to convert into string format with decode
# cmd_arg = ['dir', '/p']
cmd_arg = ['git', 'clone', 'https://github.com/sourabh-git123/angular_working.git']
out = subprocess.check_output(cmd_arg, shell=True)
print(f"output = tycheck_output = {type(out)},  \n\n\n\n==> '   '")


print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("Converting to string format >>>>>>>>")
new_output = out.decode()

print(f"output type =  {type(new_output)} ")
print(f"---------------\n"
      f"Printing output\n"
      f"--------------- \n"
      f"'''{new_output}'''  ")

"""
    subprocess.run
"""










