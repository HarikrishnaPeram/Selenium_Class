import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.implicitly_wait(2)
button=driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']")
button.click()
alert=driver.switch_to.alert
text=alert.text
print("alert message",text)
alert.send_keys("Selenium")
time.sleep(10)
alert.accept()
print("alert  accepted")
text_message= driver.find_element(By.XPATH,"//p[text()='You entered: Selenium']").text
if text_message =="You entered: selenium":
    print("Successful")
else:
    print("Failed")
print(text_message)
driver.close()

