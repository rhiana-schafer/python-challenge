import os
import csv

#Accessing csv data and making workable
output = []
cands = {}
poll_csv = os.path.join("Resources", "election_data.csv")
with open(poll_csv) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=",")
  csv_header = next(csvfile)
  for row in csvreader:
    #creates candidate dict, where key is candidate and value is number of votes they received
    if row[2] not in cands:
      cands[row[2]] = 0
    cands[row[2]] += 1

#print and output header 
header = "Election Results"
output.append(header)
output.append("\n")
print(header)   

#sum up total votes
total_votes = 0
for cand in cands:
  total_votes += cands[cand]

#print and output total votes
line1 = f"Total Votes: {total_votes}"
output.append(line1) 
output.append("\n")
print(line1)

#print and output each candidate, % votes, and # votes
#determines winner
winner_name = ""
winning_votes = 0
for cand in cands:
  cand_votes = cands[cand]
  percent = round(cand_votes/total_votes*100, 3)
  line = f"{cand}: {percent}% ({cand_votes})"
  output.append(line)
  output.append("\n")
  print(line)
  if winning_votes < cand_votes:
    winning_votes = cand_votes
    winner_name = cand

#print and output winner
line5 = f"Winner: {winner_name}"
output.append(line5)
print(line5)

#Creates output file
analysis_path = os.path.join("Analysis", "analysis.txt")
with open(analysis_path, "w") as datafile:
    datafile.writelines(output)