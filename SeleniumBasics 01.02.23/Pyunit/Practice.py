import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Practicesession(unittest.TestCase):


    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def test_Pracice1_FBSIGNUP(self):
        self.driver.get("https://www.facebook.com/signup")
        url=self.driver.current_url
        print(url)
        self.driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Hari")
        self.driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Krishna")
        self.driver.find_element(By.XPATH, "//input[@name='reg_email__']").send_keys(8179216355)
        self.driver.find_element(By.CSS_SELECTOR, "#password_step_input").send_keys("Harikrishna141")
        Daydropdown = Select(self.driver.find_element(By.CSS_SELECTOR, "#day"))
        Daydropdown.select_by_index(1)
        Monthdropdown = Select(self.driver.find_element(By.CSS_SELECTOR, "#month"))
        Monthdropdown.select_by_index(1)
        Yeardropdown = Select(self.driver.find_element(By.CSS_SELECTOR, "#year"))
        Yeardropdown.select_by_index(10)
        self.driver.find_element(By.XPATH, "//input[@value='2']").click()
        self.driver.find_element(By.NAME, "websubmit").click()
        time.sleep(15)
        url2=self.driver.current_url
        print(url2)
        if url!=url2:
            print("Test is success")
        else:
            print("Test failed")
    def tearDown(self) :
        self.driver.quit()