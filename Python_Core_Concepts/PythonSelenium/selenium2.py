import time

from selenium import webdriver

driverObj = webdriver.Firefox()
#Landing on the URL
driverObj.get("https:\\www.google.co.in")
#Maximize Window
driverObj.maximize_window()

#Printing the URL of the Page
print(driverObj.current_url)
#Printing the title of the page
print(driverObj.title)

#close the driver
driverObj.close()
