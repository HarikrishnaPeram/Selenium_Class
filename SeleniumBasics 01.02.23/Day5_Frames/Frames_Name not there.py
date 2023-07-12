#if frame name not available

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://jqueryui.com/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT,"Autocomplete").click()
ele=driver.find_element(By.CLASS_NAME,"demo-frame")
#ele=driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
driver.switch_to.frame(ele)
driver.find_element(By.ID,"tags").send_keys("java")
time.sleep(2)
driver.switch_to.default_content()
driver.find_element(By.LINK_TEXT,"Accordion").click()
print("Frames without name executed")
driver.close()