
# MOST RECENT
import csv

# open file and extract data in list
with open("budget_data.csv", "r") as f:
    budgetdata = csv.reader(f)
    header = next(budgetdata)
    lines = list(budgetdata)
#print(lines[0])

# split each line into month & num
lists = list(zip(*lines))
months = lists[0]
profits = [int(x) for x in lists[1]]

# def prev(value, list1):
#     index = list1.index(value)
#     return int(list1[index - 1])

# list of change month-by-month
# net_change = []
# for k in range(1, len(profits)):
#     net_change.append(profits[k] - profits[k-1])

# net_change = [(int(k) - prev(k, profits)) for k in profits]
net_change = [(profits[k] - profits[k - 1]) for k in range(len(profits))]

# Variables we want
num_months = len(lines) # what about if empty spaces?
net_total = sum(profits)
avg_change = sum(net_change) / len(net_change) # mean function? numpy?

max_increase = lines[net_change.index(max(net_change)) + 1]
max_decrease = lines[net_change.index(min(net_change)) + 1] 

# write output string
final_output = ("Financial Analysis: \n" +
        f"Total Months: {num_months}\n" +
        f"Total: ${net_total}\n" +
        f"Average Change: ${avg_change}\n" +
        f"Biggest Increase: {max_increase[0]} (${max_increase[1]})\n" +
        f"Biggest Decrease: {max_decrease[0]} (${max_decrease[1]})")

# print output
print(final_output)

# write output to text file
with open("analysis.txt", "w", newline = "") as analysis:
    analysis.write(final_output)