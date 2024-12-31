import requests

api_key = "f25167cc23c4740a0ed100f72a87851e"
lat =39.758602
lon =-39.758602


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
    print("Lloverá")
else:
        print("No lloverá")