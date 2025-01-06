#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

data_manager = DataManager()
sheet_data = data_manager.get_data()
flight_search = FlightSearch()
flight_data = FlightData(
    price="N/A",
    origin_airport="N/A", 
    destination_airport="N/A", 
    out_date="N/A",
    return_date="N/A"
)

print(sheet_data)
for row in sheet_data:
    if row['iataCode'] == '':
        row['iataCode'] = flight_search.get_iata_code(row['city'])
        time.sleep(2)

print(sheet_data)
data_manager.destination_data = sheet_data
data_manager.update_destination_codes()


# **********************************

tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
six_month_from_today = (datetime.now() + timedelta(days=(6 * 30))).strftime("%Y-%m-%d")

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.get_flight_data(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = flight_data.find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        send_sms = NotificationManager()
        send_sms.send_sms_alert(cheapest_flight)
    else:
        print("No hay vuelo economico")

