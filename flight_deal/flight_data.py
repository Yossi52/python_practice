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

    def get_flight_info(self, to_iata):
        parameters = {
            "fly_from": self.depart,
            "fly_to": to_iata,
            "date_from": (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y"),
            "date_to": (datetime.now() + timedelta(days=6*30)).strftime("%d/%m/%Y"),
            "nights_in_dst_from": "7",
            "nights_in_dst_to": "28",
            "flight_type": "round",
            "curr": self.currency,
            "max_stopovers": "0",
            "limit": "1"
        }
        response = requests.get(url=self.search_endpoint, params=parameters, headers=self.header)

        return response.json()["data"][0]


