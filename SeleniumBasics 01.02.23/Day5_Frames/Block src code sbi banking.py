from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://retail.onlinesbi.sbi/retail/login.htm")
driver.maximize_window()
driver.implicitly_wait(5)
#get the source code for  page  we are not allowed to inpect click at that time     we have to use page source
#str=driver.page_source
#print(str)
driver.find_element(By.LINK_TEXT,"CONTINUE TO LOGIN").click()
driver.implicitly_wait(2)
driver.find_element(By.ID,"username").send_keys("Harikrishna")
driver.find_element(By.NAME,"password").send_keys("I dont know")
print("Successfully completed")
driver.close()