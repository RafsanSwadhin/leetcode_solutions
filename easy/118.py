s = 4
res = [[1]]
for i in range(s-1):
    temp = [0]+res[-1]+[0]
    row = []
    for j in range(len(res[-1])+1):
        row.append(temp[j]+temp[j+1])
    res.append(row)
print(res)

for i in range(1):
    print("jkfjdkjf")