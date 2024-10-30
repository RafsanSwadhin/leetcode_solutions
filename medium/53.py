nums = [-2,1,-3,4,-1,2,1,-5,4]
max_sum = nums[0]
curr_sum = 0
for i in nums:
    if curr_sum < 0:
        curr_sum = 0
    curr_sum += i
    max_sum = max(max_sum,curr_sum)
print(max_sum)