from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

BASE_URL = "https://www.instagram.com/"
FOLLOW_ACCT = ""
FOLLOW_XP = "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/" \
            "div[2]/div/ul/div/div/a/div/div[2]/div[2]/div"
LOGIN_XP = "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/" \
           "div[1]/div/label/input"
LOGIN = ""
PW_XP = "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/" \
        "div[2]/div/label/input"
PW = ""
LOGIN_BUTTON_XP = "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/" \
                  "form/div/div[3]"
SAVE_INFO_SET_XP = "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/" \
                   "div/button"
NOTIF_SET_XP = "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/" \
            "button[2]"
SEARCH_BUTTON_XP = "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[1]/div/div[2]/" \
                   "div[2]/div/a/div/div/div/div/svg"
SEARCH_FIELD_XP = "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]" \
            "/div/input"
FOLLOWERS_XP = '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/' \
               'ul/li[2]/a/div'
POPUP_XP = "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get(BASE_URL)
        time.sleep(1)

        login = self.driver.find_element(By.XPATH, LOGIN_XP)
        login.send_keys(LOGIN)
        pw = self.driver.find_element(By.XPATH, PW_XP)
        pw.send_keys(PW)
        login_button = self.driver.find_element(By.XPATH, LOGIN_BUTTON_XP)
        login_button.click()

        time.sleep(4)
        try:
            self.driver.find_element(By.XPATH, SAVE_INFO_SET_XP).click()
        except NoSuchElementException:
            pass

        time.sleep(4)
        try:
            self.driver.find_element(By.XPATH, NOTIF_SET_XP).click()
        except NoSuchElementException:
            pass

    def find_followers(self):
        """Find followers"""
        self.driver.get(BASE_URL+FOLLOW_ACCT)

        time.sleep(4)
        self.driver.find_element(By.XPATH, FOLLOWERS_XP).click()

        time.sleep(4)

        XP = "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(By.XPATH, XP)

        time.sleep(2)
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            try:
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            except:
                pass
            time.sleep(2)

insta_follower = InstaFollower()
insta_follower.login()
insta_follower.find_followers()

time.sleep(60)
# driver.quit()
