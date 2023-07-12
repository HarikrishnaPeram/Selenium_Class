import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

#Right click= c
driver=webdriver.Chrome()
driver.get("https://amazon.in/")
driver.maximize_window()
driver.implicitly_wait(2)
e1=driver.find_element(By.ID,"twotabsearchtextbox")
actions=ActionChains(driver)
actions.click().perform()
actions.context_click().perform()
time.sleep(5)
print("Right click")

#(//span[text()='Brands']//following::div)[1]//i
#mobil
#laptop and accesaries