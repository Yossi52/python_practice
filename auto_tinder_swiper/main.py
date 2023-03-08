import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://tinder.com/")
time.sleep(2)

# # login
login_btn = driver.find_element(by=By.XPATH, value='//*[@id="o1400699221"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_btn.click()
time.sleep(5)
facebook_login = driver.find_element(by=By.XPATH, value='//*[@id="o1622039657"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button')
facebook_login.click()
time.sleep(5)

# window change
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

# send info and login
driver.find_element(by=By.ID, value="email").send_keys(EMAIL)
time.sleep(0.5)
driver.find_element(by=By.ID, value="pass").send_keys(PASSWORD)
time.sleep(0.5)
driver.find_element(by=By.ID, value="loginbutton").click()

# window change
driver.switch_to.window(base_window)
time.sleep(7)


# popup agreement
driver.find_element(by=By.XPATH, value='//*[@id="o1622039657"]/main/div/div/div/div[3]/button[1]').click()
time.sleep(2)
driver.find_element(by=By.XPATH, value='//*[@id="o1622039657"]/main/div/div/div/div[3]/button[2]').click()
time.sleep(2)
driver.find_element(by=By.XPATH, value='//*[@id="o1400699221"]/div/div[2]/div/div/div[1]/div[1]/button').click()
time.sleep(5)


# dislike click
dislike_btn = driver.find_element(by=By.XPATH, value='//*[@id="o1400699221"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[2]')
print(dislike_btn.get_attribute("class"))
dislike_btn.click()

for _ in range(100):
    time.sleep(1)
    try:
        dislike_btn = driver.find_element(by=By.XPATH, value='//*[@id="o1400699221"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]')
        dislike_btn.click()
    except selenium.common.exceptions.NoSuchElementException:
        print("no such element")
        time.sleep(2)
    except selenium.common.exceptions.ElementClickInterceptedException:
        print("intercept")
        time.sleep(3)
        driver.find_element(by=By.XPATH, value='//*[@id="o1622039657"]/main/div/div[2]/button[2]').click()

driver.quit()

