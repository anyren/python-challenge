# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#expected output:
'''
Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
'''

import os
import csv

month = []
profit = []
profit_change = []
row_count = 0
num_months = 0
total = 0

filepath = os.path.join("Resources", "budget_data.csv")

# read file and create separate lists for month, profit, and profit change
with open(filepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        current_profit =int(row[1])
        if row_count == 0:
            previous_month = current_profit
        month.append(row[0])
        profit.append(current_profit)
        profit_change.append(current_profit - previous_month)
        previous_month = current_profit
        row_count += 1

# zip into new dataset
data = zip(month, profit, profit_change)

# all the counters
change_total = 0
increase_profit = 0
decrease_profit = 0

# calculate/assign values
for row in data:
    month = row[0]
    profit = row[1]
    profit_change = row[2]
    total += profit
    change_total += profit_change
    if profit_change > increase_profit:
        increase_profit = profit_change
        increase_profit_month = month
    if profit_change < decrease_profit:
        decrease_profit = profit_change
        decrease_month = month
month_count = row_count

# create output
output =[]
analysis_file = os.path.join("analysis", 'financial_analysis.txt')
output.append("Financial Analysis")
output.append("----------------------------")
output.append(f'Total Months: {month_count}')
output.append(f'Total: ${total}')
output.append(f'Average Change: ${round(change_total/(month_count-1),2)}')
output.append(f'Greatest Increase in Profits: {increase_profit_month} (${increase_profit})')
output.append(f'Greatest Decrease in Profits: {decrease_month} (${decrease_profit})')

# print output to screen and write to analysis_file
with open(analysis_file, 'w') as f:
    for row in output:
        print(row)
        f.write(row)
        f.write('\n')