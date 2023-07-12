from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///C:/Users/sds01798/Downloads/Table_3.html")
driver.maximize_window()
driver.implicitly_wait(5)
#Get all the Headers
list_header=driver.find_elements(By.XPATH,"//tr//th")
l=len(list_header)
print(l)
for element in list_header:
    print(element.text)
driver.quit()

