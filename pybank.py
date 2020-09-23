import csv

# open file and extract data in array
file1 = open("budget_data.csv", "r")
lines = []

for x in file1:
    lines.append(x)

file1.close()

# # split each line into month & num, take out '\n'
for i in range(len(lines)):
    pair = lines[i].split(",")
    if len(pair) > 1:
        pair[1] = pair[1][:-1]

    lines[i] = pair



# split up lists for easier use
months = []
profits = []
for j in range(1,len(lines)):
    months.append(lines[j][0])
    profits.append(int(lines[j][1]))

# list of change month-by-month
net_change = []
for k in range(1, len(profits)):
    net_change.append(profits[k] - profits[k-1])


# Variables we want
num_months = len(lines) # what about if empty spaces?
net_total = sum(profits)
avg_change = sum(net_change) / len(net_change) # mean function? numpy?

max_increase = net_change.index(max(net_change))
max_decrease = net_change.index(min(net_change)) # need to translate these back to lines1 pair

max_increase_pair = lines[max_increase + 1] # according to answers should be +2. Why?
#print(max_increase_pair)

final_output = "Financial Analysis: \n" 
final_output += "Total Months: " + str(num_months) + "\n"
final_output += "Total: " + str(net_total) + "\n"
final_output += "Average Change: " + str(avg_change) + "\n"
final_output += "Max min stuff"

print(final_output)