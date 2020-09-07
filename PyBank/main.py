
## Import the dependencies needed to read/write csv
import os
import csv

## define the csv path
pybank_csv = os.path.join("Resources", "budget_data.csv")

# define the function and accept 'budget_data' as its parameter
def print_analysis(budgetData):

    # variables to store the data
    month = budgetData[0]
    total_months= len(list(budgetData))
    net_total = float(budgetData[1])
    avg_change = float()
    greatest_inc = float()
    greatest_dec = float()

## reading the budget_data.csv file into Python
with open(pybank_csv, 'r') as csvfile:
    budgetData = csv.reader(csvfile, delimiter=',')

    # defining the header
    header = next(budgetData)
  
    
       
    # Your task for PyBank is to create a Python script that analyzes the records to calculate each of the 
    # following:

    # The total number of months included in the dataset
    
    print(total_months)

    # The net total amount of "Profit/Losses" over the entire period


    # The average of the changes in "Profit/Losses" over the entire period


    # The greatest increase in profits (date and amount) over the entire period


    # The greatest decrease in losses (date and amount) over the entire period


# In addition, your final script should both print the analysis to the terminal and export a text file 
# with the results.

