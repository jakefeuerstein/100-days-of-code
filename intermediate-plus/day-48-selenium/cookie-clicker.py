from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = "http://orteil.dashnet.org/experiments/cookie/"

chrome_driver_path = "C:\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get(URL)

start_time = time.perf_counter()
cookie = driver.find_element(By.ID, "cookie")
is_clicking = True

while is_clicking:
    cookie.click()
    if time.perf_counter() - start_time >= 5:
        money = int(driver.find_element(By.ID, "money").text)
        cursor_price = int(driver.find_element(By.CSS_SELECTOR, "#buyCursor b").text.split("- ")[1])
        grandma_price = int(driver.find_element(By.CSS_SELECTOR, "#buyGrandma b").text.split("- ")[1])
        print(f"5s passed, money: {money}, cursor price: {cursor_price}")
        start_time = time.perf_counter()
        if money > grandma_price:
            grandma = driver.find_element(By.ID, "buyGrandma")
            try:
                grandma.click()
            except:
                pass

        elif money > cursor_price:
            cursor = driver.find_element(By.ID, "buyCursor")
            try:
                cursor.click()
            except:
                pass
    # else:
    #     time.sleep(1)
    #     print(time.perf_counter())

driver.quit()