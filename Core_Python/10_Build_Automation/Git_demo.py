
import git
import os

"""
    Working Code     
"""

try:

    print("Cloning...")
    git_user = 'sourabh-git123'
    git_password = 'gitpassword123'
    git_token = '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'

    query_string = 'https://' + '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' + 'x-oauth-basic@' + 'github.com/sourabh-git123/Angular_Project1.git'
    query_string2 = 'https://sourabh-git123:gitpassword123@github.com/sourabh-git123/Angular_Project1.git'
    query_string3 = 'https://sourabh-git123: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@github.com/sourabh-git123/Angular_Project1.git'


    private_repo_url = 'https://github.com/sourabh-git123/Angular_Project1.git'
    public_repo_url = 'https://github.com/DanWahlin/Angular-HelloWorld'

    new_token = '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'

    path = "/tmp/git_clones/sourabh_private_repo/lates2"

    # git.Repo.clone_from(private_repo_url, path, branch = "master")

    git.Repo.clone_from(query_string3, path)

    print("Cloning.. Done..")


except Exception as e:
    import traceback
    print(f"Exception in cloning...{traceback.format_exception()}   ")


"""

    1. Now Read from property 
    2. Next - Search logger in python and need to configure in the project

"""

