from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///C:/Users/sds01798/Downloads/Table_3.html")
driver.maximize_window()
driver.implicitly_wait(5)
#To identify the column values in 3
m=driver.find_elements(By.XPATH,"//td[text()='Mukesh']")
s=len(m)
print(s)
#Check if list seize greater than 0
if s>0:
    print("Text found")
driver.quit()