import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://regqc.sifyitest.com/pmcfeb23/reg_details.php?q=MTU4YzAzMWY3YmM5MTBmYWI3ZGFkNGUwMTAyYzg1N2N8MjczMDAwMDE5")

driver.implicitly_wait(20)
validate_your_details=driver.find_element(By.ID,"Recheck")
validate_your_details.click()

Cerebral=driver.find_element(By.XPATH,"//input[@id='disabilitysuffersoc1']")
Cerebral.click()
Cerebral_Time=driver.find_element(By.XPATH,"(//input[@id='compensatory'])[1]")
Cerebral_Time.click()
Dominant_Hand=driver.find_element(By.XPATH,"(//input[@id='optscribe'])[1]")
Dominant_Hand.click()
Dominant_Hand_Time=driver.find_element(By.XPATH,"(//input[@id='compensatory1'])[1]")
Dominant_Hand_Time.click()
Scribe=driver.find_element(By.XPATH,"(//input[@id='optscribe'])[1]")
Scribe.click()
Save_and_Next=driver.find_element(By.CSS_SELECTOR,"#FinalSubmit")
Save_and_Next.click()
time.sleep(5)
Back=driver.find_element(By.CSS_SELECTOR,"a[type='button']")
Back.click()
