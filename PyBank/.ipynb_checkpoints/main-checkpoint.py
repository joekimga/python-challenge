# Modules
import os
import csv

# Setting the path
dir = "C:/Users/joeki/Desktop/python-challenge/PyBank/"
file_to_load = os.path.join(dir, "Resources", "budget_data.csv")
file_to_save = os.path.join(dir, "analysis", "budget_analysis.txt")

# Variables
total_months = 0
total_net = 0
#profit_change = we will calculate this anyway
profit_change_list = []
#average :  this will be calculated this anyway so no need to declare
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]



# Open the CSV   ##################UDEMY ACTIVITY #############################
with open(file_to_load) as data:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(data)
    #next pops header off
    header = next(csvreader)
    #data = next(csvreader)
    #print(data)

    # Extract first row (nothing above, so there is no change)
    first_row = next(csvreader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])


    # Count months, revenue, Greatest Increase, Greatest Decrease
    for row in csvreader:
        total_months += 1
        total_net += int(row[1])
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        profit_change_list += [net_change]

        #change_1, change_2 
        #list_ages = [3,10]
        #3, 10
        #0list_ages += [3]
        #list_ages += [10]

        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

    #avg_age = sum(list_ages)/len(list_ages)

    avg_change = sum(profit_change_list)/len(profit_change_list)

results = (
    f"Financial Analysis\n"
    f"-------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Net: ${total_net}\n"
    f"Average Change: ${avg_change:.2f}\n"
    f"Greatest Increase: {greatest_increase[0]} ${greatest_increase[1]}\n"
    f"Greatest Decrease: {greatest_decrease[0]} ${greatest_decrease[1]}\n"
)
print(results)
with open(file_to_save, "w") as txt_file:
    txt_file.write(results)