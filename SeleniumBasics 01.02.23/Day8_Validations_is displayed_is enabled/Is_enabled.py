import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_pushbutton_disabled2")
driver.maximize_window()
driver.implicitly_wait(2)
driver.switch_to.frame("iframeResult")
e1=driver.find_element(By.XPATH,"//button[text()='My Button']")
print("is enabled")
e1state=e1.is_enabled()
print("E1 is enable->"+str(e1state))
print("is enabled sample")
print(e1state)
e2=driver.find_element(By.XPATH,"//button[text()='Try it']")
e2.click()
time.sleep(4)
e1state=e1.is_enabled()
print("E1 is enabled ->"+str(e1state))