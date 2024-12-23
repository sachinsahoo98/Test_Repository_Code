import time

from selenium import webdriver

#creating a chrome driver object
"""
selenium does not directly invoke chrome driver. it invokes chrome driver service that is used to provide webdriver
commands to interact with chrome browser.
As soon as you use webdriver to invoke chrome selenium in the backend tries to look for driver service if not available
local downloads it and invokes browser.
"""

#Invoking different webdrivers
driver1 = webdriver.Chrome()
driver1.get("https://www.google.co.in")

driver2 = webdriver.Firefox()
driver2.get("https://www.youtube.co.in")

driver3 = webdriver.Edge()
driver3.get("https://www.facebook.com")

driver1.close()
driver2.close()
driver3.close()