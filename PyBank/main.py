import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as budgetdata:
   
    csvreader = csv.reader(budgetdata, delimiter=',')   
    csv_header = next(budgetdata)    

#assign lists:
    TotalMonthList = []
    TotalList1 = []
    TotalList2 = []
    change = []
    changemonths = []

    Total = 0
    TotalMonths = 0
        
    for row in csvreader:
        TotalMonths = TotalMonths + 1
        Total = Total + int(row[1]) 
        
        TotalList1.append(int(row[1]))
        TotalList2.append(row[0])
        Data1 = TotalList1
        Data2 = TotalList2
        
       
    for i in range(len(TotalList1)-1):
        change.append (TotalList1[i+1] - TotalList1[i])
        changemonths.append (TotalList2[i])

    # print(change)
    # print(changemonths)
    Mean = sum(change) / len(change)

    
    print(f"Total Months: {TotalMonths}")
    print(f"Total: {Total}")
    print(f"Average Change: {Mean}")
    # print(f"Greatest Increase: {}")
    # print(f"Greatest Decrease: {}")
    
    
    # Total Months: 86
    # Total: $38382578
    # Average  Change: $-2315.12
    # Greatest Increase in Profits: Feb-2012 ($1926159)
    # Greatest Decrease in Profits: Sep-2013 ($-2196167)


   