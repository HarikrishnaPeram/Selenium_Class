import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

#Right click= c
driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)
e1=driver.find_element(By.ID,"field1")
e1.clear()
e2=driver.find_element(By.ID,"field2")
e1.send_keys("hi")
button=driver.find_element(By.XPATH,"//button[text()='Copy Text']")
actions=ActionChains(driver)
actions.double_click(button).perform()
time.sleep(5)
print("Double click")
