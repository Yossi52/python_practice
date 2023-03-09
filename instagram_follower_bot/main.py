import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os
from dotenv import load_dotenv

load_dotenv()

SIMILAR_ACCOUNT = "nike"
USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")


class InstaFollow:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.follow_list = []

    def login(self):
        """Instagram login method."""
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(5)
        user_name = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        user_name.send_keys(USER_NAME)
        sleep(1)
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(8)
        self.driver.find_element(By.CSS_SELECTOR, "div._ac8f").click()
        sleep(8)
        similar_url = f"https://www.instagram.com/{SIMILAR_ACCOUNT}/"
        self.driver.get(similar_url)
        sleep(8)

    def find_followers(self):
        """Open followers pop-up for specific account."""
        follower_btn = self.driver.find_elements(By.CSS_SELECTOR, "header>section>ul>li")[1]
        follower_btn.find_element(By.CSS_SELECTOR, "a").click()
        sleep(3)

    def find_follows(self):
        """Open follows pop-up for specific account."""
        follower_btn = self.driver.find_elements(By.CSS_SELECTOR, "header>section>ul>li")[2]
        follower_btn.find_element(By.CSS_SELECTOR, "a").click()
        sleep(3)

    def follow(self):
        """Follow accounts in opened pop-up."""
        follow_list = []
        close_count = 0
        stop_following = False
        while not stop_following:
            follow_list = self.driver.find_elements(By.CSS_SELECTOR, "div._aano>div>div>div")[len(follow_list):]

            if len(follow_list) == 0:
                stop_following = True

            for follow in follow_list:
                self.driver.execute_script("arguments[0].scrollIntoView();", follow)
                try:
                    follow.find_element(By.CSS_SELECTOR, "button").click()
                except selenium.common.exceptions.ElementClickInterceptedException:
                    sleep(1)
                    self.driver.find_element(By.CSS_SELECTOR, "button._a9_1").click()
                    close_count += 1
                    if close_count >= 5:
                        stop_following = True
                        break
                else:
                    close_count = 0
                    sleep(1.5)


insta_follow = InstaFollow()
insta_follow.login()
insta_follow.find_follows()
insta_follow.follow()
