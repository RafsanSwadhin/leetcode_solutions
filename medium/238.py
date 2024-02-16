#238. Product of Array Except Self


from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

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

        return resul_list
