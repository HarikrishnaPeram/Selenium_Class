from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.maximize_window()
driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID,"Password").clear()
driver.find_element(By.ID,"Password").send_keys("admin")
driver.find_element(By.XPATH,"//button[@type='submit']").submit()
print("Login successfully")