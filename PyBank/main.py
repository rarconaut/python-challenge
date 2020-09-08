
## Import the dependencies needed to read/write csv
import os
import csv

## define the csv path
pybank_csv = os.path.join("Resources", "budget_data.csv")

# define the function and accept 'budget_data' as its parameter
def print_analysis(budgetData):

    ## variables to store the data
    date = none
    #profit_loss = float(budgetData[1])
    
    net_total = 0.0
    greatest_inc = 0.0
    greatest_des = 0.0

## reading the budget_data.csv file into Python
with open(pybank_csv, 'r') as csvfile:
    budgetData = csv.reader(csvfile, delimiter=',')
    
    # defining the header
    header = next(budgetData)
    profits = []
    losses = []
   #=========================================# 
       
    # Your task for PyBank is to create a Python script that analyzes the records to calculate each of the 
    # following:

    # The total number of months included in the dataset
    ## total months is equal to the number of rows (minus the header)
    total_months = len(list(budgetData))
   

    for row in budgetData:
        # The net total amount of "Profit/Losses" over the entire period
        ## I need to convert the string numbers read from the csv into floats/integers to use them in the calculations. Python tells me
        ## that I can't convert an entire list, so I'm converting each value as the function iterates through the rows, and adding them 
        ## to either the 'profits' or 'losses' lists, according to their appropriate IF statements.
        ## Net Total = Profits - Losses
        if float(row[1]) >= 0:
            # print(row)
            profit = float(row[1])
            profits.append(profit)

        elif float(row[1]) < 0:
            # print(row[1])
            loss = float(row[1])
            losses.append(loss)

        # print(profit) #This part works correctly, and outputs a list of all profits as floats
        # print(losses) #This prints a complicated mess, and I can't figure out what the issue is - it works on a set of simple test figures and it's formatted the same way as the 'profits' list. 

        net_total = sum(profits) - sum(losses)
        

        # The average of the changes in "Profit/Losses" over the entire period
        ## avg_change = (sum of differences month to month)/total months



        # The greatest increase in profits (date and amount) over the entire period
        if float(row[1]) > greatest_inc:
            greatest_inc = float(row[1])
            date = row[0]
            

        # The greatest decrease in losses (date and amount) over the entire period
        if float(row[1]) < greatest_dec:
            greatest_dec = float(row[1])
            date = row[0]
           
#-----------------------------------------#
## The Statistical Report output
print(f'Total number of months = {total_months}')
print(f'The Net Total of Profit/Losses over the period was {net_total}.')
print(f'The Average Change of Profit/Losses over the period was {avg_change}.')
print(f'The greatest increase in profits was {greatest_inc} and occured in {date}.')
print(f'The greatest decrease in losses was {greatest_dec} and occured in {date}.')

# In addition, your final script should both print the analysis to the terminal and export a text file 
# with the results.

# Set variable for output file
output_file = os.path.join("analysis", "PyBank_analysis.txt")

#  Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)