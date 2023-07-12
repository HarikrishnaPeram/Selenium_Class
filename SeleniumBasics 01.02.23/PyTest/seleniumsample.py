from selenium import webdriver
from selenium.webdriver.common.by import By


def test_setUp():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()

def test_login():
    driver.get("https://practice.automationtesting.in/my-account/")

    driver.find_element(By.ID,"username").send_keys("Admin")
    driver.find_element(By.ID,"password").send_keys("admin123")
    driver.find_element(By.NAME,"login").click()


def test_teardown():
    driver.close()
    driver.quit()