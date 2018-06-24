import csv
import sys
import os


with open('budget_data.csv','r') as csv_file:
    read_csv = csv.reader(csv_file, delimiter=',')
    
    totalMonths = 0
    totalPL = 0
    totalMMPL = 0
    prevMonth = 0
    mostProfit = 0
    mostLoss = 0
    mmChange = 0
    next(read_csv)
    counter = 0

    for row in read_csv:
        #counter to determine number of records, which will equal number of months.
        totalMonths += 1
        #running total of Profit and Loss
        totalPL += int(row[1])

        if counter == 0:
            prevMonth = int(row[1])
            counter += 1
        else:
            mmChange = int(row[1]) - prevMonth
            if mmChange > mostProfit:
                mostProfit = mmChange
                mostProfitMonth = row[0]
            if mmChange < mostLoss:
                mostLoss = mmChange
                mostLossMonth = row[0]

            totalMMPL = totalMMPL + mmChange
            prevMonth = int(row[1])
            counter += 1

sys.stdout = open('AnalysisOutput.txt', 'w')

print('')
print('Financial Analysis\n')
print('----------------------------\n')

print('Total Months: ' + str(totalMonths) + '\n')

print('Total Profit/Loss: $' + str(totalPL) + '\n') 

avgMonthChange = totalMMPL/counter
print(f'Average Change: $ {round(avgMonthChange, 2)} \n')

print(f'Greatest increase in profits: {mostProfitMonth} ${mostProfit} \n')
print(f'Greatest decrease in profits: {mostLossMonth} ${mostLoss}')