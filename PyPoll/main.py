# importing modules
import os
import csv

# navigating to correct directory
os.chdir('/Users/eimaanejaz/Desktop/GitHub/python-challenge/PyPoll')
# defining path for source file
csvpath = os.path.join(".", "Resources", "election_data.csv")
# defining path for output file
txtpath = os.path.join(".", "analysis", "election_results.txt")

# assigning initial values to variables
total_votes = 0
winner = ""
winner_votes = 0
 # 
candidates = []
votes_by_candidate = {}

# opening csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # ignoring headers
    header = next(csvreader)

    # looping through each row in election data
    for row in csvreader:

        # adding 1 to total number of votes for each row in dataset
        total_votes += 1

        # retreiving candidate name from column 3
        candidate_name = row[2]

        # checking if candidate not already in list
        if candidate_name not in candidates:
            # adding candidates to list
            candidates.append(candidate_name)
            votes_by_candidate[candidate_name] = 0

        # adding 1 to candidate vote count for each row in data set
        votes_by_candidate[candidate_name] += 1

# selecting all candidates in candidate list
for candidate in candidates:
    # assigning total votes per candidate
    votes = votes_by_candidate[candidate]
    # calculating % votes
    vote_percent = round((votes / total_votes) * 100, 3)
 # calculating winner
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate
 
 # defining results
    results = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
    f"{candidate}: {vote_percent}% ({votes})\n"
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

# printing results to terminal
print(results)
