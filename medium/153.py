# nums = [4,5,6,7,0,1,2]
nums = [4,3]
l = 0
r = len(nums)-1
# m = (l+r)//2 # 3
# print(m)
res = nums[0]
while l <= r:
    if nums[l] < nums[r]:
        res = min(res,nums[l])
        break
    #print(res)

    m = (l+r)//2 # 3
    res = min(res,nums[m])
    if nums[m] >= nums[l]:
        l = m+1
    else:
        r -= 1

print(res)
# print(nums[res])
# print(2//2)