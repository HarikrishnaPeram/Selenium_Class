from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(2)
speed=driver.find_element(By.ID,"speed")
sel_speed=Select(speed)
if (sel_speed.is_multiple):
    print("This is multiple select")
else:
    print("This is not multiple select")