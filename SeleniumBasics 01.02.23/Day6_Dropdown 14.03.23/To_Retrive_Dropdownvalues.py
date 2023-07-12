from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(2)
speed=driver.find_element(By.ID,"speed")
sel_speed=Select(speed)
sel_speed.select_by_index("2")
sel_speed.first_selected_option
print(sel_speed.first_selected_option.text)
for i in sel_speed.options: # Options is a property to retrive data from the dropdown
    print(i.text)



Religion=Select(driver.find_element(By.XPATH,"//select[@id='religion']"))
