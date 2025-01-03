import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = "https://api.sheety.co/a44fac337a69cb40e33fc23fda905c7a/flightDeals/prices"
        self.destination_data = self.get_data()

    def get_data(self):
        response = requests.get(self.endpoint)
        response.raise_for_status()
        data = response.json()
        return data['prices']

    def update_destination_codes(self):
        for row in self.destination_data:
            put_params = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }
            response = requests.put(f"{self.endpoint}/{row["id"]}", json=put_params)
            response.raise_for_status()

