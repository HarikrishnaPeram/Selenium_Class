from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox")
driver.maximize_window()
driver.implicitly_wait(2)
#select
driver.switch_to.frame("iframeResult")
ele1=driver.find_element(By.ID,"vehicle1")
print("Is the option is selected"+str(ele1.is_selected()))
ele1.click()
print("Is the option is selected"+str(ele1.is_selected()))