# class Solution:
#     def arrangeCoins(self, n: int) -> int:
#         i = 0
#         while n >= 0:
#             i +=1
#             n = n-i
#         return i-1


n = 5
res = 0  # Represents the number of complete rows
i = 1       # Row counter, where each row i requires i coins

while n >= i:
    n -= i      # Deduct the coins needed for the current row
    res += 1 # Increment complete rows count
    i += 1      # Move to the next row

print(res)   # Output the number of complete rows

n = 5
res = 0  # Keeps track of the number of complete rows

# Loop through rows, where each row `i` requires `i` coins
for i in range(1, n + 1):
    if n >= i:       # Check if there are enough coins for row `i`
        n -= i       # Deduct `i` coins for this row
        res += 1  # Count the row as complete
    # else:
        # break        # Exit if there are not enough coins for the next row

print(res)  # Output the number of complete rows


n = 5
i =  1
res = 0
for j in range(1,n+1):
    if j == i and n >= i:
        res += 1
        n -= 1
print(res)