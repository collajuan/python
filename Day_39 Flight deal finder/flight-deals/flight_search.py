import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os

load_dotenv()
class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_API_SECRET")
        self._token = self._get_new_token()

    def get_iata_code(self, city):
        amadeus_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        params = {
            "keyword": city
        }
        response = requests.get(url=amadeus_endpoint, headers={"Authorization": f"Bearer {self._token}"}, params=params)
        response.raise_for_status()
        print(response.json()["data"][0]["iataCode"])
        return response.json()["data"][0]["iataCode"]
        
    
    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token", headers=header, data=body)
        print(response.json()["access_token"])
        print(response.json()["expires_in"])
        return response.json()["access_token"]