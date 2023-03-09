from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os
from dotenv import load_dotenv


load_dotenv()

TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
USER_ID = os.getenv("USER_ID")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")


class InternetSpeedTwitterBot:
    def __init__(self, promised_down, promised_up):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.PROMISED_DOWN = promised_down
        self.PROMISED_UP = promised_up
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        """인터넷 스피드를 크롤링하는 메소드"""
        self.driver.get("https://www.speedtest.net/")
        sleep(3)
        go_btn = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_btn.click()
        sleep(45)

        down_speed = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.down = down_speed.text
        up_speed = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.up = up_speed.text

        print(f"down: {self.down}")
        print(f"up: {self.up}")

        return (self.down, self.up)


    def tweet_at_provider(self, msg):
        """트위터에 로그인 하고 개인 서클에 메세지를 트윗하는 메소드"""
        self.driver.get("https://twitter.com/")
        sleep(2)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="layers"]/div/div[1]/div/div/div/div/div/div/div/div[1]/a').click()
        sleep(2)
        email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)
        sleep(2)
        user_id = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        user_id.send_keys(USER_ID)
        user_id.send_keys(Keys.ENTER)
        sleep(2)
        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(7)

        mention_btn = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        mention_btn.click()
        sleep(2)

        mention_box = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        mention_box.send_keys(msg)
        sleep(3)

        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[1]/div/div').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[3]/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div[3]').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]').click()
        sleep(2)

        self.driver.quit()