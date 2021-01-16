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
        candidate = row[0]
        if candidate in candidates.keys():
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1
        #print(candidates)
        #print(candidate)

    ##########################################
    ######  UDEMY ROADMAP   #############
    for row in csvreader:
        # Count the total number of votes
        total_votes += 1
        # Set the candidate names to candidatelist
        candidates.append(row[2])
        # Create a set from the candidatelist to get the unique candidate names
    for x in set(candidates):
        unique_id.append(x)
        # y is the total number of votes per candidate
        y = candidates.count(x)
        total_votes.append(y)
        # z is the percent of total votes per candidate
        z = (y/count)*100
        vote_percent.append(z)


#total_vote  = Tally up the candidates  check
# if candidate = 1 total_votes
# total for candidate
# total for Corry, etc
# then divide by total_vote

# Do a comparison logic
# total cand_vote +=
# divide total by # candidate


    #Find Candidate First, percentage

# count candidates
########  go from list to a set to a list   ########
# set cannot have duplicates

# count candidates,

# percentage = total_votes/candidates_num
#percent = round(int(row[6]) / int(row[5]), 2)
    #review_percent.append(percent)
percent = round(int(total_votes) / int(candidates_num), 2)
review_percent.append(percent)


print(percentage)
# winner = Max(total_votes)
max(candidate)


# results = (
#     f"Total Votes\n"
#     f"Candidates: {}"
#     f"Percentate: {}"
#     f""

# )
# print("results")