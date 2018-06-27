import csv
import os
import sys
import logging

def calcNumVote(candidate):
    #perVotesfor = 0.0
    numVotesfor = 0
    for x in candidates:
        if candidate == x:
            numVotesfor += 1      
    #perVotesfor = numVotesfor/totalVotesCast
    #return (perVotesfor, numVotesfor)
    return numVotesfor

def calcPerVote(candidate):
    perVotesfor = 0.0
    numVotesfor = 0
    for x in candidates:
        if candidate == x:
            numVotesfor += 1
    perVotesfor = round(((numVotesfor/totalVotesCast)*100), 3)
    return perVotesfor
    
####return multiple values use Tuple
####build tuple with parentheses, i.e. return TupleName
####

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
    ListCandidates = list(setCandidates)


print('\n')
print('Election Results\n')
print('----------------------------\n')


# The total number of votes cast
totalVotesCast = len(candidates)
print(f'Total Votes Case: {totalVotesCast}\n')
print('----------------------------\n')
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won

setCandidates = sorted(set(candidates))
ListCandidates = list(setCandidates)
#print(ListCandidates)
#input('Press Enter....')

mostVotes = 0.0

for i in ListCandidates:
    print(f'{i}: {calcPerVote(i)}% ({calcNumVote(i)}) \n')
    if calcPerVote(i) > mostVotes:
        winner = i
        mostVotes = calcPerVote(i)

# The winner of the election based on popular vote.
print('----------------------------\n')
print(f'Winner: {winner}')