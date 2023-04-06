import self as self
from selenium.webdriver.common.by import By

class registerpage:
    myaccountlink = "My Account"
    registerlink = "Register"
    firstname = "input-firstname"
    lastname = "input-lastname"
    email = "input-email"
    password = "input-password"
    name = "agree"
    submitbutton = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver
    def clickonmyaccount(self):
        self.driver.find_element(By.LINK_TEXT, self.myaccountlink).click()
    def clickonregisterlink(self):
        self.driver.find_element(By.LINK_TEXT, self.registerlink).click()
    def enterfirstname(self,firstname):
        self.driver.find_element(By.ID, self.firstname).send_keys(firstname)
    def enterlastname(self,lastname):
        self.driver.find_element(By.ID, self.lastname).send_keys(lastname)
    def enteremail(self, email):
        self.driver.find_element(By.ID, self.email).send_keys(email)
    def enterpassword(self, password):
        self.driver.find_element(By.ID, self.password).send_keys(password)
    def clickonname(self):
        self.driver.find_element(By.NAME, self.name).click()
    def clickonsubmit(self):
        self.driver.find_element(By.XPATH, self.submitbutton).click()