import csv

with open('budget_data.csv','r') as csv_file:
    read_csv = csv.reader(csv_file, delimiter=',')
    
    dates = []
    revenues = []
    
    next(read_csv)

    for row in read_csv:
        date = row[0]
        revenue = row[1]

        dates.append(date)
        revenues.append(int(revenue))
    
    # print(dates)
    # print(revenues)

print('')
print('Financial Analysis\n')
print('----------------------------\n')

#determine Total Months
totalMonths = len(dates)
print('Total Months: ' + str(totalMonths) + '\n')

#calculate total net amount of Profit/Losses over entire period
netAmount = 0
for i in range(len(revenues)):
    netAmount += revenues[i]
print('Total: ' + str(netAmount) + '\n') 
#rint('Total: ',sum(revenues))