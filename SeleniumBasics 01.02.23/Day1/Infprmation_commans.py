from selenium import webdriver

#get (To lunch the url in the browser )
#title (to print title of the page)
#current_url (Print current url)
#page_source (Print all code which are present in the url)

driver=webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
title=driver.title
print(title)
url=driver.current_url
print(url)
ps=driver.page_source
print(ps)