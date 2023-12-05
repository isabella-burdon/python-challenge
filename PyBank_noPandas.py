# save file paths as variables
in_path = "Starter_Code/PyBank/Resources/budget_data.csv"
out_path = "Output/financial_analysis.txt"

# read in data
with open(in_path, 'r') as file:
    # Assuming the first row is the header
    header = file.readline().strip().split(',')
    data = [line.strip().split(',') for line in file]

# Your analysis should align with the following results:

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)

# The total number of months included in the dataset
total_months = len(set(row[header.index('Date')] for row in data))

# The net total amount of "Profit/Losses" over the entire period
total = sum(int(row[header.index('Profit/Losses')]) for row in data)

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
delta_list = [int(data[i + 1][header.index('Profit/Losses')]) - int(row[header.index('Profit/Losses')]) for i, row in enumerate(data[:-1])]
average_delta = sum(delta_list) / len(delta_list)

# The greatest increase in profits (date and amount) over the entire period
max_delta = max(delta_list)
date_max_delta = data[delta_list.index(max_delta) + 1][header.index('Date')]

# Greatest Decrease in Profits: Feb-14 ($-1825558)
min_delta = min(delta_list)
date_min_delta = data[delta_list.index(min_delta) + 1][header.index('Date')]

output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total}
Average Change: ${round(average_delta, 2)}
Greatest Increase in Profits: {date_max_delta} (${max_delta})
Greatest Decrease in Profits: {date_min_delta} (${min_delta})
"""

print(output)

with open(out_path, "w") as file:
    file.write(output)
