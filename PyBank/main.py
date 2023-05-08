# import modules

import os
import csv

# navigating to correct directory

os.chdir('/Users/eimaanejaz/Desktop/GitHub/python-challenge/PyBank')
csvpath = os.path.join(".", "Resources", "budget_data.csv")

# opening csv file

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
 # changing data to list format
    data = list(csvreader)
 # defining total month variable
  # -1 from total to exclude header in count
    total_months = len([i[0] for i in data])-1
 # printing total months
    print(total_months)
