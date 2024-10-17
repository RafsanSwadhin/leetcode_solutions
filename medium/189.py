nums = [1,2,3,4,5,6,7]
# k = 3
# left_k = 0
# right_k = (-1)*k
# # print(nums[-3]) 5
# while left_k < k:
#     nums[left_k],nums[right_k] = nums[right_k],nums[left_k]
#     left_k +=1
#     right_k +=1

# print(nums)

nums = [1,2,3,4,5,6,7]
k = 3
k = k%len(nums)
l,r = 0, len(nums)-1

while l < r:
    nums[l],nums[r] = nums[r],nums[l]
    l +=1
    r -=1

print(nums)

l,r = 0, k-1

while l < r:
    nums[l],nums[r] = nums[r],nums[l]
    l +=1
    r -=1
print(nums)

l,r = k, len(nums)-1

while l < r:
    nums[l],nums[r] = nums[r],nums[l]
    l +=1
    r -=1
print(nums)

