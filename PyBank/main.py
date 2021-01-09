# Modules
import os
import csv

# Setting the path
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Variables
months = 0
revenue = 0






# Open the CSV
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    # Count months, revenue, Greatest Increase, Greatest Decrease
    for row in csvreader:
        months += 1
        revenue += 1
