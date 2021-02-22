# Using the datetime module


import csv
import matplotlib.pyplot as plt
from datetime import datetime

fig = plt.figure()

infile = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(infile, delimiter=",")

header_row = next(csv_file)

# for index, header in enumerate(header_row):
#     print("Index:",index, "Column header:", header)

highs = []
lows = []
dates = []
for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    convertedDate = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(convertedDate)


plt.plot(dates, highs, c="red")
plt.plot(dates,lows, c = "purple")

plt.fill_between(dates,highs,lows, facecolor = "blue", alpha = .1)


plt.title("Daily High and Low Temperatures for 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)


fig.autofmt_xdate()

plt.show()

fig2, a = plt.subplots(2)

a[0].plot(dates,highs, c='red')
a[1].plot(dates,lows, c='purple')

plt.show()