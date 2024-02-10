# Use Selenium to fill in the form you created (step 1,2,3 above). Each listing should have its price/address/
# link added to the form. You will need to fill in a new form for each new listing. e.g.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

URL = ""

driver = webdriver.Chrome()
driver.get(URL)
time.sleep(2)
inputs = driver.find_element(By.XPATH, "/html/body/div/div[3]/form/div[2]/div/div[1]/div/div[2]/div[1]/div")
print(inputs.text)
time.sleep(60)

# class FormCreator():
#     def __init__(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get(URL)
#         time.sleep(2)
#
#     def create_form(self, listings: list):
#             self.inputs = self.driver.find_element(By.TAG_NAME, "title")
#             print(self.inputs)
            # self.inputs[0].send_keys(listings[0]['address'])
            # self.inputs[1].send_keys(listing['price'])
            # self.inputs[2].send_keys(listing['link'])

