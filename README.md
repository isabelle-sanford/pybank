# pybank

This is a Python script for analyzing financial records. The dataset in budget_data.csv has two columns: Date and Profit/Losses. This script uses that data to produce an output (both a print statement and a text file) comprising of:
* The total number of months
* The net total of Profit/Losses over the entire period
* The average month-to-month change in Profit/Losses 
* The greatest increase and greatest decrease in profits (date and amount)

When run on this particular set of data, the output should look as follows:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

This was part of Assignment 3 for the USC Viterbi Boot Camp (Python unit). 
