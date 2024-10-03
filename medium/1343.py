arr = [2,2,2,2,5,5,5,8]
#arr = [11,13,17,23,29,31,7,5,2,3]
k = 3
threshold = 4
n = threshold*k
cur= sum(arr[:k]) #6
if cur >= n:
    count = 1
else:
    count = 0
for i in range(k,len(arr)):
    cur = cur +arr[i]-arr[i-k]
    if cur >= n :
        count = count+ 1


print(count)
