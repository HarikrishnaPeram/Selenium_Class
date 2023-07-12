from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://amazon.in/")
driver.maximize_window()
driver.implicitly_wait(2)
list_element=driver.find_elements(By.XPATH,"(//img)|(//div[@type='image'])")
l=len((list_element))
print(l)
vcount=0
ivcount=0
for i in (list_element):
    if(i.is_displayed()):
        vcount+=1
    else:
        ivcount+=1
print("Visible no.of images",vcount)
print("Invisible no.of images",ivcount)