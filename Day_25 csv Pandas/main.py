# # with open("./weather_data.csv") as file:
# #     data = file.readlines()
# # print(data)

# # import csv

# # with open("./weather_data.csv") as file:
# #     data = csv.reader(file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperatures.append(int(row[1]))
# #     print(temperatures)

import pandas

# data = pandas.read_csv("./weather_data.csv")
# print(data)

# temp_list = data["temp"].to_list()
# # temp_avg = sum(temp_list)/len(temp_list)
# # print(temp_avg)
# print(data["temp"].mean())
# print(data["temp"].max())
# # Imprime unicamente la fila con la temperatura maxima
# print(data[data.temp == data.temp.max()])

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data["Primary Fur Color"].to_list())
count_gray = len(data[data["Primary Fur Color"] == "Gray"])
count_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
count_black = len(data[data["Primary Fur Color"] == "Black"])
# for element in data["Primary Fur Color"].to_list():
#     if element == 'Gray':
#         count_gray += 1
#     elif element == 'Cinnamon':
#         count_cinnamon += 1
#     elif element == 'Black':
#         count_black += 1
    
data_dict = {
    "Fur Color": ['Cinnamon', 'Gray', 'Black',],
    "Count": [count_cinnamon, count_gray, count_black]
}

color_data = pandas.DataFrame(data_dict)
color_data.to_csv("./squirrel_count.csv")

