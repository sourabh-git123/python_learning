
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://www.google.com"

driver.get(url)

# image_xpath = '//a[contains(text(), "Image")]'

image_xpath = '//img[contains(@alt, "Google")]'

ret = driver.find_element(By.XPATH, image_xpath).size

print(f"return of find element = {ret}  \n {type(ret)} ")

res = isinstance(ret, dict)   # ==> True

res1 = isinstance(ret, list)   # ==> False

print(f"return of res instance = {res1}  ")

