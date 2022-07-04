# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.
# Your analysis should look similar to the following:
'''
Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
'''
import os
import csv

filepath = os.path.join("Resources", "election_data.csv")

candidates = {}

# populate dictionary with candidate name and add votes
with open(filepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        candidate = row[2]
        if candidate in list(candidates):
            candidates[candidate] = candidates[candidate] + 1
        else:
            candidates[candidate] = 1

# summary analysis
keys = list(candidates.keys())
values = list(candidates.values())
total = sum(values)
winner_votes = max(values)
winner = keys[values.index(winner_votes)]

# create output
output =[]
output.append("Election Results")
output.append("----------------------------")
output.append(f'Total Votes: {total}')
output.append("----------------------------")
for k, v in candidates.items():
    percent = round((v/total) * 100,3)
    output.append(f'{k} : {percent}% ({v})')
output.append("----------------------------")
output.append(f"Winner: {winner}")
output.append("----------------------------")

# print output to screen and write to analysis_file
analysis_file = os.path.join("analysis", 'election_results.txt')
with open(analysis_file, 'w') as f:
    for row in output:
        print(row)
        f.write(row)
        f.write('\n')
