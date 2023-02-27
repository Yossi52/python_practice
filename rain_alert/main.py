import requests
import smtplib

# https://openweathermap.org/
OWN_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "your api key"
MY_EMAIL = "email@gmail.com"
MY_PASSWORD = "your password"
MY_LAT = 33.45
MY_LON = 126.50


weather_parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": api_key,
    "exclude": "current,minutely,daily",
    "units": "metric"
}

response = requests.get(url=OWN_Endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()["hourly"]
weather_slice = weather_data[:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:It will Rain.\n\nBring an umbrella."
        )
