# import modules
import os
import csv

# navigating to correct directory
os.chdir('/Users/eimaanejaz/Desktop/GitHub/python-challenge/PyBank')
# defining path for source file
csvpath = os.path.join(".", "Resources", "budget_data.csv")
# defining path for output file
txtpath = os.path.join(".", "analysis", "financial_analysis.txt")

# assigning initial values to variables
total_months = 0
net_profitloss = 0
prev_profitloss = 0
 # creating empty list variable to store the changes in profit/loss from one month to the next
changes = []
 # creating empty dictionaries to store greatest increase and decrease values
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}

# opening csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # ignoring headers
    next(csvreader)

    # looping through each row in budget data
    for row in csvreader:

        # adding 1 to total number of months for each row in dataset
        total_months += 1

        # adding the profit/loss to net total
        net_profitloss += int(row[1])

        # defining profit/loss for current month
        current_profitloss = int(row[1])
        # from month 2 onwards (since no previous month for month 1)
        if total_months > 1:
            # calculate change in profit/loss from previous value
            change = current_profitloss - prev_profitloss
            # add change to to changes list
            changes.append(change)

            # checking if the change is the greatest increase
            if change > greatest_increase["amount"]:
                # adding to greatest increase dictionary
                greatest_increase["date"] = row[0]
                greatest_increase["amount"] = change
              # checking if the change is the greatest decrease  
            elif change < greatest_decrease["amount"]:
                # adding to greatest decrease dictionary
                greatest_decrease["date"] = row[0]
                greatest_decrease["amount"] = change

        # moving to next iteration
        prev_profitloss = current_profitloss

# calculating average change using changes list
average_change = sum(changes) / len(changes)

# formatting results list
results = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_profitloss}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
)

# printing results to terminal
print(results)

# printing results to output file
with open(txtpath, "w") as financial_analysis:
    financial_analysis.write(results)
    