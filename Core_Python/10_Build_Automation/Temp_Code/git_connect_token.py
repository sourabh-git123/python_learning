

from github import Github

def read_repo1():
    try:

        master_token = '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'
        # git_hub_obj = Github(base_url='https://github.com/sourabh-git123/Angular_Project1.git', login_or_token='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')
        git_hub_obj = Github(base_url='https://github.com/sourabh-git123/Angular_Project1.git', login_or_token=master_token)
        repos = git_hub_obj.get_user().get_repos('sourabh-git123/Angular_Project1')
        print(repos)

        for each_repo in repos:
            print(each_repo)
            each_repo.edit(has_wiki=False)
            print("false set...")
            print(dir(each_repo))

    except Exception as e:
        import traceback

        print(f"Exception in Github : {traceback.print_exc()}  ")

def read_repo2():
    try:

        username = 'sourabh - git123'
        password = 'root123'
        git_obj = Github(username, password, base_url='https://github.com/sourabh-git123/Angular_Project1.git')

        user = git_obj.get_user()
        print(user.name)

    except Exception as e:
        import traceback
        print(f"Exception in read_repo2 : {traceback.print_exc()} ")


# read_repo2()

# def read_repo3



