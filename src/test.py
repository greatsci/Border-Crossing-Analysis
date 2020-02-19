import csv
f = open("C:/Users/ningz/Documents/GitHub/NingZhang2020/insight_testsuite/tests/test_1/input/Border_Crossing_Entry_Data.csv")
csv_f = csv.reader(f)
myDict = {}
# Use flag to avoid title line
flag = 1
for row in csv_f:
    # Extract 'Border', 'Date',' Measure' information from each entry
    if flag:
        flag = 0
        continue
    temp = tuple([row[3], row[4], row[5]])
    num = int(row[6])
    # print((temp))
    if temp in myDict:
        myDict[temp] += num
    else:
        myDict[temp] = num
# print(myDict)

lst = []
for key, value in myDict.items():
    lst.append([key[0], key[1], key[2], value])

sortedlst = sorted(lst, key = lambda l:l[1], reverse = True)
print(lst)
print(sortedlst)
