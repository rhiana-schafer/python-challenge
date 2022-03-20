#Your analysis should look similar to the following:
 # Election Results
  #Total Votes: 369711
  #Charles Casper Stockham: 23.049% (85213)
  #Diana DeGette: 73.812% (272892)
  #Raymon Anthony Doane: 3.139% (11606)
  #Winner: Diana DeGette

#Your final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv

#Accessing csv data and making workable
voter_ids = []
counties = []
candidates = []
poll_csv = os.path.join("Resources", "election_data.csv")
with open(poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csvreader:
        voter_ids.append(row[0])
        counties.append(row[1])
        candidates.append(row[2])

header = "Election Results"
print(header)

#The total number of votes cast
line1 = f"Total Votes: {len(voter_ids)}"
print(line1)

#A complete list of candidates who received votes, 
# along with the percentage of votes each candidate won, 
# and the total number of votes each candidate won
line234 = f"{name}: {percent}% ({total_votes})"
print(line234)

#The winner of the election based on popular vote.
line5 = f"Winner: {winner)}"
print(line1)

#Creates output file
output = [header,"\n", line1, "\n", line2, "\n", line3, "\n", line4, "\n", line5]
analysis_path = os.path.join("Analysis", "analysis.txt")
with open(analysis_path, "w") as datafile:
    datafile.writelines(output)