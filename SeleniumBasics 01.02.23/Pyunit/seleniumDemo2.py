import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class MyTestCases1(unittest.TestCase):
    @classmethod
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
        self.assertEqual(X,"selenium - Google Search")
    @classmethod
    def tearDown(self):
        self.driver.quit()