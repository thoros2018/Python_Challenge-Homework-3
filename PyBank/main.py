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
    #Change = []
        
    Total = 0
    TotalMonths = 0
        
    for row in csvreader:
        TotalMonths = TotalMonths + 1
        Total = Total + int(row[1]) 
        # /Total2 = Total + int(row[1])-1
    
    for
                
        Mean = Total / 86
        #Greatest = max(Total)
        #Least = min(Total)

        TotalMonthList.append(row[0])
        TotalList1.append(row[1])
        TotalList2.append(row[0])
        Data1 = TotalList1
        Data2 = TotalList2
        x = list(enumerate(Data1))
        y = list(enumerate(Data2)) 
        
        
    print('\n') 
    print("Enumerator: Total")
    print(x)
    print('\n')
    print("Enumerator: Total Months")
    print(y)
    print('\n')
    print(f"Total Months: {TotalMonths}")
    print(f"Total: {Total}")
    # print(f"Total: {Total2}")
    print('\n')
    print(f"Average Change: {Mean}")
    # print(f"Change: {Total2}")

    
    # Total Months: 86
    # Total: $38382578
    # Average  Change: $-2315.12
    # Greatest Increase in Profits: Feb-2012 ($1926159)
    # Greatest Decrease in Profits: Sep-2013 ($-2196167)


    #Store all the text inside a variable called "lines"
    #lines = csv.read()

    #Print the contents of the text file
    #print(lines)

    ##import file with 5 entries to test
    #counter row counter
    #previous row counter
