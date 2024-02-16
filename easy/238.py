'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        k = []

        total_product = 1
        for num in nums:
            total_product *= num

        for num in nums:
            s = total_product // num
            k.append(s)
 
        return k        

'''
'''
nums = [1,0,2,3,4]

cc = []*len(nums)
xx = 1
for i in range(len(nums)-1,-1,-1):

    if i == 0:
        nums.remove(0)
        bb = 1
    for i in range(len(nums)):
        bb *=nums[i]
    else:


        nums.remove(nums[i])
        xx *=nums[i]


print(nums)
print(bb)
'''

'''

nums = [1, 0, 2, 3, 4]

cc = [0] * len(nums)  # Corrected list initialization
xx = 1

for i in range(len(nums) - 1, -1, -1):
    if nums[i] == 0:
        nums.remove(0)
        bb = 1
    else:
        xx *= nums[i]

for i in range(len(nums)):
    bb *= nums[i]

print("Modified List:", nums)
print("Product without zeros:", bb)


'''
nums = [0,0]

resul_list = [0] * len(nums)  # Initialize with zeros

res = 1

if 0 not in nums:
    for i in nums:
        res *= i

    j = 0
    for i in nums:
        resul_list[j] = res // i
        j += 1

else:
    if nums.count(0) >= 2:
        resul_list = [0] * len(nums)  # If there are two or more zeros, set all elements to 1

    elif nums.count(0) == 1:
        for i in range(len(nums)):
            if nums[i] != 0:
                res *= nums[i]

        zero_index = nums.index(0)
        resul_list[zero_index] = res  # If there is exactly one zero, set its index to the product of non-zero elements

print(resul_list)





