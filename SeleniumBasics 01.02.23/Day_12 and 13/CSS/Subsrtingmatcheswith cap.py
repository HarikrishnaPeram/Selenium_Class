from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://facebook.com")
driver.maximize_window()
driver.implicitly_wait(3)
#start with em than use^
ele=driver.find_element(By.CSS_SELECTOR,"input[id^='em']").send_keys("selenium")
print("Testcompleted")
#contains id than use*
driver.get("https://gmail.com")
ele=driver.find_element(By.CSS_SELECTOR,"input[id*='id']").send_keys("hari")
print("Testcompleted")
