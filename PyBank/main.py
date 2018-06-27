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

#determine Total Months
totalMonths = len(dates)

#Create new tuple list using lists already created.
extendedData = zip(dates, revenues, profitChanges)

file_out = open('AnalysisOutput.txt', 'w')

file_out.write('\n')
file_out.write('Financial Analysis\n')
file_out.write('----------------------------\n \n')
file_out.write(f'Total Months: {str(totalMonths)}\n \n')

#calculate total net amount of Profit/Losses over entire period
file_out.write(f'Total Profit/Loss: $ {sum(revenues)} \n \n')

#calculate average change between months i.e. Nov12-Oct12=month to month change
file_out.write(f'Average Change: $ {round((sum(profitChanges)/counter), 2)} \n \n')

for j in extendedData:
    if j[2] > mostProfit:
        mostProfit = j[2]
        mostProfitMonth = j[0]
    if j[2] < mostLoss:
        mostLoss = j[2]
        mostLossMonth = j[0]
        
#The greatest increase in profits (date and amount) over the entire period
file_out.write(f'Greatest Increase in Profits: {mostProfitMonth} (${mostProfit}) \n \n')

#The greatest decrease in losses (date and amount) over the entire period
file_out.write(f'Greatest Increase in Profits: {mostLossMonth} (${mostLoss}) \n')
file_out.close()

#Open output file created in above code and output to the console
file_in = open('AnalysisOutput.txt','r')
print(file_in.read())
file_in.close()