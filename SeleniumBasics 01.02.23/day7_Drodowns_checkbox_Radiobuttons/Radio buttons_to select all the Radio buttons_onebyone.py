import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_radio")
driver.maximize_window()
driver.implicitly_wait(2)
driver.switch_to.frame("iframeResult")
radiobuttonlist=driver.find_elements(By.XPATH,"//input[@name='fav_language']")
size=len(radiobuttonlist)
print("seize of the list" + str(size))
time.sleep(5)
for i in radiobuttonlist:
    if i.is_selected():
        print("radio button is select")
    else:
        i.click()
        time.sleep(2)
        print("select radio button")