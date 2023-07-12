from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
if(driver.title=="The Internet"):
    print("The test is paased")
else:
    print("The test is failed")