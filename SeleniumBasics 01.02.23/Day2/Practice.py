from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
#driver.get("https://the-internet.herokuapp.com/javascript_alerts")
#driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']").click()
#alert=driver.switch_to.alert
#text=alert.text
#time.sleep(2)
#print("The text is",text)
#if text=="I am a JS Alert":
 #   print("Successfully executed")
#else:
 #   print("Failed ")

#alert.accept()
#driver.close()

#driver.get("https://the-internet.herokuapp.com/javascript_alerts")
#driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']").click()
#alert=driver.switch_to.alert
#text=alert.text
#assert text=="I am a JS Confirm"

#print("the text is" ,text)

#alert.accept()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
alert=driver.switch_to.alert
text=alert.text
alert.send_keys("Harikrishna")
alert.accept()
text_message=driver.find_element(By.XPATH,"//*[@id='result']").text
print(text_message)
if text_message=="You entered: Harikrishna":
    print("Matched")
else:
    print("Not matched")


print("Successfully completed")