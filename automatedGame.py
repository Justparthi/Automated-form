

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
