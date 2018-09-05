import os
import csv
#define lists
profits = []
losses = []
dates = []
revenues = []
monthly_change = []

#define path to resource
budget_data = os.path.join('budget_data.csv')

# open file
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
# Define total number of months in file
    for row in csvreader:
        month_total = sum(1 for row in csvreader)
        new_month_total = (f"Total Months: " + str(month_total))
    print(f"Total Months: " + str(month_total))
    csvfile.seek(0)
    next(csvreader)
# Define total profit in file
    total = 0
    for row in csvreader:
        total += int(row[1])
        new_total = (f"Total: $" + str(total))
    print(f"Total: $" + str(total))
    csvfile.seek(0)
    next(csvreader)
# find average change - need to figure out how to compare corresponding values
    #for row in csvreader:
        
# find largest gain and largest lost    
    for row in csvreader:
        dates.append(str(row[0]))
        revenues.append(int(row[1]))
        max_profit = max(revenues)
        #print(max_profit)
        max_loss = min(revenues)
        #print(max_loss)
        max_profit_loc = revenues.index(max_profit)
        #print(max_profit_loc)
        max_loss_loc = revenues.index(max_loss)
        #print(max_loss_loc)
        max_loss_date = dates[max_loss_loc]
        #print(max_loss_date)
        max_profit_date = dates[max_profit_loc]
        new_max = (f"Greatest Increase in Profits: $" + str(max_profit) + " on " + str(max_profit_date))
        new_loss = (f"Greatest Decrease in Profits: $" + str(max_loss) + " on " + str(max_loss_date))
    #print(f"Greatest Increase in Profits: $" + str(max_profit) + " on " + str(max_profit_date))
    print(new_max)
    #print(f"Greatest Decrease in Profits: $" + str(max_loss) + " on " + str(max_loss_date))
    print(new_loss)
    csvfile.seek(0)
    next(csvreader)
    output_path = os.path.join("final_budget_data.csv")
    with open(output_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow([new_month_total])
        csvwriter.writerow([new_total])
        csvwriter.writerow([new_max])
        csvwriter.writerow([new_loss])



