import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Open the Sitka weather data file.
filename = 'sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high temperatures, and low temperatures from this file.
    dates, highs, lows = [], [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)

        high = int(row[5])
        highs.append(high)

        low = int(row[6])
        lows.append(low)


# Display instructions when the program starts.
print("\nWelcome to the Sitka Weather Program!")
print()
print("This program allows you to view the high or low temperatures for Sitka in 2018.")


# Continue displaying the menu until the user selects Exit.
while True:
    print("\nPlease select an option:")
    print("1 - Highs")
    print("2 - Lows")
    print("3 - Exit")
    print()

    choice = input("Please enter your choice: ")

    if choice == "1":
        # Plot the high temperatures.
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')

        # Format the high temperature plot.
        plt.title("Daily High Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()

    elif choice == "2":
        # Plot the low temperatures.
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')

        # Format the low temperature plot.
        plt.title("Daily Low Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()

    elif choice == "3":
        print("\nThank you for using the Sitka Weather Program.")
        print("Goodbye!")
        break

    else:
        print("\nInvalid selection. Please enter 1, 2, or 3.")
