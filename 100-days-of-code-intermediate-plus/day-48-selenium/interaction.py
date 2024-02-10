from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# URL = "https://en.wikipedia.org/wiki/Main_Page"
URL = "https://www.google.com/"

chrome_driver_path = "C:\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get(URL)
# article_count = driver.find_element(By.CSS_SELECTOR, "div #articlecount a")
# article_count.click()
# print(article_count)

# all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# all_portals.click()

search = driver.find_element(By.NAME, "q")
search.send_keys("Python", Keys.ENTER)
# search.send_keys(Keys.ENTER)
time.sleep(5)

