import csv

with open('Resources\election_data.csv', 'r') as csv_file:
    
    elecData = csv.reader(csv_file)
    
    for line in elecData:
        print(line)
        
