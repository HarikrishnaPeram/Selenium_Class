from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///C:/Users/sds01798/Downloads/Table_3.html")
driver.maximize_window()
driver.implicitly_wait(5)
#To identify the table row
r=driver.find_elements(By.XPATH,"//*[@name='BookTable']/tbody/tr")
#To identify the  table column
c=driver.find_elements(By.XPATH,"//*[@name='BookTable']/tbody/tr[3]/td")
#To get rows counts with len method
rc=len(r)
print(rc)

#To get column counts with len method
cc=len(c)
print(cc)


#To traverse through the table row excilding header
for i in range(2,rc+1):
    for j in range(1,cc+1):
        d= driver.find_element(By.XPATH,"//tr["+str(i)+"]/td["+str(j)+"]").text
        print(d)
driver.close()