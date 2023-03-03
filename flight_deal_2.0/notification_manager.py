import smtplib
import requests
import os
from dotenv import load_dotenv

load_dotenv()


class NotificationManager:
    def __init__(self, currency_sign, flight_info, stop_over_count):
        self.email = os.getenv("EMAIL")
        self.pw = os.getenv("PASSWORD")
        self.message = ""
        self.curr_sign = currency_sign
        self.flight_info = flight_info
        self.stop_over_cnt = stop_over_count
        self.endpoint = os.getenv("USER_SHEET_ENDPOINT")
        self.header = {"Authorization": f"Bearer {os.getenv('SHEET_TOKEN')}"}

    def send_notification(self, user_email):
        price = self.flight_info['price']
        city_from = self.flight_info['cityFrom']
        city_from_iata = self.flight_info['flyFrom']
        city_to = self.flight_info['cityTo']
        city_to_iata = self.flight_info['flyTo']
        depart_date = self.flight_info['route'][0]['local_departure'][:10]
        arrive_date = self.flight_info['route'][self.stop_over_cnt + 1]['local_arrival'][:10]

        self.message = f"Only {price} {self.curr_sign} to fly from " \
                       f"{city_from}-{city_from_iata} to {city_to}-{city_to_iata}, from " \
                       f"{depart_date} to {arrive_date}"

        if self.stop_over_cnt > 0:
            self.message += f"\n\nFlight has {self.stop_over_cnt} stop over via "
            for i in range(0, self.stop_over_cnt + 2):
                additional_message = f"{self.flight_info['route'][i]['cityFrom']} -> "
                if i == self.stop_over_cnt + 1:
                    additional_message += f"{self.flight_info['route'][i]['cityTo']}"
                self.message += additional_message

        self.message += f"\n\nhttps://www.google.co.kr/flights?hl=kr#flt={city_from_iata}.{city_to_iata}." \
                        f"{depart_date}*{city_to_iata}.{city_from_iata}.{arrive_date}"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.pw)
            connection.sendmail(
                from_addr=self.email,
                to_addrs=user_email,
                msg=f"Subject:Lowe price alert!\n\n"
                    f"{self.message}".encode("UTF-8")
            )

    def send_emails(self):
        response = requests.get(url=self.endpoint, headers=self.header)
        users_data = response.json()["users"]
        for user in users_data:
            self.send_notification(user["email"])
