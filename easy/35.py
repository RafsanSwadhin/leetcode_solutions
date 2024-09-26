nums = [1,3,5,6,8,9,13]
target = 5
l,r = 0,len(nums)-1
while l <= r:
    mid = (l+r)//2
    if target == nums[mid]:
        print(mid)
        break
    if target < nums[mid]:
        r = mid -1
    else:
        l = mid +1
print(mid)