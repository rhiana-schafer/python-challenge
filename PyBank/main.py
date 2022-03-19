#Your analysis should look similar to the following:
#  Financial Analysis
#  Total Months: 86
#  Total: $22564198
#  Average Change: $-8311.11
#  Greatest Increase in Profits: Aug-16 ($1862002)
#  Greatest Decrease in Profits: Feb-14 ($-1825558)

#Your final script should both print the analysis to the terminal and
#export a text file with the results.

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
    print(f"Header: {csv_header}")
    for row in csvreader:
        dates.append(row[0])
        profit_losses.append(int(row[1]))

print("Financial Analysis")

#Finds the total number of months included in the dataset
print(f"Total Months: {len(dates)}")

#Finds the net total amount of "Profit/Losses" over the entire period
print(f"Total: ${sum(profit_losses)}")  

#Finds the changes in "Profit/Losses" over the entire period, 
#and then the average of those changes
changes = []
for x in range(len(profit_losses)-1):
    changes.append(profit_losses[x+1] - profit_losses[x])

change_average = round(np.average(changes), 2)
print(f"Average change: ${change_average}")

#Finds the greatest increase in profits (date and amount) over the entire period
big_profit = max(changes)
big_profit_day = dates[changes.index(big_profit)+1]
print(f"Greatest Increase in Profits: {big_profit_day} (${big_profit})")

#Finds the greatest decrease in profits (date and amount) over the entire period
big_loss = min(changes)
big_loss_day = dates[changes.index(big_loss)+1]
print(f"Greatest Decrease in Profits: {big_loss_day} (${big_loss})")
