import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TestPractice:
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        yield
        driver.close()
        driver.quit()
    def test_fb(self,test_setup):
        driver.get("https://www.facebook.com/signup")
        url = driver.current_url
        print(url)
        driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Hari")
        driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Krishna")
        driver.find_element(By.XPATH, "//input[@name='reg_email__']").send_keys(8179216355)
        driver.find_element(By.CSS_SELECTOR, "#password_step_input").send_keys("Harikrishna141")
        time.sleep(5)
        Daydropdown = Select(driver.find_element(By.CSS_SELECTOR, "#day"))
        Daydropdown.select_by_index(1)
        Monthdropdown = Select(driver.find_element(By.CSS_SELECTOR, "#month"))
        Monthdropdown.select_by_index(1)
        Yeardropdown = Select(driver.find_element(By.CSS_SELECTOR, "#year"))
        Yeardropdown.select_by_index(10)
        driver.find_element(By.XPATH, "//input[@value='2']").click()
        driver.find_element(By.NAME, "websubmit").click()
        time.sleep(15)
        url2 = driver.current_url
        print(url2)
        if url != url2:
            print("Test is success")
        else:
            print("Test failed")



