from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://facebook.com")
driver.maximize_window()
driver.implicitly_wait(3)
ele=driver.find_element(By.CSS_SELECTOR,"input[id$='mail']").send_keys("Selenium")
print("Test completed")
driver.close()