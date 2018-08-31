#import csv
import os
import csv

max_profit = []
max_loss = []
revenue = []

#I need to create a dictionary that will allow me to store a key value pair.
#date is the key and profit loss is the value

#define path to resource
budget_data = os.path.join('budget_data.csv')

# open file
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        month_total = sum(1 for row in csvreader)
    print(month_total)
    csvfile.seek(0)
    next(csvreader)
    total = 0
    for row in csvreader:
        total += int(row[1])
    print(total)
    csvfile.seek(0)
    next(csvreader)
    for row in csvreader:
        maxprofit = max(row[1])
    print(maxprofit)