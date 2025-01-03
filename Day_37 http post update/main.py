from datetime import datetime
import requests

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "collajuan"
TOKEN = "...."

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
# *******

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_id = "graph1"
graph_config = {
    "id": graph_id,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# Se crea nueva grafica
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# *******


# POST a pixel
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
today = datetime.now()
pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "25"
}
# response = requests.post(post_pixel_endpoint,json=pixel_params,headers=headers)
# print(response.text)

# PUT pixel
put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{today.strftime("%Y%m%d")}"
put_params = {
   "quantity": "10"
}
# response = requests.put(url=put_endpoint, json=put_params, headers=headers)
# print(response.text)

# DELETE pixel
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{today.strftime("%Y%m%d")}"
response = requests.delete(url=delete_endpoint,headers=headers)
print(response.text)