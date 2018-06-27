import csv
import os
import sys

def calcNumVote(candidate):
    #calculate the number of votes received for the candidate that was passed to the function
    numVotesfor = 0
    for x in candidates:
        if candidate == x:
            numVotesfor += 1      
    return numVotesfor

def calcPerVote(candidate):
    #calculate the percent of votes recieved for the candidate that was passed to the function
    perVotesfor = 0.0
    numVotesfor = 0
    for x in candidates:
        if candidate == x:
            numVotesfor += 1
    perVotesfor = round(((numVotesfor/totalVotesCast)*100), 3)
    return perVotesfor
    
totalVotesCast = 0
candidates = []
counter = 0

filepath = os.path.join('Resources', 'election_data.csv')

with open(filepath, newline='', encoding='utf8') as csv_file:
    read_csv = csv.reader(csv_file, delimiter=',')
    next(read_csv)
    for i in read_csv:
        candidates.append(i[2])
        
    setCandidates = set(candidates)

file_out = open('ElectionResults.txt', 'w')

file_out.writelines(
    [
        'Election Results\n',
        '----------------------------\n \n'
    ]
)


# The total number of votes cast
totalVotesCast = len(candidates)
file_out.writelines(
    [
        f'Total Votes Case: {totalVotesCast}\n',
        '----------------------------\n \n'
    ]
)
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won

#Create Set of candidates to pull unique values out and alphabetize the list
setCandidates = sorted(set(candidates))

mostVotes = 0.0

for i in setCandidates:
    file_out.write(f'{i}: {calcPerVote(i)}% ({calcNumVote(i)}) \n \n')
    if calcPerVote(i) > mostVotes:
        winner = i
        mostVotes = calcPerVote(i)

# The winner of the election based on popular vote.
file_out.writelines(
    [
        '----------------------------\n',
        f'Winner: {winner}'
    ]
)
file_out.close()

file_in = open('ElectionResults.txt', 'r')
print(file_in.read())
file_in.close()