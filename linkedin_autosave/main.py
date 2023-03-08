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

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3502814454&geoId=105149562&keywords=%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B6%84%EC%84%9D&location=%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD&refresh=true")

time.sleep(1)
login_btn = driver.find_element(by=By.PARTIAL_LINK_TEXT, value="로그인")
login_btn.click()
time.sleep(1)

username = driver.find_element(by=By.ID, value="username")
username.send_keys(EMAIL)
time.sleep(1)

password = driver.find_element(by=By.ID, value="password")
password.send_keys(PASSWORD)
time.sleep(1)

login = driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
login.click()
time.sleep(2)

company = driver.find_elements(by=By.CSS_SELECTOR, value="li.ember-view")
for c in company:
    time.sleep(1.5)
    c.click()
    time.sleep(1.5)
    save_btn = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button')
    save_btn.click()
    driver.execute_script("arguments[0].scrollIntoView();", c)

driver.quit()
print("Save complete.")