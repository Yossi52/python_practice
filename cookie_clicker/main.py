from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(3)
kor_btn = driver.find_element(by=By.ID, value="langSelect-KO")
kor_btn.click()
time.sleep(3)

cookie = driver.find_element(by=By.ID, value="bigCookie")

play_minute = 15
increment = 10
cur_time = time.time()
timeout = time.time() + 60 * play_minute
while True:
    if time.time() >= cur_time + increment:
        cur_time = time.time()

        upgrade_list = driver.find_elements(by=By.CSS_SELECTOR, value="#upgrades div.enabled")
        try:
            upgrade_list[0].click()
        except IndexError:
            pass

        product_list = driver.find_elements(by=By.CSS_SELECTOR, value="#products div.enabled")
        try:
            product_list[-1].click()
            product_list[-2].click()
        except IndexError:
            pass


    if time.time() > timeout:
        break

    cookie.click()

final_cps = driver.find_element(by=By.ID, value="cookiesPerSecond")
print(final_cps.text)