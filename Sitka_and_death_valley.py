import csv
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

infile = open("sitka_weather_2018_simple.csv", "r")
infile2 = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(infile, delimiter=",")
csv_file2 = csv.reader(infile2, delimiter=",")

header_row = next(csv_file)
header_row2 = next(csv_file2)


highs = []
lows = []
dates = []

highs_dv = []
lows_dv = []
dates_dv = []


tmax_index_sitka = header_row.index("TMAX")
tmin_index_sitka = header_row.index("TMIN")
date_index_sitka = header_row.index("DATE")
station_index_sitka = header_row.index("STATION")
name_index_sitka = header_row.index("NAME")

station_name_sitka = header_row[name_index_sitka]


tmax_index_dv = header_row2.index("TMAX")
tmin_index_dv = header_row2.index("TMIN")
date_index_dv = header_row2.index("DATE")
station_index_dv = header_row2.index("STATION")
name_index_dv = header_row2.index("NAME")

station_name_dv = header_row2[name_index_dv]

for row in csv_file:

    station_name_sitka = row[name_index_sitka]
    try:
        high = int(row[tmax_index_sitka])
        low = int(row[tmin_index_sitka])
        convertedDate = datetime.strptime(row[date_index_sitka], "%Y-%m-%d")

    except ValueError:
        print(f"Missing data for {convertedDate}")
    else:
        highs.append(int(row[tmax_index_sitka]))
        lows.append(int(row[tmin_index_sitka]))
        dates.append(convertedDate)

for row in csv_file2:

    station_name_dv = row[name_index_dv]

    try:
        high = int(row[tmax_index_dv])
        low = int(row[tmin_index_dv])
        convertedDate = datetime.strptime(row[date_index_dv], "%Y-%m-%d")

    except ValueError:
        print(f"Missing data for {convertedDate}")
    else:
        highs_dv.append(int(row[tmax_index_dv]))
        lows_dv.append(int(row[tmin_index_dv]))
        dates_dv.append(convertedDate)


fig, ax = plt.subplots(2)


ax[1].plot(dates_dv, highs_dv, c="red")
ax[1].plot(dates_dv, lows_dv, c="purple")

plt.fill_between(dates_dv, highs_dv, lows_dv, facecolor="blue", alpha=0.1)

ax[0].set_title(station_name_sitka, fontsize=14)
plt.tick_params(axis="both", which="major", labelsize=6)


ax[0].plot(dates, highs, c="red")
ax[0].plot(dates, lows, c="purple")


ax[0].fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)


plt.title(station_name_dv, fontsize=14)
plt.tick_params(axis="both", which="major", labelsize=12)


fig.autofmt_xdate()

fig.suptitle(
    "Temperature comparison between " + station_name_sitka + " and " + station_name_dv
)

plt.show()