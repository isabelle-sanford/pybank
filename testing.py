
# MOST RECENT
import csv

# open file and extract data in list
with open("budget_data.csv", "r") as f:
    budgetdata = csv.reader(f)
    header = next(budgetdata)
    lines = list(budgetdata)

# split each line into month & num
lists = list(zip(*lines))
months = lists[0]
profits = [int(x) for x in lists[1]]


net_change = [int(profits[k] - profits[k - 1]) for k in range(1, len(profits))]

avg_change = sum(net_change) / len(net_change) 





max_increase = lines[net_change.index(max(net_change))]
max_decrease = lines[net_change.index(min(net_change))] 

# write output string
final_output = ("Financial Analysis: \n" +
        f"Total Months: {num_months}\n" +
        f"Total: ${net_total}\n" +
        f"Average Change: ${avg_change}\n" +
        f"Biggest Increase: {max_increase[0]} (${max(net_change)})\n" +
        f"Biggest Decrease: {max_decrease[0]} (${min(net_change)})")

# print output
print(final_output)


# write output to text file
with open("analysis.txt", "w", newline = "") as analysis:
    analysis.write(final_output)

print(net_total / 86)

# change_change = [(net_change[p] - net_change[p-1]) for p in net_change]
# print(change_change)