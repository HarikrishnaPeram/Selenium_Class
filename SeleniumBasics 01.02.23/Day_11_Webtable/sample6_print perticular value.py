from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///C:/Users/sds01798/Downloads/Table_3.html")
driver.maximize_window()
driver.implicitly_wait(5)
#Get all the column and count
text=driver.find_elements(By.XPATH,"//*[@name='BookTable']/tbody/tr[3]/td[2]")
l=len(text)
print(l)

for element in  text:
    print(element.text)
driver.quit()