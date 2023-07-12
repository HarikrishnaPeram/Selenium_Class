import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://regqc.sifyitest.com/spmnfeb23/reg_details.php?q=NzYwMTA0MWYyZmRlZTRmOGEyMTI0YmU3MGI1YTA4ZGR8MjY1MDAwMDM1")
driver.maximize_window()

Validate_details=driver.find_element(By.CSS_SELECTOR,"input[class='blue_button btn_mb_view'][value='Validate your details']")
Validate_details.click()
time.sleep(5)
Post_Dropdown=Select(driver.find_element(By.XPATH,"//select[@id='selpost']"))
Post_Dropdown.select_by_visible_text("Junior Hindi Translator")
"""Category=driver.find_element(By.CSS_SELECTOR,"input[value='UR'][id='opt_cat']").click()
Alert=driver.switch_to.alert
text=Alert.text
print(text)
Alert.accept()
Applied_category=driver.find_element(By.CSS_SELECTOR,"input[value='UR'][id='apply_category']")
Applied_category.click() """