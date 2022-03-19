import os
import csv
import numpy as np

#Accessing csv data and making workable
dates = []
profit_losses = []
bank_csv = os.path.join("Resources", "budget_data.csv")
with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csvreader:
        dates.append(row[0])
        profit_losses.append(int(row[1]))

header = "Financial Analysis"
print(header)

#Finds the total number of months included in the dataset
line1 = f"Total Months: {len(dates)}"
print(line1)

#Finds the net total amount of "Profit/Losses" over the entire period
line2 = f"Total: ${sum(profit_losses)}"
print(line2)

#Finds the changes in "Profit/Losses" over the entire period, 
#and then the average of those changes
changes = []
for x in range(len(profit_losses)-1):
    changes.append(profit_losses[x+1] - profit_losses[x])
change_average = round(np.average(changes), 2)
line3 = f"Average change: ${change_average}"
print(line3)

#Finds the greatest increase in profits (date and amount) over the entire period
big_profit = max(changes)
big_profit_day = dates[changes.index(big_profit)+1]
line4 = f"Greatest Increase in Profits: {big_profit_day} (${big_profit})"
print(line4)
#Finds the greatest decrease in profits (date and amount) over the entire period
big_loss = min(changes)
big_loss_day = dates[changes.index(big_loss)+1]
line5 = f"Greatest Decrease in Profits: {big_loss_day} (${big_loss})"
print(line5)

#Creates output file
output = [header,"\n", line1, "\n", line2, "\n", line3, "\n", line4, "\n", line5]
analysis_path = os.path.join("Analysis", "analysis.txt")
with open(analysis_path, "w") as datafile:
    datafile.writelines(output)
