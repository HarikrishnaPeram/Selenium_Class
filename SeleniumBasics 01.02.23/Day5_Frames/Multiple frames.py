#if frame multiple frames needs to captured
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("http://only-testing-blog.blogspot.com/2015/01/iframe1.html")
driver.maximize_window()
driver.implicitly_wait(5)
driver.switch_to.frame("frame1")
driver.find_element(By.XPATH,"//td[text()='Cat']//parent::tr//td//input").click()
driver.switch_to.default_content()
driver.switch_to.frame("frame2")
driver.find_element(By.NAME,"fname").send_keys("sel")
driver.implicitly_wait(5)
driver.find_element(By.ID,"check2").click()
time.sleep(10)
driver.switch_to.default_content()
print("Multiple frmes execution has been completed")
driver.close()