import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.easemytrip.com/")
driver.maximize_window()
time.sleep(5)
ele1=driver.find_element(By.XPATH,"//p[text()='Book a round trip']")
ele1.click()
#To select current date
ele2=driver.find_elements(By.XPATH,"//div[@class='box']//following::ul//li")
for td in ele2:
    if "active-date" in td.get_attribute("class"):
        td.click()
        break
        time.sleep(5)