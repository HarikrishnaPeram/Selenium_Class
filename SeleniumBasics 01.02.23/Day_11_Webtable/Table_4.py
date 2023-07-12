from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///C:/Users/sds01798/Downloads/Table_3.html")
driver.maximize_window()
driver.implicitly_wait(5)
#Get all the Headers
list_row=driver.find_elements(By.XPATH,"//*[@name='BookTable']/tbody/tr")
l=len(list_row)
print(l)



for element in  list_row:
    print(element.text)
driver.quit()