
# Checking for the availability of the driver instance

from selenium import webdriver
import time
from selenium.webdriver.remote.command import Command

driver = webdriver.Chrome()

url = "https://www.google.com"
driver.get(url)
print("Opened...")

# time.sleep(2)
# driver.refresh()
# print("Refreshed...")

ret_status = driver.execute(Command.STATUS)

print(f"return status = {ret_status}  ")
st = ret_status['value']['ready']
print(st)

print(">>>>>>>>>>")

driver.quit()

try:
    ret_status = driver.execute(Command.STATUS)
    print(f"return status = {ret_status}  ")
    st = ret_status['value']['ready']
    print(st)

except:
    print("Exception : Driver Instance is not available..")

