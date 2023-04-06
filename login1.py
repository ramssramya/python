import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://demo.opencart.com/")
driver.find_element(By.LINK_TEXT, "My Account").click()
driver.find_element(By.LINK_TEXT, "Login").click()
time.sleep(5)
if driver.title == "Your Store":
    print("title is matched")
else:
    print("title not matched")
time.sleep(4)
driver.find_element(By.ID, "input-email").send_keys("username")
driver.find_element(By.ID, "input-password").send_keys("password123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)
driver.quit()