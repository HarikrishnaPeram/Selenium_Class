import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(5)
search_bar=driver.find_element(By.NAME,"q")
actions=ActionChains(driver)
actions.click(search_bar)
actions.key_down(keys.Keys.SHIFT)
actions.send_keys("Book")
driver.implicitly_wait(5)
actions.key_up(keys.Keys.SHIFT)
actions.perform()
time.sleep(6)
print("perform")