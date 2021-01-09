# Modules
import os
import csv

# Set path
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# Variables
total_votes = 0
candidates = []
percentage = []
candidates_num = []
winner = []


# Open the CSV
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

# total votes, candidates, percentage, candidates_num, winner
total_votes







