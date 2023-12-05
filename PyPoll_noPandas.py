# save file paths as variables
in_path = "Starter_Code/PyPoll/Resources/election_data.csv"
out_path = "Output/election_results.txt"

# read in data
with open(in_path, 'r') as file:
    # Assuming the first row is the header
    header = file.readline().strip().split(',')
    data = [line.strip().split(',') for line in file]

# The total number of votes cast
total_votes = len(data)

# A complete list of candidates who received votes
candidates_list = set(row[header.index('Candidate')] for row in data)

# The percentage of votes each candidate won
# The total number of votes each candidate won
poll_results = [['Candidate', 'Votes', 'Percent vote']]

for candidate in candidates_list:
    votes = sum(1 for row in data if row[header.index('Candidate')] == candidate)
    percent = (votes / total_votes) * 100
    poll_results.append([candidate, votes, round(percent, 3)])

# The winner of the election based on popular vote
winner = max(poll_results[1:], key=lambda x: x[2])[0]

# Your analysis should align with the following results:

# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------

output = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{poll_results[1][0]}: {poll_results[1][2]}% ({poll_results[1][1]})
{poll_results[2][0]}: {poll_results[2][2]}% ({poll_results[2][1]})
{poll_results[3][0]}: {poll_results[3][2]}% ({poll_results[3][1]})
-------------------------
Winner: {winner}
-------------------------"""

print(output)

with open(out_path, "w") as file:
    file.write(output)
