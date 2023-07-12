from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
Main_window=driver.current_window_handle
print(Main_window)
print(Main_window.title())
driver.find_element(By.XPATH,"//*[text()='Click Here']").click()
for window in driver.window_handles:
    if window != Main_window:
        Child_window = window

driver.switch_to.window(Child_window)
print(driver.title)
print(Child_window.title())