

import git

from github import Github
from credentials import *

"""
    pyGithub
    
    def __init__(
        self,
        login_or_token=None,
        password=None,
        jwt=None,
        base_url=DEFAULT_BASE_URL,
        timeout=DEFAULT_TIMEOUT,
        user_agent="PyGithub/Python",
        per_page=DEFAULT_PER_PAGE,
        verify=True,
        retry=None,
        pool_size=None,
    ):
"""

url_string = 'https'

git_url = 'https://github.com/sourabh-git123/Angular_Project1.git'
git_user = 'sourabh-git123'
git_password = 'gitpassword123'
git_token = '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'

def git_try1():
    try:

        git_obj = Github(user_agent=git_user, password=git_password)
        # git_obj = Github(login_or_token=git_token, base_url=git_url)
        repos = git_obj.get_user().get_repos()

        user = git_obj.get_user()
        print(user)
        print(user.name)

    except Exception as e:
        import traceback
        print(f"exception occurred : {traceback.print_exc()}  ")

def git_try2():
    from github import Github
    import pickle

    # with open()
    import os






if __name__ == '__main__':
    git_try2()


