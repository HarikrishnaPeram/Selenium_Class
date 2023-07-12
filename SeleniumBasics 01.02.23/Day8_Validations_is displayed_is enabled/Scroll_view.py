import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://amazon.in")
driver.maximize_window()
driver.implicitly_wait(2)
#scroll down
driver.execute_script("window.scrollBy(0,1000);")
time.sleep(3)
#scroll up
driver.execute_script("window.scrollBy(0,-1000);")
time.sleep(3)
#scroll element into view

e1=driver.find_element(By.ID,"twotabsearchtextbox")
driver.execute_script("arguments[0].scrollIntoView(true);",e1)
time.sleep(3)
driver.execute_script("window.scrollBy(0,-150);")
#native way to scroll element into view
time.sleep(3)
driver.execute_script("window.scrollBy(0,-1000);")
location=e1.location_once_scrolled_into_view
print("location:"+str(location))
driver.execute_script("window.scrollBy(0,-150);")
