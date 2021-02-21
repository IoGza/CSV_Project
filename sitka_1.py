import csv
import matplotlib.pyplot as plt

infile = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(infile, delimiter = ",")

header_row = next(csv_file)

for index, header in enumerate(header_row):
    print("Index:",index, "Column header:", header)

highs = []

for row in csv_file:
    highs.append(int(row[5]))

# print(highs)

plt.plot(highs, c="purple")
plt.title("Daily high temperatures, July 2018", fontsize = 16)
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis="both", which ="major",labelsize=16)
plt.show()