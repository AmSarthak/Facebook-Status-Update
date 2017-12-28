from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
user = raw_input("Enter your email id: ")
password = ""
message = raw_input("Enter your status update: ")
print ("   ")
print ("Please Wait")
print ("     ")
print ("Contacting Chrome")
print ("............")
driver = wb.Chrome('C:/WebDriver/chromedriver.exe')
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(password)
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_name("xhpc_message")
elem.send_keys(message)
#elem.send_keys(Keys.RETURN)

