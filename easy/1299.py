'''

arr = [17, 18, 5, 4, 6, 1]
res = []

for i in range(1,len(arr)):
    max_val = max(arr[i:])  # Find the maximum of the remaining sublist
    res.append(max_val)

print(res+[-1])

'''


#arr = [17, 18, 5, 4, 6, 1]
arr = [1]
res = []
max_val = -1  # Start with -1 as the last element should be -1

# Traverse the array from right to left
for i in range(len(arr)-1, -1, -1):
    res.append(max_val)
    max_val = max(max_val, arr[i])  # Update the maximum value

# Since we traversed from right to left, reverse the result
res.reverse()

print(res)

