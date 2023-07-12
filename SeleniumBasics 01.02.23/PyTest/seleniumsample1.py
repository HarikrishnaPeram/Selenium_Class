import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


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
        print("Test completed")


    def test_login(self,test_setUp):
        driver.get("https://practice.automationtesting.in/my-account/")

        driver.find_element(By.ID, "username").send_keys("Admin")
        driver.find_element(By.ID, "password").send_keys("admin123")
        driver.find_element(By.NAME, "login").click()