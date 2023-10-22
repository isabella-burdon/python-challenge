# import pandas package
# Your task is to create a Python script that analyses the records to calculate each of the following values:

    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in profits (date and amount) over the entire period

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
import pandas as pd

# save file paths as variables
in_path = "Starter_Code/PyBank/Resources/budget_data.csv"
out_path = "Output/financial_analysis.txt"

# read in data
df_budget = pd.read_csv(in_path)
df_budget.tail()

# Your analysis should align with the following results:

    # Financial Analysis
    # ----------------------------
    # Total Months: 86
    # Total: $22564198
    # Average Change: $-8311.11
    # Greatest Increase in Profits: Aug-16 ($1862002)
    # Greatest Decrease in Profits: Feb-14 ($-1825558)

# The total number of months included in the dataset
total_months = len(df_budget['Date'].unique())

# The net total amount of "Profit/Losses" over the entire period
total = df_budget['Profit/Losses'].sum()

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
delta_list = []
for i in range(len(df_budget['Profit/Losses']) - 1):
    delta = df_budget['Profit/Losses'].iloc[i + 1] - df_budget['Profit/Losses'].iloc[i]
    delta_list.append(delta)
average_delta = sum(delta_list) / len(delta_list)

# The greatest increase in profits (date and amount) over the entire period
max_delta = max(delta_list)
date_max_delta = df_budget['Date'].iloc[delta_list.index(max_delta) + 1]

# Greatest Decrease in Profits: Feb-14 ($-1825558)
min_delta = min(delta_list)
date_min_delta = df_budget['Date'].iloc[delta_list.index(min_delta) + 1]

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