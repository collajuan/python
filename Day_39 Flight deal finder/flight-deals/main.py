#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()

sheet_data = data_manager.get_data()
print(sheet_data)
if sheet_data[0]['iataCode'] == '':
    flight_search = FlightSearch()    
    for row in sheet_data:
        row['iataCode'] = flight_search.get_iata_code(row['city'])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()
    print(sheet_data)
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.