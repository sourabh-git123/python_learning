import time
import traceback

from selenium import webdriver

driver = webdriver.Chrome()



try:

    driver.get(url)
    print("url opened..")

    # driver.quit()
    time.sleep(2)

    driver.get(url)

except Exception as e:
    print(f"e : {traceback.print_exc()}")

# status = driver.execute(Command.STATUS)





