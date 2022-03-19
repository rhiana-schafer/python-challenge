## PyBank Instructions

#In this challenge, you are tasked with creating a Python script to analyze the financial 
#records of your company. You will give a set of financial data called [budget_data.csv]
#(PyBank/Resources/budget_data.csv). The dataset is composed of two columns: "Date" and 
#"Profit/Losses". 

#Your task is to create a Python script that analyzes the records to calculate each of the following:


#* The greatest increase in profits (date and amount) over the entire period
#* The greatest decrease in profits (date and amount) over the entire period

#Your analysis should look similar to the following:
#  Financial Analysis
#  Total Months: 86
#  Total: $22564198
#  Average Change: $-8311.11
#  Greatest Increase in Profits: Aug-16 ($1862002)
#  Greatest Decrease in Profits: Feb-14 ($-1825558)

#Your final script should both print the analysis to the terminal and export a text file with the results.
#

import os
import csv

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
        profit_losses.append(row[1])

#Finds the total number of months included in the dataset
months = []
[months.append(date[0:3]) for date in dates if date[0:3] not in months]       
num_months = len(months)
print(f"Total number of months in the dataset: {num_months}")

#Finds the net total amount of "Profit/Losses" over the entire period
net_total = 0
for x in profit_losses:
    net_total += int(x)
print(f"Total amount of Profits/Losses: {net_total}")  

#Find the changes in "Profit/Losses" over the entire period, 
#and then the average of those changes
