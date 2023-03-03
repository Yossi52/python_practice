import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()


class FlightData:
    def __init__(self, from_iata="LON", currency="GBP", curr_sign="£"):
        self.search_endpoint = "https://api.tequila.kiwi.com/v2/search"
        self.header = {"apikey": os.getenv("FLIGHT_API_KEY")}
        self.depart = from_iata
        self.currency = currency
        self.sign = curr_sign
        self.stop_over = 0
        self.via_city = ""

    def get_flight_info(self, to_iata):
        parameters = {
            "fly_from": self.depart,
            "fly_to": to_iata,
            "date_from": (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y"),
            "date_to": (datetime.now() + timedelta(days=6 * 30)).strftime("%d/%m/%Y"),
            "nights_in_dst_from": "7",
            "nights_in_dst_to": "28",
            "flight_type": "round",
            "curr": self.currency,
            "max_stopovers": str(self.stop_over),
            "limit": "1"
        }

        while True:
            response = requests.get(url=self.search_endpoint, params=parameters, headers=self.header)
            try:
                info = response.json()["data"][0]
            except IndexError:
                self.stop_over += 1
                parameters["max_stopovers"] = str(self.stop_over)
            else:
                return info

