# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         count = 0
#         n = len(nums)
#         for i in range(k):
#             count += nums[i]
#         max_avg = count/k

#         for i in range(k,n):
#             count += nums[i]
#             count -= nums[i-k]
#             avg = count/k
#             max_avg = max(avg,max_avg)
#         return max_avg