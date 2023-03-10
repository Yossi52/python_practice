import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

ZILLOW_URL = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.67674483251953%2C%22east%22%3A-122.18991316748047%2C%22south%22%3A37.61800196820299%2C%22north%22%3A37.932247013814965%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
GOOGLE_FORM = "Your account's google form"

# bs 로 주택정보 크롤링
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"
}
response = requests.get(ZILLOW_URL, headers=header)


soup = BeautifulSoup(response.text, "html.parser")

# urls
link_list = soup.find_all(attrs={"data-test": "property-card-link"})[::2]
rental_urls = [item.attrs["href"] for item in link_list]
for i in range(len(rental_urls)):
    if "https://" not in rental_urls[i]:
        rental_urls[i] = "https://www.zillow.com" + rental_urls[i]

# prices
price_list = soup.find_all(attrs={"data-test": "property-card-price"})
prices = [item.text.split("+")[0] for item in price_list]

# addresses
address_list = soup.find_all(attrs={"data-test": "property-card-addr"})
addresses = [item.text for item in address_list]


# selenium으로 구글 폼 작성
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

for i in range(len(addresses)):
    driver.get(GOOGLE_FORM)
    time.sleep(2)
    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(addresses[i])
    price_input.send_keys(prices[i])
    link_input.send_keys(rental_urls[i])

    submit_btn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_btn.click()

driver.quit()




