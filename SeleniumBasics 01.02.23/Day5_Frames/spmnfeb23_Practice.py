import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://regqc.sifyitest.com/spmnfeb23/reg_details.php?q=NzYwMTA0MWYyZmRlZTRmOGEyMTI0YmU3MGI1YTA4ZGR8MjY1MDAwMDM1")
driver.maximize_window()
Validate_details=driver.find_element(By.CSS_SELECTOR,"input[class='blue_button btn_mb_view'][value='Validate your details']")
Validate_details.click()
Post_Dropdown=Select(driver.find_element(By.CSS_SELECTOR,"select[id='selpost']"))
Post_Dropdown.select_by_index(2)
Category=driver.find_element(By.CSS_SELECTOR,"input[value='UR'][id='opt_cat']").click()
Alert=driver.switch_to.alert
text=Alert.text
print(text)
Alert.accept()
Applied_category=driver.find_element(By.CSS_SELECTOR,"input[value='UR'][id='apply_category']")
Applied_category.click()
Disability_40=driver.find_element(By.CSS_SELECTOR,"input[value='Y'][id='optdisability']").click()
Religion_Dropdown=Select(driver.find_element(By.CSS_SELECTOR,"select[id='religion']"))
Religion_Dropdown.select_by_index(1)
Minority=driver.find_element(By.CSS_SELECTOR,"input[value='Y'][id='optminority']").click()
Women=driver.find_element(By.CSS_SELECTOR,"input[value='Y'][id='relax_remarried']").click()
Spmcil_employee=driver.find_element(By.CSS_SELECTOR,"input[value='Y'][id='inservice_spmcil']").click()
Spmcil_candidate=driver.find_element(By.CSS_SELECTOR,"input[value='Y'][id='internal_cand_spmcil']").click()
Centre_Examination_Dropdown=Select(driver.find_element(By.CSS_SELECTOR,"select[id='selexamcentre']"))
Centre_Examination_Dropdown.select_by_index(1)
Day=Select(driver.find_element(By.CSS_SELECTOR,"select[id='seldobday']"))
Day.select_by_index(1)
Month=Select(driver.find_element(By.CSS_SELECTOR,"select[id='seldobmon']"))
Month.select_by_index(1)
time.sleep(2)

Year=Select(driver.find_element(By.CSS_SELECTOR,"select[id='seldobyear']"))
Year.select_by_index(1)
time.sleep(5)
Alert_DOB=driver.switch_to.alert
Alert_DOB.accept()
Corr_State=Select(driver.find_element(By.CSS_SELECTOR,"select[id='txtstate']"))
Centre_Examination_Dropdown.select_by_index(2)
time.sleep(7)
Checkbox_same_Address=driver.find_element(By.XPATH,"//input[@id='same_presentadd']")
#Checkbox_same_Address.click()
a=ActionChains(driver)
a.double_click(Checkbox_same_Address).perform()

GST=Select(driver.find_element(By.CSS_SELECTOR,"select[id='gstState']"))
GST.select_by_index(1)
Save_and_Next=driver.find_element(By.XPATH,"//input[@id='FinalSubmit']")
Save_and_Next.click()
time.sleep(10)
edu=driver.current_url
print(edu)
if edu=="https://regqc.sifyitest.com/spmnfeb23/edu_details.php?q=NzYwMTA0MWYyZmRlZTRmOGEyMTI0YmU3MGI1YTA4ZGR8MjY1MDAwMDM1":
    print("Validation successful")
else:
    print(" Validation Failed")

time.sleep(10)
Back=driver.find_element(By.CSS_SELECTOR,"a[class='blue_button3']")
Back.click()
reg_url=driver.current_url
print(reg_url)
if reg_url=="https://regqc.sifyitest.com/spmnfeb23/reg_details.php?q=NzYwMTA0MWYyZmRlZTRmOGEyMTI0YmU3MGI1YTA4ZGR8MjY1MDAwMDM1":
    print("Validation successful")
else:
    print(" Validation Failed")
time.sleep(5)

#Validate_details.click()
#PWD FIELDS IN SPMNFEB23 Application
compensatory=driver.find_element(By.XPATH,"//input[@id='compensatory2'][1]")
cerebral=driver.find_element(By.XPATH,"//input[@id='disabilitysuffersoc1'][1]")
cerebral_compensation_time=driver.find_element(By.XPATH,"//input[@id='compensatory'][1]")
dominant_hand=driver.find_element(By.XPATH,"//input[@id='compensatary_time1'][1]")
dominant_hand_compensation_time=driver.find_element(By.XPATH,"//input[@id='compensatory1'][1]")
scribe=driver.find_element(By.XPATH,"//input[@id='optscribe'][1]")
if compensatory.is_displayed():
    print("compensatory Not enabled no issue")
else:
    print("compensatory Enabled is an issue")
if cerebral.is_displayed():
    print("cerebral Not enabled no issue")
else:
    print("cerebral Enabled is an issue")
if cerebral_compensation_time.is_displayed():
    print("cerebral_compensation_time Not enabled no issue")
else:
    print("cerebral_compensation_time Enabled is an issue")
if dominant_hand.is_displayed():
    print("dominant_hand Not enabled no issue")
else:
    print("dominant_hand Enabled is an issue")
if dominant_hand_compensation_time.is_displayed():
    print("dominant_hand_compensation_time Not enabled no issue")
else:
    print("dominant_hand_compensation_time Enabled is an issue")
if scribe.is_displayed():
    print("scribe Not enabled no issue")
else:
    print("scribe Enabled is an issue")

disability_Category_dropdown=Select(driver.find_element(By.XPATH,"//select[@id='disability_category']"))
a=disability_Category_dropdown.select_by_visible_text("a")

