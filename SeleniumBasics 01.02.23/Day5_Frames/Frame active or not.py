from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/tinymce")
driver.maximize_window()
driver.implicitly_wait(5)
element=driver.find_element(By.ID,"mce_0_ifr")
driver.switch_to.frame(element)
e1=driver.switch_to.active_element
e1.clear()
e1.send_keys("Harikrishna")
print("Frame is active or not successfully completed ")
driver.close()