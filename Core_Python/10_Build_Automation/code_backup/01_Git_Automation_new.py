import logging
import os
import git
import subprocess

import yaml

"""
    
    Goal Of This TASK : ( Build Automation Automatic Platform To Generate the Buid )
    
        1. Need to take the clone from a git repository, that may be a Angular Project
        2. Check while turning on local host server of Project : ng server      (Validate the console output)
        3. Create Build of that project to deploy with         : ng build       (Validate the console output)
        
"""


class Git():
    def __init__(self, **kwargs):
        try:

            # Code to Read data from yml file
            git_config_file = 'configuration_file/git_automation_conf.yml'

            if os.path.exists(git_config_file):
                with open(git_config_file, 'rt') as file:
                    reading_file = file.read()
                    config_dict = yaml.safe_load(reading_file)
                    # print(f" git_config_json = {config_dict}   ")
            else:
                raise FileNotFoundError(f"\n'{git_config_file}' File is not found in that location.. "
                                        f"\nPlease provide valid file name or path! \n")

            self.step = 0
            self.logger = None
            self.git_config_dict = config_dict
            self.repo_url = config_dict['repo_url']
            self.repo_username = config_dict['username']
            self.repo_password = config_dict['password']

            self.token = config_dict['token']
            self.master_token = config_dict['master_token']
            self.branch = config_dict['branch']

            self.checkout_path = config_dict['checkout_path']
            self.local_path = config_dict['local_path']
            self.log_config_path = config_dict['log_config_file']
            self.log_output_path = config_dict['log_output_file']

            self.operation_list = config_dict['operations']
            print(f">>>>>>>> op list ", self.operation_list)

            print("Deserializing Done !\n")


        except Exception as e:
            import traceback
            print("Exception in Constructor / Init of GIT ")
            print(f"{traceback.print_exc()}")

    """
        Logger configuration : 
            This file will read configuration file yml, all information related to configuration changes is 
            written to the file...
            Note : Need to call logger_config first to utilize logger
    """

    def logger_config(self):

        import logging
        from logging.config import dictConfig
        from datetime import datetime

        try:
            print("Logging Configuration is under processing...")

            """
                Code to Read YML Configuration file while making changes of date in it...
            """

            # import logging
            # logger = logging.getLogger('simpleLogger')
            # logger.setLevel(logging.DEBUG)

            log_config_path = self.log_config_path

            if not os.path.exists(log_config_path):
                raise FileNotFoundError(f"{log_config_path} File not found !"
                                        f"\nPlease provide valid file / path in yml configuration file ! ")

            else:
                with open(log_config_path, 'rt') as file:
                    reading_file = file.read()
                    print("Reading log configuration file...")
                    config_json = yaml.safe_load(reading_file)

                    # print(f"Currently read config json = {config_json} ")

                    # dd mm yyyy time getting
                    today_date = str(datetime.today().strftime('%d-%m-%Y'))

                    log_file_name = config_json['handlers']['file_handler']['filename'][:-4] + '_' + today_date + '.log'
                    print(f"output log_file_name = {log_file_name} ")

                    # Updating log file to the configuration json
                    config_json['handlers']['file_handler']['filename'] = log_file_name

                    # Passing log yml configuration file to the logging constructor via dictConfig
                    dictConfig(config_json)
                    print("Logging configuration Done...\n")

                    # Code to check if logger is working
                    import logging
                    self.logger = logging.getLogger('simpleLogger')
                    self.logger.setLevel(logging.DEBUG)

                    # print(f" \n\ntype = {type(self.logger)}")

                    # print("Checking for many logs...")
                    # for i in range(10):
                    #     self.logger.debug("Log debug message...")
                    #     self.logger.info("Log info message...")
                    #     self.logger.error("Log error message...")
                    #     self.logger.warning("Log warning message...")
                    #     self.logger.critical("Log critical message...")

                    return True

        except Exception as e:
            import traceback
            print(f'Exception while logging configuration :  {traceback.print_exc()} ')
            return False

    """
        Code to clone Project from Remote Repository to Local Repository
    """

    def git_clone(self, repo_url=None, repo_username=None, repo_password=None, local_path=None, branch=None):

        self.logger("Git clone is called...")
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

        self.logger.info("Inside Read from YML...")
        yaml_file = open(config_filename, "r")

        yaml_dict_data = yaml.load(yaml_file, Loader=Loader)
        self.logger.info(f"Currently read yml data : {yaml_dict_data} ")

        return yaml_dict_data

    """
        - This will create a subprocess while taking the command list argument, input and return the output
          of the command in string format
        - This will handle exception based on return code  
          return code :
            0       - for ok 
            1, 2, 3 - for command list[i] element failure 
    """
    def create_subprocess(self, arg_list = None, input = "", execute_path=""):
        try:
            self.step = self.step + 1
            self.logger.info(f"\n\n^^^^^^^^^^^^^^^^^^"
                             f"\n     STEP : {self.step}"
                             f"\n^^^^^^^^^^^^^^^^^^")
            self.logger.info(f"Current path = {os.getcwd()}")
            self.logger.info(f"Calling subprocess for : {arg_list} ")

            if not execute_path == "":
                self.logger.info(f"Changing Path to : {execute_path}")
                os.chdir(execute_path)
                self.logger.info(f"Now current Path : {os.getcwd()} ")

            # Code for change directory , i.e cd directory_name logic
            if arg_list[0] == 'cd' or arg_list[0] == 'CD':
                self.logger.info(f"Changing directory request to : {arg_list[1]} ")
                os.chdir(arg_list[1])
                self.logger.info(f"Changing directory Done..")
                self.logger.info(f"Now current working directory : {os.getcwd()}")
                output = b""
            else:
                output = subprocess.check_output(arg_list, shell=True, input=input.encode('utf-8'))

            # Returning output to string format
            str_output = output.decode()
            self.logger.info(f"Console output : \n'{str_output}' ")

            self.logger.info(f"Return Code : 0, Arg_list = {arg_list}  ")
            self.logger.info(f"Executed Successfully !!")
            return True, str_output

        except subprocess.CalledProcessError as sub_error:
            returncode = sub_error.returncode
            passed_command = sub_error.cmd

            self.logger.info("Exception in calling command : %s" % (sub_error.cmd))
            self.logger.info(f"Return code = %d , Passed Command = '%s' is Invalid in - {passed_command} !"
                             f"\nPlease check this command... " % (returncode, sub_error.cmd[returncode - 1]))
            return False, f"Subprocess calling failed : [Return Code : {returncode}]  passed_command = {passed_command}"

    """
        git_manage : This is entry point of api, that will do the following :
        1. Call Log Configure
        2. Cloning repository
        3. 
            
    """

    # TODO :-
    def git_manage(self):
        try:

            """   1. Configuring logger   """
            self.logger_config()

            """   2. Cloning the repository   """
            self.logger.info("Inside Git Manage...")
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

            # clone_query_string = 'https://' + repo_username + ':' + token + '@' + repo_url[8:]
            clone_query_string = 'https://%s:%s@%s' % (repo_username, token, repo_url[8:])
            #
            # self.logger.info(f"Cloning to local path = {local_path} ")
            # self.logger.info(f"Cloning from query string : {clone_query_string} ")
            # self.logger.info(f"Cloning from query string : {clone_query_string} ")
            #
            # self.logger.info("Cloning...")
            # git.Repo.clone_from(clone_query_string, local_path)
            # self.logger.info("Cloning Done...")

            """ 3. Launch Angular Server of that Repository """
            #
            # self.logger.info("Launching the Angular Server...")
            # # print(f"Current path : {self.create_subprocess(['cd'])}")
            # # print(f"Changing path to : {local_path}")
            #
            # my_angular_project_path = r"D:\git_clones\New_Angular_Project\my_app"
            # cmd_arg = ['ng', 'serve']
            # console_output = self.create_subprocess(arg_list=cmd_arg, execute_path=my_angular_project_path)
            #
            # self.logger.info(f"console_output for Angular launching = \n=={console_output}==\n")

            """  4. Logic to execute all operation at once """
            self.logger.info(f"printing operation list : {self.operation_list}  ")
            self.logger.info("Executing all list from operation list : ")
            for each_cmd_list in self.operation_list:
                output = self.create_subprocess(each_cmd_list.split())
                # self.logger.info(f"\n\nout = {output[1]}  ")

                if output[0] == False:
                    return False, f"Failure on cmd_list : {each_cmd_list} "


        except Exception as e:
            import traceback
            self.logger.info(f"Exception in git manage : {traceback.print_exc()}  ")


def main():
    print("From main...")

    git_obj = Git()
    git_obj.git_manage()

    # Code to : Clone to generate built ok

    """
    cmd_list = ['md', 'angular_demo2']
    print("Creating directory ")
    ret_out = git_obj.create_subprocess(arg_list=cmd_list, input="", execute_path= 'd:/' )
    print("Creating directory ok..")
    print(f'ret_res = \n =={ret_out[1]}== \n\n')

    cmd_list = ['dir', '/p']
    print("Entering to folder  ")
    ret_out = git_obj.create_subprocess(arg_list=cmd_list, input="")
    print("Entering to folder ok..")
    print(f'ret_res = \n =={ret_out[1]}== \n\n')

    cmd_list = ['git', 'clone', 'https://github.com/sourabh-git123/angular_working.git']
    print("cloning here..  ")
    ret_out = git_obj.create_subprocess(arg_list=cmd_list, input="", execute_path = 'd:/angular_demo2')
    print("cloning here done.. ")
    print(f'ret_res = \n =={ret_out[1]}== \n\n')

    cmd_list = ['npm', 'i']
    print("Installing node packages...  ")
    ret_out = git_obj.create_subprocess(arg_list=cmd_list, input="", execute_path = 'd:/angular_demo2/angular_working')
    print("Installing node packages Ok.. ")
    print(f'ret_res = \n =={ret_out[1]}== \n\n')

    cmd_list = ['ng', 'build']
    print("Generating build...  ")
    ret_out = git_obj.create_subprocess(arg_list=cmd_list, input="", execute_path = 'd:/angular_demo2/angular_working')
    print("Generating build... Ok.. ")
    print(f'ret_res = \n =={ret_out[1]}== \n\n')
    """


"""
    Try :
        1. Need to git from private repo that require username/password                     - o with url_string
        2. Need to Read input from : 
        
            Configuration Reading : YAML , Properties , JSON,   (Python most preferable)    - 
            
        3. Make separate function for all steps                                             - 
            
    
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
    2. Next - Search logger in python and need to configure in the project  - Partially used - 
    
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
            
            
            <<<<<  You...  >>>>>
            e. do dump all these log to the console and file while using yml file for conf of log
            f. Follow this paradigm :
               - Interpret each statement command if any failure found then it should show that failure to the user
               and as to the log file also and return with false 
               - While success continue with dumping log to the log file and console also
                
            i.e,
                when success then continue if failure then code exit 
                while showing proper message to the user with the specific error that obtained that time
                "Their is some error : {exception }"
           
       
    ---------------------------------------------------
        # TODO :-  Meeting - 6   ( 22 Aug )
    --------------------------------------------------
    
        0. Do check manually if working :       - o
            clone and 
            ng i
            ng serve
            ng build            
        1. Do use time format in logging_conf.yml for rather than using in code while reading from that
        2. Do check with new updated project from git server name : angular_working 
            a. clone it
            b. do npm i  
            c. ng serve 
            d. ng build 
            
            Note : Project in Git repo is without library so need to do npm i
            
            c. do build to this cloned project that will create a dict folder that is our req to deploy
            d. Do all these steps with your code as well --> 
            e. Note log should be dump while these..
        

"""

if __name__ == "__main__":
    main()
