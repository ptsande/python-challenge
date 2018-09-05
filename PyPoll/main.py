import os
import csv
import collections
from collections import Counter
#define lists

#define path to resource
poll_data = os.path.join('election_data.csv')

# open file
with open(poll_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
# 1.) Find Total Votes Cast    
    for row in csvreader:
        total_votes = sum(1 for row in csvreader)
    print(total_votes)
    csvfile.seek(0)
    next(csvreader)
# 2.) Full list of candidates who recieved votes
    candidates = []
    for row in csvreader:
        if row [2] not in candidates:
            candidates.append(row[2])
    print(candidates)
    csvfile.seek(0)
    next(csvreader)
# 3.) number of votes each candidate won
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0
    for row in csvreader:
        if (row[2] == "Khan"):
                khan_votes = khan_votes + 1
        if (row[2] == "Correy"):
                correy_votes = correy_votes + 1
        if (row[2] == "Li"):
                li_votes = li_votes + 1
        if (row[2] == "O'Tooley"):
                otooley_votes = otooley_votes + 1
    print(khan_votes)
    print(correy_votes)
    print(li_votes)
    print(otooley_votes)
    csvfile.seek(0)
    next(csvreader)
# 4.) Find percentages
    for row in csvreader:
        khan_percentage = (khan_votes/total_votes) * 100
        correy_percentage = (correy_votes/total_votes) * 100
        li_percentage = (li_votes/total_votes) * 100
        otooley_percentage = (otooley_votes/total_votes) * 100
    print(khan_percentage)
    print(correy_percentage)
    print(li_percentage)
    print(otooley_percentage)
    csvfile.seek(0)
    next(csvreader)
    output_path = os.path.join("final_poll_data.txt")
    with open("final_poll_results.txt", 'w') as text_file:
        print("Election Results", file=text_file)
        print("---------------------------------", file=text_file)
        print(f"Total Votes: " + str(total_votes), file=text_file)
        print("---------------------------------", file=text_file)
        print(f"Khan: " + str(khan_votes) + "(" + str(khan_percentage) + ")", file=text_file)
        print(f"Correy: " + str(correy_votes) + "(" + str(correy_percentage) + ")", file=text_file)
        print(f"Li: " + str(li_votes) + "(" + str(li_percentage) + ")", file=text_file)
        print(f"O'Tooley: " + str(otooley_votes) + "(" + str(otooley_percentage) + ")", file=text_file)


