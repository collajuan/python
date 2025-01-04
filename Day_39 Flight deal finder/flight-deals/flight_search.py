import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os

load_dotenv()
SEARCH_FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
SEARCH_IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_API_SECRET")
        self._token = self._get_new_token()

    def get_iata_code(self, city):
        params = {
            "keyword": city
        }
        response = requests.get(url=SEARCH_IATA_ENDPOINT, headers={"Authorization": f"Bearer {self._token}"}, params=params)
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
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        print(response.json()["access_token"])
        print(response.json()["expires_in"])
        return response.json()["access_token"]
    
    def get_flight_data(self, origin_city_code, destination_city_code, from_time, to_time):
        headers={
            "Authorization": f"Bearer {self._token}"
        }
        
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time,
            "returnDate": to_time,
            "nonStop": "true",
            "currencyCode": "GBP",
            "adults": 1,
            "max": 10
        }

        response = requests.get(url=SEARCH_FLIGHT_ENDPOINT, headers=headers, params=query)
        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()
        