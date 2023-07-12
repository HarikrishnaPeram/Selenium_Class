import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Testconfirmation:
    @pytest.fixture()
    def test_setUp(self):
        global driver
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        yield
        driver.close()
        driver.quit()

    def test_confirmation(self,test_setUp):

        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox")
               # select
        driver.switch_to.frame("iframeResult")
        ele1 = driver.find_element(By.ID, "vehicle1")
        print("Is the option is selected" + str(ele1.is_selected()))
        ele1.click()
        print("Is the option is selected" + str(ele1.is_selected()))