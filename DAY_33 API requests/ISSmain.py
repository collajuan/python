import requests
import  datetime as datetime


iss_response = requests.get("http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()
iss_data = iss_response.json()

iss_latitude = float(iss_data["iss_position"]["latitude"])
iss_longitude = float(iss_data["iss_position"]["longitude"])

print(iss_data)
my_lat = -42.2552
my_long = -109.4877

parameters = {
    "lat": my_lat,
    "lng":my_long,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
result = response.json()
sunrise = int(result["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(result["results"]["sunset"].split("T")[1].split(":")[0])

print(sunrise)
print(sunset)

time_now = datetime.datetime.now().hour
print(time_now)

def is_iss_close():
    if iss_latitude - 5 <= my_lat <= iss_latitude + 5 and iss_longitude - 5 <= my_long <= iss_longitude + 5:
        return True
    else:
        return False

if time_now >= sunset or time_now <= sunrise:
    print("It's dark")
    if is_iss_close():
        print("The ISS is close")
    else:
        print("The ISS is not close")
else:
    print("It's light")
    if is_iss_close():
        print("The ISS is close")
    else:
        print("The ISS is not close")