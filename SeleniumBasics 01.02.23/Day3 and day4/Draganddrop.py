import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)
source=driver.find_element(By.ID,"draggable")
dest=driver.find_element(By.ID,"droppable")
actions=ActionChains(driver)
actions.click_and_hold(source).move_to_element(dest).release(source).perform()
time.sleep(10)
print("dragg and drop")