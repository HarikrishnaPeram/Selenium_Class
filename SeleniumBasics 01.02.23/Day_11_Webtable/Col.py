from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///C:/Users/sds01798/Downloads/Table_3.html")
driver.maximize_window()
driver.implicitly_wait(5)
#Get all the column and count
list_col=driver.find_elements(By.XPATH,"//*[@name='BookTable']/tbody/tr[3]")
l=len(list_col)
print(l)



for element in  list_col:
    print(element.text)
driver.quit()