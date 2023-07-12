import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import XLUtils

driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
#Age Validation
driver.get("https://regqc.sifyitest.com/ubimesapr23")
path= "C://Users//sds01798//Downloads//PracticeDDT.xlsx"
rows=XLUtils.getRowCount(path,'Sheet1')
for r in range(2,rows+1):
    Desc= XLUtils.readData(path,"Sheet1",r,2)
    category= XLUtils.readData(path,"Sheet1",r,4)
    PWD=XLUtils.readData(path,"Sheet1",r,6)
    Religion=XLUtils.readData(path,"Sheet1",r,13)
    centre=XLUtils.readData(path,"Sheet1",r,14)
   # MAXDOB=XLUtils.readData(path,"Sheet1",r,15)
    #MINDOB=XLUtils.readData(path,"Sheet1",r,16)
    #Date_asondate=XLUtils.readData(path,"Sheet1",r,17)
    MaxAgeminus1=XLUtils.readData(path,"Sheet1",r,21)
    MaxAgE=XLUtils.readData(path,"Sheet1",r,22)
    MaxAgePlus1=XLUtils.readData(path,"Sheet1",r,23)
    MinAge1=XLUtils.readData(path,"Sheet1",r,24)
    MinAge=XLUtils.readData(path,"Sheet1",r,25)
    MinAgePlus1=XLUtils.readData(path,"Sheet1",r,26)
    MaxAgePlus28=XLUtils.readData(path,"Sheet1",r,27)
    MinAge28=XLUtils.readData(path,"Sheet1",r,28)
    Payamount=XLUtils.readData(path,"Sheet1",r,32)

    driver.find_element(By.ID, "reg_click_here").click()
    driver.find_element(By.ID, "fullname").send_keys("KK")
    driver.find_element(By.ID, "cfullname").send_keys("KK")
    driver.find_element(By.ID, "txtmobile").send_keys("9876543211")
    driver.find_element(By.ID, "txtcmobile").send_keys("9876543211")
    driver.find_element(By.ID, "txtemail").send_keys("check")
    dropdown = Select(driver.find_element(By.XPATH, "//select[@id='seldomain']"))
    dropdown.select_by_index(2)
    driver.find_element(By.ID, "txtcemail").send_keys("check@gmail.com")
    time.sleep(5)
    driver.find_element(By.ID, "FinalSubmit").click()
    time.sleep(10)
    alert = driver.switch_to.alert
    time.sleep(2)
    alert.accept()
    time.sleep(10)
    # alert.dismiss()
    # Photo signature page
    driver.find_element(By.XPATH, "//input[@id='picture']").send_keys("D:\Hari\Images\Krishna.jpg")
    time.sleep(10)
    driver.find_element(By.XPATH, "//input[@id='signature']").send_keys("D:\Hari\Images\kumar_sign.jpg")
    time.sleep(10)
    driver.find_element(By.XPATH, "//input[@id='confirmPhoto']").click()
    driver.find_element(By.XPATH, "//input[@id='confirmSign']").click()
    driver.find_element(By.XPATH, "//input[@id='Submit']").click()

    # Basic details

    driver.find_element(By.ID, "Recheck").click()
    time.sleep(5)
    #driver.switch_to.alert.accept()
    Category = driver.find_element(By.XPATH, " (// input[@ id='opt_cat'])[5]").click()
    time.sleep(10)
    alert1 = driver.switch_to.alert
    text = alert1.text
    print(text)
    alert1.accept()
    #Disability.clear()
    Disability = driver.find_element(By.XPATH, "(//input[@name='optdisability'])[2]").click()
    Religion = Select(driver.find_element(By.XPATH, "//select[@id='religion']"))
    Religion.select_by_index(2)
    Centre = Select(driver.find_element(By.XPATH, "//select[@id='selexamcentre1']"))
    Centre.select_by_index(1)
    Day = Select(driver.find_element(By.XPATH, "//select[@id='seldobday']"))
    Day.select_by_value("02")
    Month = Select(driver.find_element(By.XPATH, "//select[@id='seldobmon']"))
    Month.select_by_value("04")
    year = Select(driver.find_element(By.XPATH, "//select[@id='seldobyear']"))
    year.select_by_value("1995")


    driver.find_element(By.XPATH,"(//input[@id='optsex'])[2]").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "input[value='N'][name='twinbrosis']").click()
    driver.find_element(By.XPATH, "(//input[@value='Unmarried'])").click()
    driver.find_element(By.ID, "fatherfirstname").send_keys("hh")
    driver.find_element(By.ID, "motherfirstname").send_keys("hh")
    driver.find_element(By.ID, "txtaddress1").send_keys("hh")
    driver.find_element(By.ID, "txtdistrict").send_keys("hh")
    State = Select(driver.find_element(By.ID, "txtstate"))
    State.select_by_index(2)
    driver.find_element(By.ID, "txtpin").send_keys("524444")
    driver.find_element(By.ID, "same_presentadd").click()
    Gst = Select(driver.find_element(By.XPATH, "//select[@id='gstState']"))
    Gst.select_by_index(1)
    driver.find_element(By.ID,"FinalSubmit").click()
    driver.quit()





