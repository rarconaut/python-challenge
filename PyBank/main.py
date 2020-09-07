
## Import the dependencies needed to read/write csv
import os
import csv

## define the csv path
pybank_csv = os.path.join("Resources", "budget_data.csv")

# define the function and accept 'budget_data' as its parameter
def print_analysis(budgetData):

    # variables to store the data
    date = str(budgetData[0])
    profit_loss = float(budgetData[1])
    profits = []
    losses = []
    greatest_inc = 0
    greatest_des = 0

## reading the budget_data.csv file into Python
with open(pybank_csv, 'r') as csvfile:
    budgetData = csv.reader(csvfile, delimiter=',')
    
    # defining the header
    header = next(budgetData)

   #=========================================# 
       
    # Your task for PyBank is to create a Python script that analyzes the records to calculate each of the 
    # following:

    # The total number of months included in the dataset
    ## total months is equal to the number of rows (minus the header)
    total_months= len(list(budgetData))
    print(f'Total number of months = {total_months}')

    for row in budgetData:
        # The net total amount of "Profit/Losses" over the entire period
        ## net_total = sum(Profits) - sum(Losses)
        if row[1] > 0:
            profits.append(row[1])
        elif row[1] < 0:
            losses.append(row[1])
            

        # The average of the changes in "Profit/Losses" over the entire period
        ## avg_change = (sum of differences month to month)/total months


        # The greatest increase in profits (date and amount) over the entire period
        if row > greatest_inc:
            greatest_inc = row
            print(f'The greatest increase in profits was {greatest_inc} and occured in {date}.')

        # The greatest decrease in losses (date and amount) over the entire period
        if row < greatest_dec:
            greatest_dec = row
            print(f'The greatest decrease in losses was {greatest_dec} and occured in {date}.')

# In addition, your final script should both print the analysis to the terminal and export a text file 
# with the results.

