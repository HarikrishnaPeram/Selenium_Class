import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class MyTestCases(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def test_search(self):
        self.driver.get("http://google.com")
        self.driver.find_element(By.NAME, "q").send_keys("selenium")
        self.driver.find_element(By.NAME,"btnK").submit()
        X= self.driver.title
        print(X)
        self.assertEqual(X,"Google")
    def tearDown(self):
        self.driver.quit()