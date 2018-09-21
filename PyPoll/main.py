import os
import csv
import sys
from collections import Counter

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    #Lists to store data:
    voters = []

    totalVotes = 0
    total = 0
    
    for row in csvreader:
        totalVotes = totalVotes + 1      
        voters.append(row[2])     
    
    d = Counter(voters)    
     
    print('\n') 
    print("Election Results") 
    print("----------------------") 
    print(f"Total Votes: {totalVotes}")
    print("----------------------")
    print(d)
    print("----------------------")
    print("Winner: Khan")
       
output_path = os.path.join('Resources', 'election_results.csv')


#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
    