import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Lists.gfg_Cd1 import testObject


class FacebookOperations:

    """Facebook Operations Class"""

    def __init__(self):
        self.driver = webdriver.Chrome()

    def testSetup(self):
        """
        :return:
        """
        #Open FB homepage and maximize window
        self.driver.get("https://www.facebook.com/login/?next=https%3A%2F%2Fwww.facebook.com%2F")
        #maximize the window
        self.driver.maximize_window()

    def checkLogin(self):
        email = "dasshweta23@gmail.com"
        password = "shweta01"
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.NAME, "pass").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@name='login']").click()

    def signUpUser(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT,"Sign up").click()
        self.driver.find_element(By.CSS_SELECTOR,  "input[name='firstname']").send_keys("Rohan")
        self.driver.find_element(By.NAME, "lastname").send_keys("Malhotra")
        bddate = Select(self.driver.find_element(By.NAME, "birthday_day"))
        bddate.select_by_visible_text("6")
        bdmonth = Select(self.driver.find_element(By.ID, "month"))
        bdmonth.select_by_index(1)
        bdyear = Select(self.driver.find_element(By.ID, "year"))
        bdyear.select_by_value("1998")
        self.driver.find_element(By.XPATH, "//input[@value='2']").click()
        self.driver.find_element(By.NAME, "reg_email__").send_keys("test123@gmail.com")
        self.driver.find_element(By.NAME, "reg_passwd__").send_keys("pwd123@1")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(10)

fbObject = FacebookOperations()
fbObject.testSetup()
fbObject.signUpUser()
#fbObject.checkLogin()