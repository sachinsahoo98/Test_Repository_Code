"""
To identify elements using locators in Webpage

1.name
2.Classname
3.CSS Selector
4.Link Text
5.ID
6.XPATH

"""

import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driverObject = webdriver.Chrome()
driverObject.get("https://rahulshettyacademy.com/angularpractice/")
driverObject.maximize_window()
print("Title of webpage is:", driverObject.title)
print("Current url is:", driverObject.current_url)
#Find Element by Name
driverObject.find_element(By.NAME, "name").send_keys("Rihaan")
driverObject.find_element(By.NAME, "email").send_keys("rmalhotra@gmail.com")
#Find Element by ID
driverObject.find_element(By.ID, "exampleInputPassword1").send_keys("testpassword")
driverObject.find_element(By.ID, "exampleCheck1").click()
appearance = Select(driverObject.find_element(By.ID, "exampleFormControlSelect1"))
appearance.select_by_visible_text("Male")
driverObject.find_element(By.NAME, "bday").send_keys("15/06/1998")
#sample syntax for XPATH Creation: //tagname[@attribute=value]

"""sample syntax for CSS Selection: tagname[attribute=value], it can be also constructed taking any attribute
#using ID syntax -> #IDname
#using className syntax -> .className
"""

driverObject.find_element(By.CSS_SELECTOR,"input[id='inlineRadio1']").click()
driverObject.find_element(By.XPATH, "//input[@type='submit']").click()
resultMsg = driverObject.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
print(resultMsg)
assert "Success" in resultMsg
driverObject.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys(" Malhotra")

time.sleep(2)
driverObject.close()