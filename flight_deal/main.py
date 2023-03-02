from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData(from_iata="LON", currency="GBP", curr_sign="£")
notification_manager = NotificationManager()
sheet_data = data_manager.sheet_get()


for data in sheet_data:
    if data["iataCode"] == "":
        iata_code = flight_search.get_iata(data)
        data_manager.iatacode_update(data, iata_code)
        data["iataCode"] = iata_code

for data in sheet_data:
    flight_info = flight_data.get_flight_info(data["iataCode"])
    if data['lowestPrice'] >= flight_info['price']:
        notification_manager.message = f"Only {flight_data.sign}{flight_info['price']} to fly from " \
                                       f"{flight_info['cityFrom']}-{flight_info['flyFrom']} to " \
                                       f"{flight_info['cityTo']}-{flight_info['flyTo']}, from " \
                                       f"{flight_info['route'][0]['local_departure'][:10]} to " \
                                       f"{flight_info['route'][1]['local_arrival'][:10]}"
        notification_manager.send_notification()

