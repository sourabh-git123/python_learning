import json

private_repo_url = 'https://github.com/sourabh-git123/Angular_Project1.git'
public_repo_url = 'https://github.com/DanWahlin/Angular-HelloWorld'

kwargs_json = {
    "repo_url": private_repo_url,
    "repo_username": "root",
    "repo_password": "root123",
    "local_path": '/tmp/sourabh_private_repo',
    "live_status" : True
}

yaml_data = json.dumps(kwargs_json, indent=4, default=str)

print(f"yaml = {yaml_data}  ")


