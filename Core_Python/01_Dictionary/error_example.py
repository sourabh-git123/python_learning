import time

# Checking for error content
def check_error_content():
    try:
        # It will return the content of error or Success message
        error_list = ['error ']
        time.sleep(1)
        error_content_text = "Cannot connect to net"
        print(f"Error Content : {error_content_text} ")

        # checking for error content in error list
        for each_error in error_list:
            if error_content_text[10:-10] in each_error:
                return True, error_content_text

        return False, "No error message found !"
    except:
        return False, "No error message found !"

return_status = check_error_content()

print(f"return_status = {return_status}  ")
