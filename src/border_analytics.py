import csv
import sys

# Open input csv file
f = open(sys.argv[1])
csv_f = csv.reader(f)
inputDict = {}
# Use flag to avoid table header
flag = 1

for row in csv_f:
    # Extract 'Border', 'Date',' Measure' from each entry
    if flag:
        flag = 0
        continue
    temp = tuple([row[3], row[4], row[5]])
    num = int(row[6])
    # Sum up the total value for each category
    if temp in inputDict:
        inputDict[temp] += num
    else:
        inputDict[temp] = num

lst = []
for key, value in inputDict.items():
    lst.append([key[0], key[1], key[2], value, 0])

# x[0]: Border; x[1]: Date; x[2]: Measure; x[3]: Value
sortedlst = sorted(lst, key = lambda x : (x[1], x[3], x[2], x[0]))

# Calculate moving average for all previous months
avgDict = {}
for item in sortedlst:
    temp2 = tuple([item[0], item[2]])
    # avgcnt = [item[3], 0]
    if temp2 in avgDict:
        item[4] =  round(avgDict[temp2][0] / avgDict[temp2][1], 0)
        avgDict[temp2] = [(item[3] +  avgDict[temp2][0]), avgDict[temp2][1] + 1]
    else:
        # Python3 always rounds x.5 to the nearst even number (like 2.5 to 2). Therefore a small residue is added to the total value before calculating the average
        avgDict[temp2] = [item[3] + 1e-10, 1]

sortedlst = sorted(lst, key = lambda x : (x[1], x[3], x[2], x[0]), reverse = True)

# Add header line
results = [['Border', 'Date', 'Measure', 'Value', 'Average']]
for res in sortedlst:
    res[-1] = round(res[-1])
    results.append(res)

with open(sys.argv[2], "w", newline = '') as f:
    cw = csv.writer(f)
    cw.writerows(r for r in results)