
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element(By.NAME,"q").send_keys("Selenium")
driver.find_element(By.NAME,"btnK").submit()


