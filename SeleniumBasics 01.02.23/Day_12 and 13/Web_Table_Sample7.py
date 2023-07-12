from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///C:/Users/sds01798/Downloads/Table_3.html")
driver.maximize_window()
driver.implicitly_wait(5)
#To identify the column value in 3
text=driver.find_elements(By.XPATH,"//*[@name='BookTable']/tbody/tr/td[3]")
for i in text:
    print(i.text)
driver.quit()