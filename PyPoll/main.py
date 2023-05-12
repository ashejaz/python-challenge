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
# creating list of candidates
candidates = []
# creating candidate dictionary
votes_per_candidate = {}

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
            votes_per_candidate[candidate_name] = 0

        # adding 1 to candidate vote count for each row in data set
        votes_per_candidate[candidate_name] += 1

# formatting results
results = "Election Results\n"
results += "-------------------------\n"
 # defining results for total votes
results += f"Total Votes: {total_votes}\n"
results += "-------------------------\n"
# looping through candidates in candidate list
for candidate in candidates:
    # assigning total votes to each candidate
    votes = votes_per_candidate[candidate]
    # calculating % votes
    vote_percent = round((votes / total_votes) * 100, 3)
    # adding every candidates name, % of votes and total votes to results list
    results += f"{candidate}: {vote_percent}% ({votes})\n"
    # calculating winner
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate
# adding winner name to results list
results += "-------------------------\n"
results += f"Winner: {winner}\n"
results += "-------------------------\n"

# printing results to terminal
print(results)

# printing results to output file
with open(txtpath, "w") as election_results:
    election_results.write(results)