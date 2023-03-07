import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
wanted_price = 350.0
product_url = "https://www.amazon.com/Sony-WH-1000XM5-Canceling-Headphones-Hands-Free/dp/B09XS7JWHH/ref=sr_1_1?keywords=wh-1004m5&qid=1678153681&s=electronics&sr=1-1"


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"
}
response = requests.get(url=product_url, headers=header)

soup = BeautifulSoup(response.text, "lxml")

product_title = soup.select_one("#productTitle").getText().strip()
price_whole = soup.select_one("span.a-price-whole").getText()
price_fraction = soup.select_one("span.a-price-fraction").getText()
price = float(price_whole + price_fraction)


if price <= wanted_price:
    message = f"Subject:Amazon Price Alert!\n\n" \
          f"{product_title} is now ${price}\n" \
          f"{product_url}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=message.encode("utf-8")
        )
        