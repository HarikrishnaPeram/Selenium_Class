import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://chercher.tech/practice/hidden-division-popup")
driver.maximize_window()
driver.implicitly_wait(2)
driver.find_element(By.XPATH,"//*[text()='View Pop-up']").click()
driver.find_element(By.XPATH,"//p[contains(text(),'Modal')]//following::input[1]").send_keys("Hidden divison text")
time.sleep(5)
driver.close()