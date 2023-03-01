import requests
from datetime import datetime


USERNAME = "your name"
TOKEN = "your token"
GRAPH_ID = "graph1"

# ----------- 계정 생성 ------------ #
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# ----------- 그래프 생성 ----------- #
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# ------------- 픽셀 추가 ---------------- #
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
# today = datetime(year=2023, month=2, day=28)
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5.3"
}
# response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)


# --------------픽셀 수정 ---------------- #
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
pixel_update_data = {
    "quantity": "4.8"
}
# response = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)
# print(response.text)


# ---------------픽셀 삭제------------------ #
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)