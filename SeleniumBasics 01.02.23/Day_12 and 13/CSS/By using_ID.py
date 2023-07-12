from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://skptricks.github.io/learncoding/selenium-demo/login%20registration%20page/Register.html")
driver.maximize_window()
driver.implicitly_wait(3)
driver.find_element(By.CSS_SELECTOR,"input#regUsername").send_keys("Hari")
driver.find_element(By.CSS_SELECTOR,"input#regEmail").send_keys("Hari@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input#regPassword").send_keys("Harikrishna123")
driver.close()


print("Test completed")