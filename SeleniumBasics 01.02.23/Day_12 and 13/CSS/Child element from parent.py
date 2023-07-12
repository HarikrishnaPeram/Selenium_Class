import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://skptricks.github.io/learncoding/selenium-demo/login%20registration%20page/Register.html")
driver.maximize_window()
driver.implicitly_wait(3)
ele= driver.find_element(By.CSS_SELECTOR,"form>input.username").send_keys("Selenium")
print("Test completed")
time.sleep(4)
driver.quit()