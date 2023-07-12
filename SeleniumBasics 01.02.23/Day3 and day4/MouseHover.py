import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

#Right click= c
driver=webdriver.Chrome()
driver.get("https://amazon.in/")
driver.maximize_window()
driver.implicitly_wait(2)
e1=driver.find_element(By.ID,"nav-link-accountList")
actions=ActionChains(driver)
actions.move_to_element(e1).perform()
time.sleep(5)
print("MouseHover")