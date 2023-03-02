import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    def __init__(self):
        self.email = os.getenv("EMAIL")
        self.pw = os.getenv("PASSWORD")
        self.message = ""

    def send_notification(self):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.pw)
            connection.sendmail(
                from_addr=self.email,
                to_addrs=self.email,
                msg=f"Subject:Lowe price alert!\n\n"
                    f"{self.message}".encode("UTF-8")
            )
