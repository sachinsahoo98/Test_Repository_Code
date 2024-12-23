import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class YatraTestClass:

    """
    Documentation:
    """
    def __init__(self):
        self.driverObject = None

    def handleNotifications(self):
        try:
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-notifications")
            options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
            self.driverObject = webdriver.Chrome(options=options)
        except:
            print("Disabling didn't work")

    def yatraTestCheck(self):
        #Land on the webPage
        self.driverObject.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        print(self.driverObject.current_url)
        print(self.driverObject.title)
        self.driverObject.maximize_window()
        time.sleep(2)

    def loginUser(self):
        #Hover to login webelement and click it to go login page
        self.driverObject.find_element(By.XPATH, "//button[@type='submit']").click()

    def createUser(self):
        emailID = "saruy@gmail.com"
        phoneNum = 8789754312
        passWord = '$Achin06'

        time.sleep(3)

        #click signup page
        self.driverObject.find_element(By.CSS_SELECTOR, "button[type='button']").click()
        #provide the email id
        self.driverObject.find_element(By.NAME,"login-input").send_keys(emailID)
        #click signup button
        self.driverObject.find_element(By.ID, "login-continue-btn").click()
        time.sleep(3)
        #provide phoneNum and Password
        try:
            (WebDriverWait(self.driverObject, 10).until
             (EC.element_to_be_clickable((By.ID, "signup-mobile-number"))).send_keys(str(phoneNum)))
            (WebDriverWait(self.driverObject, 10).until
             (EC.element_to_be_clickable((By.ID, "signup-password"))).send_keys(passWord))
        except Exception as e:
            print("Element is not interactable due to error {}".format(e))

        selectedObj = Select(self.driverObject.find_element(By.ID, "signup-user-designation"))
        selectedObj.select_by_visible_text("Mr.")
        self.driverObject.find_element(By.ID, "signup-user-first-name").send_keys("Sachin")
        self.driverObject.find_element(By.ID, "signup-user-last-name").send_keys("Sahoo")
        self.driverObject.find_element(By.XPATH, "//label[@for='specialPromoNotif']").click()
        self.driverObject.find_element(By.XPATH, "//label[@for='whatsAppNotif']").click()
        self.driverObject.find_element(By.XPATH, "//button[@id='signup-form-continue-btn']").click()
        time.sleep(2)

    def closeBrowser(self):
        self.driverObject.close()

ytestObj = YatraTestClass()
ytestObj.handleNotifications()
ytestObj.yatraTestCheck()
ytestObj.createUser()
ytestObj.closeBrowser()