nums = [2,3,1,2,4,3]
target = 7
l = 0
count = 0
min_len = float('inf')
for r in range(len(nums)):
    count += nums[r]
    # min_len = min(min_len,count)
    while count >= target:
        min_len = min(min_len,r-l+1)
        count -= nums[l]
        l += 1
print(min_len)  if min_len < float('inf') else print(0)