# Modules
import os
import csv

# Set path
dir = "C:/Users/joeki/Desktop/python-challenge/PyPoll/"
file_to_load = os.path.join(dir, "Resources", "election_data.csv")
file_to_save = os.path.join(dir, "analysis", "election_data.txt")


# Variables
total_votes = 0
candidates = {}

# Open the CSV
#with open(csvpath) as csvfile:
with open(file_to_load) as data:
    # CSV reader specifies delimiter and variable that holds contents
    #csvreader = csv.reader(csvfile, delimiter=",")
    csvreader = csv.reader(data)

    #next pops header off
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate in candidates.keys():
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1
# print(candidates)
print(total_votes)

with open(file_to_save, "w") as txt_file:
    election_result = (
        f"Election Result\n"
        f"---------------------\n"
        f"Total Votes: {total_votes}\n"
        f"---------------------\n")
    txt_file.write(election_result)
    for candidate, votes in candidates.items():
        percent = round(votes/total_votes * 100, 2)
        candidate_result = f"{candidate}: {percent:.2f}% ({votes})\n"
        print(candidate_result)
        txt_file.write(candidate_result)
    winner = max(candidates, key = candidates.get)
    winning_candidate = f"Winner: {winner}\n"
    #print('Winner', winner)
    txt_file.write(winning_candidate)
    print('Winner', winner)
# results = (
#     f"Total Votes\n"
#     f"Candidates: {}"
#     f"Percentate: {}"
#     f"Winner": {}""

# )
# print("results")