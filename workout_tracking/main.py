import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# --------------- 운동 정보 불러오기 ------------------ #
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

GENDER = "male"
WEIGHT_KG = 75
HEIGHT_CM = 180
AGE = 20
QUERY = input("Tell me which exercise you did: ")

exercise_data = {
    "query": QUERY,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=exercise_endpoint, json=exercise_data, headers=headers)
response.raise_for_status()
result = response.json()["exercises"]


# --------------------- 구글 시트에 저장하기 -------------------- #
sheet_post_endpoint = os.getenv("SHEET_ENDPOINT")
SHEET_TOKEN = os.getenv("SHEET_TOKEN")

today = datetime.now()

for exercise in result:
    new_data = {
        "workout": {
            "date": today.strftime('%d/%m/%Y'),
            "time": today.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    headers = {
        "Authorization": f"Bearer {SHEET_TOKEN}"
    }
    response = requests.post(url=sheet_post_endpoint, json=new_data, headers=headers)
    print(response.text)

