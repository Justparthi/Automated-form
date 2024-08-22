# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from time import sleep



# option = webdriver.ChromeOptions()
# option.add_experimental_option("detach", True)

# end_pt = "https://orteil.dashnet.org/experiments/cookie/"


# driver = webdriver.Chrome(options=option)
# driver.get(end_pt)

# cookie = driver.find_element(By.ID, value="cookie")
# cursor = driver.find_element(By.ID, value="buyCursor")
# grandma = driver.find_element(By.ID, value="buyGrandma")
# Factory = driver.find_element(By.ID, value="buyFactory")
# Mine = driver.find_element(By.ID, value="buyMine")
# shipment = driver.find_element(By.ID, value="buyShipment")
# lab = driver.find_element(By.ID, value="buyAlchemy lab")
# portal = driver.find_element(By.ID, value="buyPortal")
# timeMachine = driver.find_element(By.ID, value="buyTime machine")
# money = int(driver.find_element(By.ID, value="money").text)


# # print(money)

# def check_buy():
#     try:    
#         timeMachine.click()
#         sleep(1)        
#         print("time")
#     except Exception as e:
#         print("error")    
#     try:    
#         portal.click()
#         sleep(1)
#         print("portal")
#     except Exception as e:
#         print("error")    
#     try:    
#         lab.click()
#         sleep(1)
#         print("lab")
#     except Exception as e:
#         print("error")
#     try:        
#         shipment.click()
#         sleep(1)
#         print("ship")
#     except Exception as e:
#         print("error")
#     try:        
#         Mine.click()
#         sleep(1)
#         print("mine")
#     except Exception as e:
#         print("error")
#     try:        
#         Factory.click()
#         sleep(1)
#         print("fatory")
#     except Exception as e:
#         print("error")
#     try:    
#         grandma.click()
#         sleep(1)
#         print("grandma")
#     except Exception as e:
#         print("error")
#     try:        
#         cursor.click()
#         sleep(1)
#         print("cursor")
#     except Exception as e:
#         print("error")

        
       

# def clicker():
#     for i in range(100):
#         cookie.click()




# while True:
#     # if 1 > 0:
    
#     clicker()
#     sleep(1)
#     check_buy() 
#     sleep(1)
    

#     # money.click()
#     # print("money")
#     # timeMachine.click()
#     # print("time")
#     # portal.click()
#     # print("portal")
#     # lab.click()
#     # print("lab")
#     # shipment.click()
#     # print("ship")
#     # Mine.click()
#     # print("mine")
#     # Factory.click()
#     # print("fatory")
#     # grandma.click()
#     # print("grandma")
#     # cursor.click()
#     # print("cursor")
    
#     # money.click()
#     # timeMachine.click()
#     # portal.click()
#     # lab.click()
#     # shipment.click()
#     # Mine.click()
#     # Factory.click()
#     # grandma.click()
#     # cursor.click()    



# # print(money.text)    

# # driver.close()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep, time

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

end_pt = "https://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(options=option)
driver.get(end_pt)

cookie = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cookie")))

upgrades = [
    "buyTime machine", "buyPortal", "buyAlchemy lab", "buyShipment",
    "buyMine", "buyFactory", "buyGrandma", "buyCursor"
]

def get_money():
    money_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "money")))
    return int(money_element.text.replace(",", ""))

def check_buy():
    money = get_money()
    print(f"Current money: {money}")
    
    for upgrade in upgrades:
        try:
            upgrade_element = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.ID, upgrade))
            )
            if "grayed" not in upgrade_element.get_attribute("class"):
                upgrade_element.click()
                print(f"Bought {upgrade}")
                sleep(0.1)
        except Exception as e:
            pass 

def clicker():
    for _ in range(100):
        cookie.click()

start_time = time()
buy_interval = 5  

while True:
    clicker()
    
    current_time = time()
    if current_time - start_time >= buy_interval:
        check_buy()
        start_time = current_time
    
    sleep(0.1)  
