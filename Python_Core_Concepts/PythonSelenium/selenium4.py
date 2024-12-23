from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time
dObject = webdriver.Chrome()
dObject.get("https://rahulshettyacademy.com/client")
#Print title and current_url
print(dObject.title)
print(dObject.current_url)
dObject.maximize_window()
dObject.find_element(By.LINK_TEXT, "Register").click()
dObject.find_element(By.CSS_SELECTOR, "#firstName").send_keys("Sachin")
dObject.find_element(By.XPATH, "//input[@type='lastName']").send_keys("Sahoo")
dObject.find_element(By.CSS_SELECTOR, )

time.sleep(2)