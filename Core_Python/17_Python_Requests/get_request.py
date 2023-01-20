import requests


try:

    authentication_code = 'hasbdf86ssdf'
    url  = 'http://ip job/TASK_12_Jenkins_CI_CD_Build_Trigger_Remotely/build?token=' + authentication_code

    root_url = 'http:/ip /buildByToken/build?job=TASK_12_Jenkins_CI_CD_Build_Trigger_Remotely&token=hasbdf86ssdf'

    print("Lets to get requesting / build trigger...")
    res = requests.post(url = root_url)
    print("Request done...")
    print("Build Trigger Done...")


    print(f"res of req = {res}  ")
    print(f"type of req = {type(res)}  ")


except Exception as e:
    import traceback

    print(f"exception in request module : {traceback.format_exc()}  ")

