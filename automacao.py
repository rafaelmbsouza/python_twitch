from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:/Windows/chromedriver.exe")
time.sleep(5)

driver.get("https://gmail.com")
caixa_login = driver.find_element_by_id("identifierId")
print(caixa_login)

# driver.quit()