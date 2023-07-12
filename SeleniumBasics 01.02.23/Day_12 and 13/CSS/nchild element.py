from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://skptricks.github.io/learncoding/selenium-demo/login%20registration%20page/Register.html")
driver.maximize_window()
driver.implicitly_wait(3)
ele=driver.find_element(By.CSS_SELECTOR,"form input:nth-of-type(1)").send_keys("Selemium")
ele=driver.find_element(By.CSS_SELECTOR,"form input:nth-of-type(2)").send_keys("Selemium")
ele=driver.find_element(By.CSS_SELECTOR,"form input:nth-of-type(3)").send_keys("Selemium")
print("Test completed")