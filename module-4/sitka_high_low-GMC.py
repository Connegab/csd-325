# Gabe Conner
# Assignment 4.2

import csv
from datetime import datetime
import sys
from matplotlib import pyplot as plt

# The file path

filename = 'sitka_weather_2018_simple.csv'

# The instructions for using the menu
def print_menu():
    print("\nWelcome to the Sitka Weather Program!")
    print("Choose an option:")
    print("1. Highs - Display high temperatures")
    print("2. Lows - Display low temperatures")
    print("3. Exit - Exit the program")

# Load weather data
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, highs, and lows from the file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)

# Plot temperatures based on user choice
def plot_data(data, color, title):
    fig, ax = plt.subplots()
    ax.plot(dates, data, c=color)

    # Format plot
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

# Main program
while True:
    print_menu()
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        # Plot high temperatures
        plot_data(highs, 'red', "Daily High Temperatures - 2018")
    elif choice == '2':
        # Plot low temperatures
        plot_data(lows, 'blue', "Daily Low Temperatures - 2018")
    elif choice == '3':
        print("Thank you for using the Sitka Weather Program. Goodbye!")
        sys.exit()  # Exit the program
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
