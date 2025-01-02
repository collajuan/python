import requests
from twilio.rest import Client


api_key = "..."
account_sid = '...'
auth_token = '...'
lat =-34.901112
lon =-56.164532



endpoint = "https://api.openweathermap.org/data/2.5/weather"
five_days_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat":lat,
    "lon":lon,
    "cnt":4,
    "appid":api_key
}
response = requests.get(five_days_endpoint, params=parameters)
response.raise_for_status()
data = response.json()
print(data)
print(data["list"])
will_rain = False
for slot in data["list"]:
    print(slot["weather"][0]["id"])

    if int(slot["weather"][0]["id"]) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today!",
        from_='+1.......',
        to='+34............'
    )

    print(message.status)
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Hoy no lloverá",
        from_='+1.......',
        to='+34............'
    )
    print("Hoy no lloverá")
    print(message.status)
    print(message.sid)
