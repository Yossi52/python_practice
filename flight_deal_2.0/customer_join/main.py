import requests
import os
from dotenv import load_dotenv

load_dotenv()

USER_SHEET_ENDPOINT = os.getenv("USER_SHEET_ENDPOINT")
header = {"Authorization": f"Bearer {os.getenv('SHEET_TOKEN')}"}

print("Welcome to Yossi's Flight Club.")
print("We find the best flight deals and email you.")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
email_check = input("Type your email again.\n")

if email == email_check:
    user_info = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }
    }
    response = requests.post(url=USER_SHEET_ENDPOINT, json=user_info, headers=header)
    print("You're in the club!")