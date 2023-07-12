import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
main_win=driver.current_window_handle
print(main_win)
print(main_win.title())
print(driver.title)
time.sleep(5)
#click on the link
driver.find_element(By.XPATH,"//*[@id='content']/div/a").click()
for window in driver.window_handles:
    if window!=main_win:
        child_win=window
#change the control to new window page
driver.switch_to.window(child_win)
print(child_win.title())
time.sleep(4)
s=driver.find_element(By.XPATH,"//h3[text()='New Window']").text
print(s)
driver.close()
driver.quit()