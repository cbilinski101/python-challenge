# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os
import time
import sys

# Files to load and output (update with correct file paths)
election_data_csv = os.path.join('resources', 'election_data.csv')  # Input file path
election_analysis_txt = os.path.join('analysis', 'election_analysis.txt')  # Output file path

# Initialize variables to track the election data
vote_list = []

# Define lists and dictionaries to track candidate names and vote counts
original_dict={}

# Winning Candidate and Winning Count Tracker
winning_candidate = []

# Open the CSV file and process it
with open(election_data_csv, 'r') as election_data:
    csvreader = csv.reader(election_data, delimiter=',')

    # Skip the header row
    header = next(csvreader, None)
   
    # Loop through each row of the dataset and process it
    for row in csvreader:
        vote = row[0]
        vote_list.append(vote)

        key = row[2]
        if key in original_dict:
            original_dict[key] += 1
        else:
            original_dict[key] = 1
 
    # Print a loading indicator (for large datasets)
    def loading_indicator(duration):
        print("Loading", end="")
        for _ in range(duration):
            print(".", end="", flush=True)  # Print dots to indicate loading
            time.sleep(1)  # Simulate a loading delay
        print("\nLoading complete!")

    # Simulate loading for 5 seconds
    loading_indicator(5)

    # Calculate total number of votes
    vote = len(vote_list)

    # Find the key with the maximum value as "winning_candidate"
    winning_candidate = max(original_dict, key=original_dict.get)
 
# Print results
print('Election Results')
print('--------------------------------')
print('Total Votes: ',vote)
print('--------------------------------')
for key, value in original_dict.items():
    percentage_value = (value/vote)*100
    print(f"{key}: {percentage_value:.3f}% ({value})")
print('--------------------------------')  
print("Winner: ",winning_candidate)
print('--------------------------------')  

# Open a text file to save the output
with open(election_analysis_txt, 'w') as f:
    f.write('Election Results')
    f.write('--------------------------------')
    f.write(f"Total Votes: {vote}")
    f.write('--------------------------------')

    f.write('--------------------------------')  
    f.write(f"Winner: {winning_candidate}")
    f.write('--------------------------------')  


