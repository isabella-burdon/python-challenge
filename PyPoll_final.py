# Your task is to create a Python script that analyzes the votes and calculates each of the following values:

    # The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# import pandas package
import pandas as pd

# save file paths as variables
in_path = "Starter_Code/PyPoll/Resources/election_data.csv"
out_path = "Output/election_results.txt"

# read in data
df_polls = pd.read_csv(in_path)

# The total number of votes cast
total_votes = len(df_polls['Ballot ID'])

# A complete list of candidates who received votes
candidates_list = df_polls['Candidate'].unique()

# The percentage of votes each candidate won
# The total number of votes each candidate won
poll_results = [['Candidate', 'Votes', 'Percent vote']]

for candidate in df_polls['Candidate'].unique():
    votes = len(df_polls[df_polls['Candidate'] == candidate])
    percent = (votes / total_votes) * 100
    poll_results.append([candidate, votes, round(percent, 3)])

df_poll_results = pd.DataFrame(poll_results[1:], columns=poll_results[0])

# The winner of the election based on popular vote
winner = df_poll_results['Candidate'][df_poll_results['Percent vote'].idxmax()]

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
{df_poll_results.iloc[0,0]}: {df_poll_results.iloc[0,2]}% ({df_poll_results.iloc[0,1]}) 
{df_poll_results.iloc[1,0]}: {df_poll_results.iloc[1,2]}% ({df_poll_results.iloc[1,1]}) 
{df_poll_results.iloc[2,0]}: {df_poll_results.iloc[2,2]}% ({df_poll_results.iloc[2,1]}) 
-------------------------
Winner: {winner}
-------------------------"""

print(output)

with open(out_path, "w") as file:
    file.write(output)