import csv
from distutils import text_file
from os import name
from collections import Counter
from sqlite3 import Row
import os
with open("election_data.csv") as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=",") 
    header=next(csv_reader)
    votes=0

    Candidates =[]
    votes_per_candidate={}


    winner=""
    winning_votes=0
    winning_percentage=0


    for row in csv_reader:
        votes=votes+1
        Total_votes_Summary=(f"Total Votes:{votes}")
        name_of_candidate= row[2]

        if name_of_candidate not in Candidates:
            Candidates.append(name_of_candidate)
            votes_per_candidate[name_of_candidate]=0
        votes_per_candidate[name_of_candidate]+=1
            

    for name_of_candidate in votes_per_candidate:
        Total_votes=votes_per_candidate.get(name_of_candidate)
        votes_percentage=float(Total_votes)/float(votes)*100
        candidate_result=(
            f"{Candidates}:{votes_percentage:.1f}% ({Total_votes:,})\n")

        if (Total_votes >winning_votes):
            winning_votes=Total_votes
            winner=name_of_candidate
            winning_candidate=(f"Winner: {winner}")




print("Election Results")
print("=================================")
print(Total_votes_Summary)
print("=================================")
print(Candidates)
print(votes_per_candidate)
print(candidate_result)
print("=================================")
print(winning_candidate)



