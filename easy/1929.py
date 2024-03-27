nums = [1,2,1]
n = nums.copy()

for i in range(len(nums)):
    n.append(nums[i])

print(nums + nums)