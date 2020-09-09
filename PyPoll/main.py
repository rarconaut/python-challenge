# You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: 
# Voter ID, County, and Candidate.  

## Import the dependencies needed to read/write csv
import os
import csv

## define the csv path
pypoll_csv = os.path.join("Resources", "election_data.csv")

# reading the election_data.csv file into Python
with open(pypoll_csv, 'r') as csvfile:
    election_results = csv.reader(csvfile, delimiter=',')
    # defining the header
    header = next(budgetData)

    # The total number of votes cast
    total_vote = len(list(election_results))
    total_vote

    # A complete list of candidates who received votes
    for row in election_results:
        if row[2] <> candidates:
            candidates.append(row[2])
        candidates

# Your task is to create a Python script that analyzes the votes and 
# calculates each of the following:

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

# define the function 
def Election_analysis(election_results):

    # variables to store the data
    candidates = []  
   
    # The total number of votes cast
    total_vote = len(list(election_results))

    # A complete list of candidates who received votes
    for row in election_results:
        if row[2] <> candidates:
            candidates.append(row[2])
        candidates
        
    # The percentage of votes each candidate won


    # The total number of votes each candidate won


    # The winner of the election based on popular vote.
    
   
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# #  Set variable for output file path
# output_file = os.path.join("analysis", "PyPoll_analysis.txt")

# #  Open the output file
# with open(output_file, "w") as datafile:
#     writer = csv.writer(datafile)