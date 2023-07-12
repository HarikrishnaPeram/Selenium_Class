import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://google.co.in")
driver.maximize_window()
driver.implicitly_wait(2)
#scroll down
e1=driver.find_element(By.NAME,"q")
driver.execute_script("arguments[0].setAttribute('disabled','true');",e1)
time.sleep(5)
driver.execute_script("arguments[0].removeAttribute('disabled','true');",e1)
time.sleep(10)
