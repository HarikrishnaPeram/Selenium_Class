import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.gmail.com")
driver.maximize_window()
driver.implicitly_wait(3)
ele=driver.find_element(By.CSS_SELECTOR,"input[name='identifier']").send_keys("Selenium")
time.sleep(5)