#sort an array
'''
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.


'''






# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         if len(nums) > 1:
#             left_nums = nums[:len(nums)//2]
#             right_nums = nums[len(nums)//2:]
#             #recursion
#             self.sortArray(left_nums)
#             self.sortArray(right_nums)

#             #merge
#             i = 0 #left_arr index
#             j = 0 #right_arr index
#             k = 0 #merge_arr index

#             while i < len(left_nums) and j < len(right_nums):
#                 if left_nums[i] < right_nums[j]:
#                     nums[k] = left_nums[i]
#                     i += 1
#                 else:
#                     nums[k] = right_nums[j]
#                     j += 1
#                 k += 1

#             while i < len(left_nums):
#                 nums[k] = left_nums[i]
#                 i += 1
#                 k += 1

#             while j < len(right_nums):
#                 nums[k] = right_nums[j]
#                 j += 1
#                 k += 1
#         return nums