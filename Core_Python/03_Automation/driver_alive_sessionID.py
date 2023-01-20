import time

from selenium import webdriver

driver = webdriver.Chrome()

url = "https://www.google.com"

driver.get(url)
print("Google opened ok..")

import time
time.sleep(2)

ret = driver.session_id

print(f"Driver session id = {ret}")
print(f"Driver connectable : {driver.service.is_connectable()}")

driver.quit()
print("Driver Quit Ok..")


# is_connectable , will detect if the driver instance is available or not


# ret = True / False
print(f"Driver session id = {driver.session_id} ")
print(f"Driver connectable : {driver.service.is_connectable()}")



