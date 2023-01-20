import logging
import os
import git
import subprocess

"""
    
    Goal Of This TASK : ( Build Automation Automatic Platform To Generate the Buid )
    
        1. Need to take the clone from a git repository, that may be a Angular Project
        2. Check while turning on local host server of Project : ng server      (Validate the console output)
        3. Create Build of that project to deploy with         : ng build       (Validate the console output)
        
        

"""


class Git():
    def __init__(self, **kwargs):
        try:

            self.kwargs = kwargs
            self.repo_url = kwargs['repo_url']
            self.repo_username = kwargs['repo_username']
            self.repo_password = kwargs['repo_password']
            self.local_path = kwargs['local_path']

        except:
            pass

    def logger_config(self):
        import logging

        # Code to resolution when file not being created - Solved
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        # Code to format logger as of TAF
        logging.basicConfig(format='[%(asctime)s] %(levelname)s [%(filename)s: (line %(lineno)d) ] - %(message)s',
                            level=logging.DEBUG, filename="git_logger.txt", datefmt='%d/%m/%y %I:%M:%S %p')

        # Code to print message as received

    """
        Code to clone Project from Remote Repository to Local Repository
    """

    def git_clone(self, repo_url=None, repo_username=None, repo_password=None, local_path=None, branch=None):

        print("Git clone is called...")
        try:

            if repo_url == None:
                print("Please provide git repository URL")
                return False

            if local_path == None:
                print("Please provide local directory path to clone Project ")
                return False

            print(f"Cloning with following details : {self.kwargs}  ")
            print("Cloning is in processing...")

            # Cloning logic
            git.Repo.clone_from(repo_url, local_path, branch)

        except Exception as e:
            import traceback
            print(f"Exception in git cloning... {traceback.print_exc()}  ")

    def read_yaml_config_data(self, config_filename='git_credentials.yml'):

        import yaml
        from yaml import Loader

        logging.info("Inside Read from YML...")
        yaml_file = open(config_filename, "r")

        yaml_dict_data = yaml.load(yaml_file, Loader=Loader)
        logging.info(f"Currently read yml data : {yaml_dict_data} ")

        return yaml_dict_data

    """
        - This will create a subprocess while taking the command list argument, input and return the output
          of the command
        - This will handle exception based on return code
    """

    def create_subprocess(self, arg_list=None, input="", execute_path=""):
        try:
            print(f"Current path = {os.getcwd()}")
            print(f"Calling subprocess for : {arg_list}")
            if not execute_path == "":
                print(f"Changing Path to : {execute_path}")
                os.chdir(execute_path)
                print(f"Now current Path : {os.getcwd()} ")

            output = subprocess.check_output(arg_list, shell=True, input=input.encode('utf-8'))
            str_output = output.decode()

            return str_output
        except subprocess.CalledProcessError as sub_error:
            returncode = sub_error.returncode
            passed_command = sub_error.cmd

            print("Exception in calling command : %s" % (sub_error.cmd))
            print(f"Return code = %d , Passed Command = '%s' is Invalid in - {passed_command} !"
                  f"\nPlease check this command... " % (returncode, sub_error.cmd[returncode - 1]))
            return f"Subprocess calling failed : [Return Code : {returncode}]  passed_command = {passed_command}"

    """
        git_manage : This is entry point of api, that will do the following :
            
    """
        # TODO :-
    def git_manage(self):
        try:
            # """
            #  1. Cloning the repository
            logging.info("Inside Git Manage...")
            from datetime import datetime

            # Fetching current time to append in the file name
            current_date_time = str(datetime.now())[:-7]

            # time_list = current_date_time.split(' ')

            def remove_char(string=None, split_char=' '):
                # This will remove with split character and append underscore in place of that

                word_list = string.split(split_char)
                new_str = ''
                for each in word_list:
                    new_str = new_str + '_' + each
                return new_str

            # Changing file output name with concatenating time to get new everytime
            current_date_time = remove_char(current_date_time, ' ')
            current_date_time = remove_char(current_date_time, ':')

            # Reading conf data from yml file
            config_data = self.read_yaml_config_data('git_creds.yml')

            # Extracting value from config data
            repo_url = config_data['repo_url']
            repo_username = config_data['username']
            repo_password = config_data['password']
            branch = config_data['branch']
            token = config_data['token']
            operation_list = config_data['operation']
            local_path = config_data['checkout_path'] + '/' + repo_url.split('/')[-1][:-4] + current_date_time

            # Creating Query string with token to clone git repository
            # query_string3 = 'https://sourabh-git123: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@github.com/sourabh-git123/Angular_Project1.git'

            # https://<username>:<githubtoken>@github.com/<username>/<repositoryname>.git

            # clone_query_string = 'https://' + repo_username + ':' + token + '@' + repo_url[8:]
            clone_query_string = 'https://%s:%s@%s' % (repo_username, token, repo_url[8:])

            logging.info(f"Cloning to local path = {local_path} ")
            logging.info(f"Cloning from query string : {clone_query_string} ")
            print(f"Cloning from query string : {clone_query_string} ")

            print("Cloning...")

            git.Repo.clone_from(clone_query_string, local_path)

            print("Cloning Done...")
            logging.info("Cloning Done...")
            
            # """

            """ 2. Launch Angular Server of that Repository """
            print("Launching the Angular Server...")
            # print(f"Current path : {self.create_subprocess(['cd'])}")
            # print(f"Changing path to : {local_path}")

            # arg_list = ['cd']
            # arg_list.append(local_path)
            # print(f"new cd :>  {arg_list} ")
            # self.create_subprocess(arg_list)

            # print(f"Current path : {self.create_subprocess(['cd'])}")
            my_angular_project_path = r"D:\git_clones\New_Angular_Project\my_app"
            cmd_arg = ['ng', 'serve']
            console_output = self.create_subprocess(arg_list=cmd_arg, execute_path=my_angular_project_path)

            print(f"console_output for Angular launching = \n=={console_output}==")


        except Exception as e:
            import traceback
            print(f"Exception in git manage : {traceback.print_exc()}  ")


def main():
    import time
    print("From main...")

    git_obj = Git()
    git_obj.logger_config()

    git_obj.git_manage()
    time.sleep(20)


"""
    Try :
        1. Need to git from private repo that require username/password
        2. Need to Read input from : 
        
            Configuration Reading : YAML , Properties , JSON,   (Python most preferable)
            
        3. Make separate function for all steps
            
    
    Need to Read from input file from separate file : 
    
    Different methods :
    
    Read property 
    Clone 
    
    
    Covered (2/8/22) : 
    
    1. read yml data from file
    2. created own private git repository
        able to clone private repository in with git bash
        
        
    Task on 5 Aug : 
    
    1. Now Read from property --  OK
    2. Next - Search logger in python and need to configure in the project  - Partially used
    
    -------------------------------
    
    Do These 8 / 8 / 22
    
    1. Use Git library to use username and password , instead of using while reading from yml file and concatenating
    2. Check which git uses the log by default and dumps into the logger file
    3. Check log levels
    
    Do These 8/8/22  Meeting - 2
    
    
    1. Use format string %d, %s like wise in url string     ---o
    2. Check how to call shell script from python and to use log dump   ---
    3. Call linux command dump there log                    ---o                               
    
    ---------------------------------------
    # TODO : 10 August Meeting - 3
    ---------------------------------------
    0. check of return of failure of subprocess output  --  error 1, success 0                          -- o
    1. install node, from npm site                      --  download npm and install                    -- o
    2. install angular cli , from angular site          --                                              -- o     
    3  npm -i = install angular packages                --  ??
    4. ng serve - do start angular server , open and if local server is running in browser at that IP.  -- For testing only     -- o
    5. ng build - need to build of angular project      --                                              -- For testing only     -- o
    
    
        install angular cli - 
            install -g @angular/cli@latest
        run angular project
            ng serve
        angular version check latest version 
            ng version

    # TODO:- Sunil - ( We will do with live example )
    1. take checkout                                
        Go to that folder and Do these: 
    2. do npm -i []   # package will be in angular.json / inside angular.json
    3. create build
    4. logging
    
    
    TODO :- Improve your logging with the following...
    
    5.  a. Every run should generate different log file 
        b. if log file is > 10 MB then create next log file in the same day with different file name.
            eg - log_file1.txt  log_file2.txt    (size base policy)
        c. One folder can maximum contain 10 files only, oldest should be deleted...
            eg -                                 (Time base policy)
                                                 (History of 10 days we will keep)
                                                 
        d. Do check with logging.conf file how to use pass through logging.conf 
        e. Set log configuration file and read configuration related things from configuration file...
        
    [ Adding Some more Points ]

        f. Use yaml file for configuration 
        g. Combine for both of the file of : 
            TimeRotatingFileHandler & RotatingFileHandler
        h. Add Rotating information in the configuration file - yaml 
        
    ---------------------------------------------------
    # TODO : 18 AUGUST - Meeting 4  
    ---------------------------------------------------
        We should try to make naming convention of file like this :
        
        1. Make log format like 
            filename_date.log       -   o
        
        2. Need to Run These steps to launch with the help of subprocess in python and have to follow these process
            a. do cd
            b. goto that folder while providing the path 
            c. npm i        -> install lib of project
            d. ng build     
            
            e. do dump all these log to the console and file while using yml file for conf of log
            f. Follow this paradigm :
               - Interpret each statement command if any failure found then it should show that failure to the user
               and as to the log file also and return with false 
               - While success continue with dumping log to the log file and console also
                
            i.e,
                when success then continue if failure then code exit 
                while showing proper message to the user with the specific error that obtained that time
                "Their is some error : {exception }"
           
        
        
        

"""

if __name__ == "__main__":
    main()
