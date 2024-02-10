from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path))

# driver.get("https://www.amazon.com/Neiko-02847A-Unibody-Checkered-Resistant/dp/B000QYC26K?th=1")
# price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print(price.text)

driver.get("https://www.python.org/")
event_dates_sl = driver.find_elements(By.CSS_SELECTOR, "div.medium-widget.event-widget.last .menu time")
event_names_sl = driver.find_elements(By.CSS_SELECTOR, "div.medium-widget.event-widget.last .menu a")
events = {
    'time': [event_dates_sl[n].text for n in range(len(event_names_sl))],
    'name': [event_names_sl[n].text for n in range(len(event_names_sl))]
}
#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last
print(events)

driver.quit()