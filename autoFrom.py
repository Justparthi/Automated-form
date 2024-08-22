from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

end_pt = "http://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Chrome(options=options)
driver.get(end_pt)

fname = driver.find_element(By.NAME, value="fName")
lname = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
btn = driver.find_element(By.CLASS_NAME, value="btn")

fname.send_keys("Test1")
lname.send_keys("Test2")
email.send_keys("test@email.com")
btn.click()



# driver.close()