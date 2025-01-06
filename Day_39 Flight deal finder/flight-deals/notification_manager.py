import requests
from requests.auth import HTTPBasicAuth
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def send_sms_alert(self,flight):
        client = Client(os.getenv("TWILIO_ID"), os.getenv("TWILIO_TOKEN"))
        body_message = f"Low price alert! {flight.price} to fly from {flight.origin_airport} to {flight.destination_airport} on {flight.out_date} until {flight.return_date}" 
        
        message = client.messages.create(
            body=body_message,
            from_= os.getenv("VIRTUAL_NUMBER"),
            to= os.getenv("VERIFIED_NUMBERS")
        )    

        print(message.status)
