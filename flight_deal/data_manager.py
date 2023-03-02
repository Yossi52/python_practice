import requests
import os
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    def __init__(self):
        self.endpoint = os.getenv("SHEET_ENDPOINT")
        self.header = {
            "Authorization": f"Bearer {os.getenv('SHEET_TOKEN')}"
        }

    def sheet_get(self):
        response = requests.get(url=self.endpoint, headers=self.header)
        response.raise_for_status()
        return response.json()["prices"]

    def iatacode_update(self, city:dict, code):
        data = {
            "price":{
                "iataCode": code
            }
        }
        response = requests.put(url=f"{self.endpoint}/{city['id']}", json=data, headers=self.header)
        response.raise_for_status()