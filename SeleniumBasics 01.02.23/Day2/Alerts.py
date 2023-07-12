import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(2)
button=driver.find_element(By.XPATH,"//button[text()='Click Me']")
button.click()
alert=driver.switch_to.alert
text=alert.text
time.sleep(2)
#alert.aceept()
alert.dismiss()
print("Alert dismissed")
driver.close()