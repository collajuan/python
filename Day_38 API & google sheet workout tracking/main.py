import requests
from datetime import datetime

APP_ID = "cdeb1824"
API_KEY = "..."

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

user_text = input('Type your exercise: ')
parameters = {
    "query": user_text,
    "weight_kg": 76,
    "height_cm": 179,
    "age": 35
}
response = requests.post(url=endpoint, headers=headers,json=parameters)
response.raise_for_status()
print(response.json())
exercise = response.json()["exercises"][0]["name"]
duration = response.json()["exercises"][0]["duration_min"]
calories = response.json()["exercises"][0]["nf_calories"]

sheety_endpoint = "https://api.sheety.co/a44fac337a69cb40e33fc23fda905c7a/myWorkoutsJuan/workouts"
date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")
print(date,time)
sheety_params = {
    "workout" : {
        "date": date,
        "time": time,
        "exercise": exercise.title(),
        "duration": duration,
        "calories": calories
    }
}

print(sheety_params)
response = requests.post(url=sheety_endpoint,json=sheety_params, auth=('...', '...'))
response.raise_for_status()
print(response.text)