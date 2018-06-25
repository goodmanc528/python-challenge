import csv
import os
import sys
import logging

dates = []
revenues = []
profitChanges = []
counter = 0
mostProfit = 0
mostProfitMonth = ''
mostLoss = 0
mostLossMonth = ''

filepath = os.path.join('Resources', 'budget_data.csv')

with open(filepath, newline='', encoding='utf8') as csv_file:
    read_csv = csv.reader(csv_file, delimiter=',')    
    next(read_csv)
    for row in read_csv:
        dates.append(row[0])
        revenues.append(int(row[1]))

for j in range(len(revenues)):
    if j == 0:
        pass
        profitChanges.append(0)
    else:
        k=j-1
        profitChanges.append(revenues[j]-revenues[k])
        counter += 1

#sys.stdout = open('AnalysisOutput.txt', 'w')

print('')
print('Financial Analysis\n')
print('----------------------------\n')

#determine Total Months
totalMonths = len(dates)
print(f'Total Months: {str(totalMonths)} \n')

#calculate total net amount of Profit/Losses over entire period
# netAmount = 0
# for i in range(len(revenues)):
#     netAmount += revenues[i]
# print(f'Total Profit/Loss: $ {str(netAmount)} \n') 
print(f'Total Profit/Loss: $ {sum(revenues)} \n')

#calculate average change between months i.e. Nov12-Oct12=month to month change
print(f'Average Change: $ {round((sum(profitChanges)/counter), 2)} \n')

#Create new tuple list using lists already created.
# keys = ["Date", "Revenue", "Change from Previous Month"]
# values = [dates, revenues, profitChanges]
# y = dict(zip(keys,values))
extendedData = zip(dates, revenues, profitChanges)
for j in extendedData:
    if j[2] > mostProfit:
        mostProfit = j[2]
        mostProfitMonth = j[0]
    if j[2] < mostLoss:
        mostLoss = j[2]
        mostLossMonth = j[0]
        
#The greatest increase in profits (date and amount) over the entire period
print(f'Greatest Increase in Profits: {mostProfitMonth} (${mostProfit}) \n')

#The greatest decrease in losses (date and amount) over the entire period
print(f'Greatest Increase in Profits: {mostLossMonth} (${mostLoss}) \n')

