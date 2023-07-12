from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(2)
list_dropDown=driver.find_elements(By.TAG_NAME,"select")
l=len(list_dropDown)
print(l)
vdrp=0
ivdrp=0
for i in (list_dropDown):
    if (i.is_displayed()):
        vdrp+=1
    else:
        ivdrp+=1
print("visible dorp down",vdrp)
print("visible dorp down",ivdrp)
