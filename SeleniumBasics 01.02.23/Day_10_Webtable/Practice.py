from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///C:/Users/sds01798/Downloads/Table_2.html")
driver.maximize_window()
driver.implicitly_wait(5)
text=driver.find_element(By.XPATH,"//td[text()='Selenium']").text
print(text)

#for multiple text
list_text=driver.find_elements(By.XPATH,"//tr//td")
l=len(list_text)
print(l)
for i in list_text:
    print(i.text)
driver.quit()