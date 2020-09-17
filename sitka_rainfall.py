import csv
from datetime import datetime

import matplotlib.pyplot as plt


filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get daily rainfall
    dates, rainfall = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            #This hung me up because I originally used an integer
            # call rather than float and it returned errors for every entry
            rain = float(row[3])
        except ValueError:
            print(f"There is no data for {current_date}")
        else:
            dates.append(current_date)
            rainfall.append(rain)

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, rainfall, c='red')

    title = "Daily rainfall - 2018\nSitka, AK"
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Rainfall (in.)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
