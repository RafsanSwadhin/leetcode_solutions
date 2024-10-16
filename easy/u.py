'''
nums = [1,1,1,2,2,3]
count =[]
l = 0
for i in range(len(nums)):
    if i == nums[0]:
       no = nums.count(i)
       count.append(no)
    if i == nums[no-1]:
        no_1 = nums.count(i)
        count.append(no_1)
           

print(no)
print(no_1)
print(count)
'''
from collections import Counter

k = 2
nums = [1, 1, 1, 2, 2, 3]
count = Counter(nums)

# Extract the counts and convert them into a list
count_list = list(count.values())

# Sort the count_list in descending order
count_list.sort(reverse=True)

# Print the top k most frequent numbers as a list
print(count_list[:k])




n = "the sky is blue"
new_n = n.split()  # ['the', 'sky', 'is', 'blue']
left = 0
right = len(new_n) - 1

# Loop to reverse the list
while left < right:
    # Swap the elements at 'left' and 'right' indices
    new_n[left], new_n[right] = new_n[right], new_n[left]
    left += 1
    right -= 1

print(new_n)
