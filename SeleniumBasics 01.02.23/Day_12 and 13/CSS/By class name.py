from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://skptricks.github.io/learncoding/selenium-demo/login%20registration%20page/Register.html")
driver.maximize_window()
driver.implicitly_wait(3)
driver.find_element(By.CSS_SELECTOR,"input.username").send_keys("Hari")
driver.find_element(By.CSS_SELECTOR,"input.emailid").send_keys("Hari@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input.password").send_keys("Harikrishna123")
driver.close()


print("Test completed")