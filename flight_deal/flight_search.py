import requests
import os
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:
    def __init__(self):
        self.location_endpoint = "https://api.tequila.kiwi.com/locations/query"
        self.header = {"apikey": os.getenv("FLIGHT_API_KEY")}

    def get_iata(self, row:dict):
        parameters = {
            "term": f"{row['city']}",
            "locale": "en-US",
            "location_types": "airport",
            "limit": "1"
        }
        response = requests.get(url=self.location_endpoint, params=parameters, headers=self.header)
        response.raise_for_status()

        return response.json()["locations"][0]["city"]["code"]
