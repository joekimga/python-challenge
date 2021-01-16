# Modules
import os
import csv

# Set path
dir = "C:/Users/joeki/Desktop/python-challenge/PyPoll/"
#csvpath = os.path.join('..', 'Resources', 'election_data.csv')
file_to_load = os.path.join(dir, "Resources", "election_data.csv")
file_to_save = os.path.join(dir, "analysis", "election_data.txt")


# Variables
total_votes = 0
candidates = []  #do a loop for the list, if list matches, skip
percentage = [] # or dictionary w/ keyvalue pairs
candidates_num = []
# Will caculate this anyways
winner = []
unique_id = []

# Open the CSV
#with open(csvpath) as csvfile:
with open(file_to_load) as data:
    # CSV reader specifies delimiter and variable that holds contents
    #csvreader = csv.reader(csvfile, delimiter=",")
    csvreader = csv.reader(data)

    #next pops header off
    header = next(csvreader)
    
    #print(len(csvreader))  # cannot use the column, must use loop.

    total_votes = 0
    candidates = {}

    # total votes, candidates, percentage, candidates_num, winner
    #total_votes
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate in candidates.keys():
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1
        print(candidates)


    #Find Candidate First, percentage


# count candidates
########  go from list to a set to a list   ########
# set cannot have duplicates

# count candidates,



# winner = Max(total_votes)


