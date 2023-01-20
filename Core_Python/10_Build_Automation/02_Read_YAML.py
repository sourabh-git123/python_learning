
import yaml
from yaml import Loader

yaml_file = open('git_creds.yml', 'r')

yaml_data = yaml.load(yaml_file, Loader = Loader)

print(f"yaml type = {type(yaml_data)}  ")
print(f"yaml type = {(yaml_data)}  ")

