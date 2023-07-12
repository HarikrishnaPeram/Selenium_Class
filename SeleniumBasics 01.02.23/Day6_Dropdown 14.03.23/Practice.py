print("Drop down counts")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver=webdriver.Chrome()
driver.get("https://regqc.sifyitest.com/spmnfeb23/reg_details.php?q=YjAwN2Q5ZDMwMzQwOGVmODRjZDBkMmI1ZmEzNTNlNTF8MjY1MDAwMDM3")
driver.maximize_window()
driver.implicitly_wait(2)
list_dropdowns=driver.find_elements(By.TAG_NAME,"select")
l=len(list_dropdowns)
print(l)
vdrp=0
indrp=0
for i in list_dropdowns:
    if i.is_displayed():
        vdrp+=1
    else:
        indrp+=1
print("Visible dropdown",vdrp)
print("Invisible",indrp)

print("Retrive data from the Dropdown values")
Religion=(driver.find_element(By.XPATH,"//select[@id='religion']"))
Religions=Select(Religion)
Religions.select_by_value("Christian")
print(Religions.first_selected_option.text)
for i in Religions.options:
    print(i.text)


#time.sleep(2)
#is it multiple or not
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)
speed=driver.find_element(By.ID,"speed")
sel_speed=Select(speed)
sel_speed.select_by_visible_text("Medium")
if (sel_speed.is_multiple):
    print("This is multiple select")
else:
    print("This is not multiple select")
sel_speed.first_selected_option
print(sel_speed.first_selected_option.text)
for i in sel_speed.options:
       print(i.text)

file=driver.find_element(By.XPATH,"//select[@id='files']")
files=Select(file)
files.select_by_value("1")
print(files.first_selected_option.text)
if files.first_selected_option.text=="TXT file":
    print("Select value is TXT FILE")
else:
    print("Selected value is not TXT File")
for i in files.options:
    print(i.text)
animal=driver.find_element(By.ID,"animals")
animals=Select(animal)
animals.select_by_value("cat")
print(animals.first_selected_option.text)
if animals == "Cat":
    print("Selected value is cat")
else:
    print("selected value is not cat")
for i in animals.options:
    print(i.text)



import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select_multiple")
driver.maximize_window()
driver.implicitly_wait(2)
#select
driver.switch_to.frame("iframeResult")
car=driver.find_element(By.ID,"cars")
cars=Select(car)
action=ActionChains(driver)
action.key_down(keys.Keys.CONTROL).perform()
time.sleep(5)
action.click(cars.select_by_value("volvo"))
time.sleep(5)
action.click(cars.select_by_value("saab"))
time.sleep(4)
action.click(cars.select_by_value("opel"))
time.sleep(5)
#deselect
action.key_up(keys.Keys.CONTROL).perform()
cars.deselect_all()
#print(cars.first_selected_option.text)














