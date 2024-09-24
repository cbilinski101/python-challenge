# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
budget_data_csv = os.path.join('resources', 'budget_data.csv')  # Input file path
budget_analysis_txt = os.path.join('analysis', 'budget_analysis.txt')  # Output file path

# Define variables to track the financial data
month_list = []
profitloss_list = []
average_change_list = []
column_values = []
differences = []

# Open and read the csv, 
with open(budget_data_csv,'r') as financial_data:
    csvreader = csv.reader(financial_data, delimiter=',')
    
    # Skip the header row
    header = next(csvreader, None)

    # Extract first row to avoid appending to net_change_list
    row = next(csvreader, None)

    month = row[0]
    month_list.append(month)
    profitloss = int(row[1])
    profitloss_list.append(profitloss)
    average_change = int(row[1])
    average_change_list.append(average_change)
   
    column_values.append (int(row[1]))  # Convert to float if necessary

    for row in csvreader:
        month = row[0]
        month_list.append(month)
        profitloss = int(row[1])
        profitloss_list.append(profitloss)
        average_change = int(row[1])
        average_change_list.append(average_change)
        column_values.append (int(row[1]))  # Convert to float if necessary

# Calculate the differences
for i in range(1, len(column_values)):
    difference = column_values[i] - column_values[i - 1]
    differences.append(difference)

# Process each row of data
months= len(month_list)
profitloss = sum(profitloss_list)
average_change = round((profitloss_list[-1]/85)-(profitloss_list[0]/85), 2)
great_inc = max(differences)
great_dec = min(differences)

# Print the results
print('Financial Analysis')
print('---------------------------')
print('Total Months:',months)
print(f"Total: ${profitloss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: (${great_inc})")
print(f"Greatest Decrease in Profits: (${great_dec})")

# Write the results to a text file
with open(budget_analysis_txt, 'w') as f:
    f.write('Financial Analysis')
    f.write("\n")
    f.write('---------------------------')
    f.write("\n")
    f.write(f"Total Months: {months}")
    f.write("\n")
    f.write(f"Total: ${profitloss}")
    f.write("\n")
    f.write(f"Average Change: ${average_change}")
    f.write("\n")
    f.write(f"Greatest Increase in Profits: (${great_inc})")
    f.write("\n")
    f.write(f"Greatest Decrease in Profits: (${great_dec})")


