from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///C:/Users/sds01798/Downloads/Hyper Text Mark Up Language1.html")
driver.maximize_window()
driver.implicitly_wait(5)
text1=driver.find_element(By.XPATH,"//td[text()='Maths']").text
print(text1)
driver.quit()