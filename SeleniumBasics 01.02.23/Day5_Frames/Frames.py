#if frame name available

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://netbanking.hdfcbank.com/netbanking/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.switch_to.frame("login_page")
driver.find_element(By.NAME,"fldLoginUserId").send_keys("Harikrishna")
print("Entered data ")
driver.close()
