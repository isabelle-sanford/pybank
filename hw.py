import csv

# open file and extract data in list
with open("budget_data.csv", "r") as f:
    budgetdata = csv.reader(f)
    lines = list(budgetdata)
#print(lines[0])

# split each line into month & num
lists = list(zip(*lines))
months = lists[0][1:]
profits = lists[1][1:]

def prev(value, list1):
    index = list1.index(value)
    return list1[index - 1]

# list of change month-by-month
# net_change = []
# for k in range(1, len(profits)):
#     net_change.append(profits[k] - profits[k-1])

net_change = [(k - prev(k, profits)) for k in profits]


# Variables we want
num_months = len(lines) # what about if empty spaces?
net_total = sum(profits)
avg_change = sum(net_change) / len(net_change) # mean function? numpy?

max_increase = lines[net_change.index(max(net_change)) + 1]
max_decrease = lines[net_change.index(min(net_change)) + 1] 

# max_increase_pair = lines[max_increase + 1] # according to answers should be +2. Why?
# #print(max_increase_pair)

print(f"Financial Analysis: ",
        "Total Months: {num_months}", 
        "Total: {net_total}",
        "Average Change: {avg_change}",
        "Biggest Increase: {max_increase}",
        "Biggest Decrease: {max_decrease}")

# final_output = "Financial Analysis: \n" 
# final_output += "Total Months: " + str(num_months) + "\n"
# final_output += "Total: " + str(net_total) + "\n"
# final_output += "Average Change: " + str(avg_change) + "\n"
# final_output += "Biggest increase: "

# print(final_output)