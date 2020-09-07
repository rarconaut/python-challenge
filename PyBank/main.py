
## Import the dependencies needed to read/write csv
import os
import csv

## define the csv path
pybank_csv = os.path.join("Resources", "budget_data.csv")

# define the function and accept 'budget_data' as its parameter
def print_analysis(budgetData):

    # variables to store the data
    date = str(budgetData[0])
    profit/loss = float(budgetData[1])

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

    # The net total amount of "Profit/Losses" over the entire period
    ## net_total = Profit - totalLoss

    # The average of the changes in "Profit/Losses" over the entire period
    ## avg_change = sum of differences month to month/total months

    # The greatest increase in profits (date and amount) over the entire period
    greatest_inc =

    # The greatest decrease in losses (date and amount) over the entire period
    greatest_dec =

# In addition, your final script should both print the analysis to the terminal and export a text file 
# with the results.

