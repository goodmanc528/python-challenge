import csv

with open('budget_data.csv','r') as csv_file:
    read_csv = csv.reader(csv_file, delimiter=',')
    
    dates = []
    revenues = []
    profitChanges = []
    
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
print('Total Profit/Loss: ' + str(netAmount) + '\n') 
#print('Total: ',sum(revenues))

#calculate average change between months i.e. Nov12-Oct12=month to month change
 
counter = 0

for j in range(len(revenues)):
    if j == 0:
        pass
    else:
        k=j-1
        ####print(f"This is {dates[k]}'s revenue {revenues[k]}")
        ####print(f"This is {dates[j]}'s revenue {revenues[j]}")
        profitChanges.append(revenues[j]-revenues[k])
        counter += 1

###print(sum(profitChanges))
###print(counter)
print(f'Average Change: $ {sum(profitChanges)/counter}')


#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period
