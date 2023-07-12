import pytest
from selenium import webdriver

#pytest = [pytest.mark.frantend, pytest.mark.slow]


@pytest.mark.smoke
def test_reg_valid_data():
    driver=webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")

@pytest.mark.sanity
def test_login_invalid_data():
    driver=webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")

@pytest.mark.smoke
@pytest.mark.Regression
def test_invalid_data():
    driver=webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")


#py.test pytestgroups.py -m smoke -v
#Disabling warnings-->pytest--disable-warnings
#pytest -w ignore::pytest.PytestUnknownMarkWarning