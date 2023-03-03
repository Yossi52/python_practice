from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.sheet_get()


for data in sheet_data:
    if data["iataCode"] == "":
        iata_code = flight_search.get_iata(data)
        data_manager.iatacode_update(data, iata_code)
        data["iataCode"] = iata_code

for data in sheet_data:
    flight_data = FlightData(from_iata="ICN", currency="KRW", curr_sign="won")
    flight_info = flight_data.get_flight_info(data["iataCode"])
    notification_manager = NotificationManager(flight_data.sign, flight_info, flight_data.stop_over)
    if data['lowestPrice'] >= flight_info['price']:
        notification_manager.send_emails()

