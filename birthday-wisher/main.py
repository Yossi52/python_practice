import datetime
import pandas
import random
import smtplib


MY_EMAIL = "email@gmail.com"
MY_PASSWORD = "password"

birth_data = pandas.read_csv("birthdays.csv")
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

now = datetime.datetime.now()
month = now.month
day = now.day
# 생일이 같은 사람이 있을 수도 있으니 생일자를 리스트로 받음
targets = []
modify_letters = []

# 오늘이 생일인지 확인
for i in range(birth_data["month"].count()):
    if birth_data.iloc[i, 3] == month and birth_data.iloc[i, 4] == day:
        targets.append(birth_data.iloc[i, :])

# 생일인 사람의 이름을 3개의 편지형식 중 하나를 선택해 적용
for i in range(len(targets)):
    with open(file=f"letter_templates/{random.choice(letters)}", mode="r") as data:
        letter = data.read()
        new_letter = letter.replace("[NAME]", targets[i]["name"])
        modify_letters.append(new_letter)

# 메일 보냄
if len(targets) != 0:
    for i in range(len(targets)):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=targets[i]["email"],
                msg=f"Subject:Happy Birthday!\n\n{modify_letters[i]}"
            )
