import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("http://www.tizag.com/javascriptT/javascriptalert.php")
driver.maximize_window()
driver.implicitly_wait(2)
button=driver.find_element(By.XPATH,"//input[@value='Confirmation Alert']")
button.click()
alert=driver.switch_to.alert
text=alert.text
print("Alert message is",text)
time.sleep(2)
alert.accept()
print("alert accepted")
driver.close()