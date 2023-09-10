# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# Converting the table to a dictionary
# data_dict = data.to_dict()
# print(data_dict)

# Calculating the average temperature like the mayas did
# temp_list = data["temp"].to_list()
# average_temperature = sum(temp_list)/len(temp_list)
# print(average_temperature)

# Calculating the average temperature with pandas
# print(data["temp"].mean())

# print(data["temp"].max())

# Get data in COLUMNS
# print(data["condition"]
# print(data.condition)

# Get data in ROW
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = data["Primary Fur Color"].value_counts()["Gray"]
cinnamon_squirrels = data["Primary Fur Color"].value_counts()["Cinnamon"]
black_squirrels = data["Primary Fur Color"].value_counts()["Black"]

# Squirrels Count Angela
# gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

squirrels_count_dict = {
    "Fur Color": ['gray', 'red', 'black'],
    "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]
}

squirrels_count = pandas.DataFrame(squirrels_count_dict)
squirrels_count.to_csv("squirrels_count.csv")