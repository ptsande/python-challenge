#import csv
import os
import csv

max_profit = []
max_loss = []

#define path to resource
budget_data = os.path.join('budget_data.csv')

# open file
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
    #total of months = total rows
    for row in csvreader:
        month_total = sum(1 for row in csvreader)
    print(month_total)

with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    #total net amount
    total = 0
    #csvfile.seek(0)
    for row in csvreader:
        total += int(row[1])
    print(total)