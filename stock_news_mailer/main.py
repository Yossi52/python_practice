import requests
import smtplib

STOCK_KEY = "your key"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_KEY = "your key"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

MY_EMAIL = "email@gmail.com"
MY_PASSWORD = "your pw"

# 소식을 받길 원하는 주식
STOCK = "TSLA"
COMPANY_NAME = "Tesla"

# 주식 정보 가져오기
stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_KEY
}
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]

close_prices = []
for data in stock_data:
    close_prices.append(float(stock_data[data]["4. close"]))
yesterday_close = close_prices[0]
day_before_yesterday_close = close_prices[1]
increase_rate = round(yesterday_close/day_before_yesterday_close - 1, 4)

# 어제와 그저께 종가의 차이가 5% 이상이면 메일을 보냄
if abs(increase_rate) >= 0.05:
    if increase_rate >= 0:
        increase_amount = f"🔺{abs(round(increase_rate * 100, 4))}%"
    else:
        increase_amount = f"🔻{abs(round(increase_rate * 100, 4))}%"

    # 3개의 뉴스 정보 가져옴
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "searchln": "title,description",
        "language": "en",
        "sortBy": "relevancy",
        "pageSize": "3",
        "apiKey": NEWS_KEY
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    articles = news_response.json()["articles"]

    mail_msg = [f"Headline: {article['title']}.\nBrief: {article['description']}" for article in articles]
    # 3개의 뉴스 정보를 각각 메일로 보냄
    for i in range(3):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Tesla Stock news\n\n"
                    f"TSLA: {increase_amount}\n"
                    f"{mail_msg[i]}".encode("UTF-8")
            )
