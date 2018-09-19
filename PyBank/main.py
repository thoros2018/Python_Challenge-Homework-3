import csv

with open('Resources/budget_data.csv', 'r') as csv_file:
    
    budgetData = csv.reader(csv_file)
    
    for line in budgetData:
        print(line)
        
