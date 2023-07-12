import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://skptricks.github.io/learncoding/selenium-demo/login%20registration%20page/Register.html")
driver.maximize_window()
driver.implicitly_wait(3)
ele= driver.find_element(By.CSS_SELECTOR,"input.username").send_keys("Selenium")
driver.find_element(By.CSS_SELECTOR,"input.emailid").send_keys("Hari")
driver.find_element(By.CSS_SELECTOR,"input.password").send_keys("Harikrishna123")
driver.find_element(By.CSS_SELECTOR,"input.button.style1.style2").click()
print("Test completed")
time.sleep(4)
driver.quit()