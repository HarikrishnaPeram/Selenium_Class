import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select_multiple")
driver.maximize_window()
driver.implicitly_wait(2)
#select
driver.switch_to.frame("iframeResult")
ele_cars=driver.find_element(By.ID,"cars")
select=Select(ele_cars)
actions=ActionChains(driver)
actions.key_down(keys.Keys.CONTROL).perform()
time.sleep(5)
actions.click(select.select_by_value("volvo"))
time.sleep(5)
actions.click(select.select_by_visible_text("Opel"))
time.sleep(5)
#deselect
actions.key_up(keys.Keys.CONTROL).perform()
select.deselect_by_value("volvo")