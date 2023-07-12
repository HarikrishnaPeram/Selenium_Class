import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)
speed=driver.find_element(By.ID,"speed")
sel_speed=Select(speed)
sel_speed.select_by_visible_text("Medium")
time.sleep(10)
files=driver.find_element(By.ID,"files")
sel_files=Select(files)
sel_files.select_by_value("3")
time.sleep(10)
animals=driver.find_element(By.ID,"animals")
sel_animals=Select(animals)
sel_animals.select_by_index("2")
time.sleep(10)