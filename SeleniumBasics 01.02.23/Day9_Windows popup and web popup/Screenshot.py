import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.maximize_window()
driver.implicitly_wait(2)
driver.find_element(By.ID,"Email").clear()
driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
Password=driver.find_element(By.ID,"Password")
Password.clear()
Password.send_keys("admin")
driver.find_element(By.XPATH,"//button[@type='submit']").submit()
print("Login successfully")
time.sleep(5)
print(driver.title)
assert driver.title=="Dashboard / nopCommerce administration"
driver.get_screenshot_as_png()
driver.save_screenshot("s123.png")