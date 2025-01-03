import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os

load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = "https://api.sheety.co/a44fac337a69cb40e33fc23fda905c7a/flightDeals/prices"
        self.user = os.getenv("SHEETY_USRERNAME")
        self.password = os.getenv("SHEETY_PASSWORD")
        self.authorization = HTTPBasicAuth(self.user, self.password)
        self.destination_data = {}


    def get_data(self):
        response = requests.get(self.endpoint, auth=self.authorization)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            put_params = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(f"{self.endpoint}/{city["id"]}", json=put_params,auth=self.authorization)
            response.raise_for_status()
            print(response.text)

