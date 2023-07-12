import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


#Browser initiation
class Testsample:
    @pytest.fixture()
    def test_setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
#To hit url and Basic info page.
    def test_ubimesapr23(self,test_setUp):
        """driver.get("https://regqc.sifyitest.com/ubimesapr23")
        driver.find_element(By.ID,"reg_click_here").click()
        driver.find_element(By.ID,"fullname").send_keys("KK")
        driver.find_element(By.ID,"cfullname").send_keys("KK")
        driver.find_element(By.ID,"txtmobile").send_keys("9876543211")
        driver.find_element(By.ID,"txtcmobile").send_keys("9876543211")
        driver.find_element(By.ID,"txtemail").send_keys("check")
        dropdown=Select(driver.find_element(By.XPATH,"//select[@id='seldomain']"))
        dropdown.select_by_index(2)
        driver.find_element(By.ID,"txtcemail").send_keys("check@gmail.com")
        time.sleep(5)
        driver.find_element(By.ID,"FinalSubmit").click()
        time.sleep(10)
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(10)
        #alert.dismiss()
# Photo signature page
        driver.find_element(By.XPATH,"//input[@id='picture']").send_keys("D:\Hari\Images\Krishna.jpg")
        time.sleep(10)
        driver.find_element(By.XPATH,"//input[@id='signature']").send_keys("D:\Hari\Images\kumar_sign.jpg")
        time.sleep(10)
        driver.find_element(By.XPATH,"//input[@id='confirmPhoto']").click()
        driver.find_element(By.XPATH,"//input[@id='confirmSign']").click()
        driver.find_element(By.XPATH,"//input[@id='Submit']").click()"""

#Basic details
        """driver.get("https://regqc.sifyitest.com/ubimesapr23/reg_details.php?q=OWUwZDI5YjJiNjk1MGVkMGU0MzdjM2U1Yzk1ZmY0NGZ8MjkzMDAwMDM2")
        driver.find_element(By.ID,"Recheck").click()
        Category=driver.find_element(By.XPATH," (// input[@ id='opt_cat'])[1]").click()
        time.sleep(5)
        alert1=driver.switch_to.alert
        text=alert1.text
        print(text)
        alert1.accept()
        Disability=driver.find_element(By.CSS_SELECTOR,"input[value='N'][name='optdisability']").click()
        Religion=Select(driver.find_element(By.XPATH,"//select[@id='religion']"))
        Religion.select_by_index(2)
        Nationality=Select(driver.find_element(By.ID,"txtnationality"))
        Nationality.select_by_index(1)

        Centre=Select(driver.find_element(By.XPATH,"//select[@id='selexamcentre1']"))
        Centre.select_by_index(1)
        Day=Select(driver.find_element(By.XPATH,"//select[@id='seldobday']"))
        Day.select_by_index(1)
        Month=Select(driver.find_element(By.XPATH,"//select[@id='seldobmon']"))
        Month.select_by_index(1)
        year=Select(driver.find_element(By.XPATH,"//select[@id='seldobyear']"))
        year.select_by_index(1)
        driver.find_element(By.XPATH,"(//input[@id='optsex'])[2]").click()
        driver.find_element(By.ID,"twinbrosis").click()
        driver.find_element(By.XPATH,"(//input[@id='twinbrosis'])[2]").click()
        driver.find_element(By.XPATH,"(//input[@value='Unmarried'])").click()
        driver.find_element(By.ID,"fatherfirstname").send_keys("hh")
        driver.find_element(By.ID,"motherfirstname").send_keys("hh")
        driver.find_element(By.ID, "txtaddress1").send_keys("hh")
        driver.find_element(By.ID, "txtdistrict").send_keys("hh")
        State=Select(driver.find_element(By.ID,"txtstate"))
        State.select_by_index(2)
        driver.find_element(By.ID,"txtpin").send_keys("524444")
        driver.find_element(By.ID,"same_presentadd").click()
        Gst=Select(driver.find_element(By.XPATH,"//select[@id='gstState']"))
        Gst.select_by_index(1)
        BasicdetailsSaveandedit=driver.find_element(By.ID,"FinalSubmit")
        BasicdetailsSaveandedit.click()"""

#Edu Page
        driver.get("https://regqc.sifyitest.com/ubimesapr23//edu_details.php?q=YzNkNmNmYWVjMGIyMTdkMzdkNzhhMGY3NjBhM2Y4YWR8MjkzMDAwMDI5")
        EDUvalidate=driver.find_element(By.XPATH,"//input[@id='Recheck']")
        EDUvalidate.click()
        time.sleep(10)
#XII
        XIIDropdown=Select(driver.find_element(By.XPATH,"//select[@id='selstream2']"))
        XIIDropdown.select_by_index(1)
        driver.find_element(By.XPATH,"//input[@id='seluniv2']").send_keys("kkk")
        Day1 = Select(driver.find_element(By.XPATH, "//select[@id='selday2']"))
        Day1.select_by_index(1)
        Month1 = Select(driver.find_element(By.XPATH, "//select[@id='selmonth2']"))
        Month1.select_by_index(1)
        year1 = Select(driver.find_element(By.XPATH, "//select[@id='selyr2']"))
        year1.select_by_index(1)
        driver.find_element(By.ID,"selmark2").send_keys("88")
        Grade1 = Select(driver.find_element(By.XPATH, "//select[@id='selgrade2']"))
        Grade1.select_by_index(1)
        time.sleep(5)
#graduation
        Graduation = Select(driver.find_element(By.XPATH, "//select[@id='selstream3']"))
        Graduation.select_by_index(5)
        driver.find_element(By.ID,"seluniv3").send_keys("hh")
        Day2 = Select(driver.find_element(By.XPATH, "//select[@id='selday3']"))
        Day2.select_by_index(1)
        Month2 = Select(driver.find_element(By.XPATH, "//select[@id='selmonth3']"))
        Month2.select_by_index(1)
        year2 = Select(driver.find_element(By.XPATH, "//select[@id='selyr3']"))
        year2.select_by_index(1)
        driver.find_element(By.ID,"selmark3").send_keys(8)
        Grade2 = Select(driver.find_element(By.XPATH, "//select[@id='selgrade3']"))
        Grade2.select_by_index(1)
        time.sleep(5)
#Extra fields
        driver.find_element(By.CSS_SELECTOR,"input[id='sports_achieve'][value='Y']").click()
        time.sleep(5)
#Sports
        driver.find_element(By.CSS_SELECTOR,"input[id='country_represent_competition'][value='Y']").click()
        driver.find_element(By.CSS_SELECTOR,"input[id='state_represent_competition'][value='Y']").click()
        driver.find_element(By.CSS_SELECTOR,"input[id='district_represent_competition'][value='Y']").click()
        driver.find_element(By.CSS_SELECTOR,"input[id='interuniv_represent_competition'][value='Y']").click()
        driver.find_element(By.CSS_SELECTOR,"input[id='schoolteam_represent_competition'][value='Y']").click()
        driver.find_element(By.CSS_SELECTOR,"input[id='national_awards_physical'][value='Y']").click()
        driver.find_element(By.CSS_SELECTOR,"input[id='active_sportsperson'][value='Y']").click()
        driver.find_element(By.CSS_SELECTOR,"input[id='certificates_relating_efficiency'][value='Y']").click()
#Sports Qualification Details
        driver.find_element(By.ID,"tournament_name1").send_keys("hhh")
        driver.find_element(By.ID, "tournament_venue1").send_keys("hhh")
        TorDay2 = Select(driver.find_element(By.XPATH, "//select[@id='tournament_day1']"))
        TorDay2.select_by_index(1)
        TorMonth2 = Select(driver.find_element(By.XPATH, "//select[@id='tournament_month1']"))
        TorMonth2.select_by_index(1)
        Toryear2 = Select(driver.find_element(By.XPATH, "//select[@id='tournament_year1']"))
        Toryear2.select_by_index(6)
        driver.find_element(By.ID,"tournament_performance1").send_keys("Jllllllllllllllllllllllllllllllllllllllp")
        driver.find_element(By.ID,"tournament_achievements1").send_keys("Lllllllllalllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllp")
#Languages
        driver.find_element(By.ID,"txtlang1").send_keys("Hh")
        Read=driver.find_element(By.ID,"lang1r")
        Read.click()
        driver.find_element(By.ID, "txtlang1").send_keys("Hh")
        Write = driver.find_element(By.ID, "lang1w")
        Write.click()
        driver.find_element(By.ID, "txtlang1").send_keys("Hh")
        Speak = driver.find_element(By.ID, "lang1s")
        Speak.click()
        EDUvalidate.click()
        time.sleep(10)
        EDUSaveandnext=driver.find_element(By.NAME,"FinalSubmit").click()
        time.sleep(10)






