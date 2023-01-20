
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import sys

chrome_obj = ChromeDriverManager()
ret_path = chrome_obj.install()
driver = webdriver.Chrome(ret_path)


# driver = webdriver.Chrome(executable_path=chrome_obj.install(),
#                                chrome_options=chrome_options)

print(f"return path = {ret_path} ")

driver.get('https://www.google.com')



# path = sys.argv[0]

# path = 'D:/Programming_Practice/Core_Python/03_Automation/'
# print(f"path = {path} ")
#
# driver = webdriver.Chrome(ChromeDriverManager.install() )
#
# driver.get(url='https://www.google.com')