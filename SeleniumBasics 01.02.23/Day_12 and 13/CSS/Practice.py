import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp")
driver.maximize_window()
driver.implicitly_wait(10)
#Create account page
First_name=(driver.find_element(By.ID,"firstName").send_keys("Hari"))
Last_Name=driver.find_element(By.ID,"lastName").send_keys("Krishna")
User_name=driver.find_element(By.ID,"username").send_keys("Ha93939123")
Password=driver.find_element(By.CSS_SELECTOR,"input[name='Passwd']").send_keys("Hari199999@")
Con_Password=driver.find_element(By.CSS_SELECTOR,"input[name='ConfirmPasswd']").send_keys("Hari199999@")
show_password=driver.find_element(By.CLASS_NAME,"VfPpkd-muHVFf-bMcfAe").click()
Next_button=driver.find_element(By.XPATH,"(//span[@class='VfPpkd-vQzf8d'])[2]").click()
time.sleep(15)
#basic details
Phone=driver.find_element(By.XPATH,"//input[@id='phoneNumberId']").send_keys("9876543210")
time.sleep(10)


Day=driver.find_element(By.XPATH,"//input[@id='day']").send_keys("01")
"""
Month=Select(driver.find_element(By.ID,"month"))
Month.select_by_index(1)
year=driver.find_element(By.ID,"year").send_keys(1995)
Gender=Select(driver.find_element(By.XPATH,"//label[@id='gender-label']"))
Gender.select_by_index(1)
Next=driver.find_element(By.XPATH,"(//div[@class='VfPpkd-RLmnJb'])[1]").click()


print("Testing completed")"""