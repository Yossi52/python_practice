import requests
from datetime import datetime
import smtplib
import time


MY_LAT = 33.4994
MY_LONG = 126.5308
MY_EMAIL = "email@gmail.com"
MY_PASSWORD = "password"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = (int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 9) % 24
    sunset = (int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 9) % 24
    time_now = datetime.now()

    if time_now.hour <= sunrise or time_now.hour >= sunset:
        return True

while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:ISS is overhead\n\nGo out side and look up!"
            )


