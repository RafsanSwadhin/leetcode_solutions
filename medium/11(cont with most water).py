# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         left = 0
#         right = len(height)-1
#         res =  0
#         while left < right :
#             w = right-left
#             l = min(height[left],height[right])
#             area = w*l
#             res = max(res,area)
#             if height[left] < height[right]: 
#                 left +=1
#             else:
#                 right -= 1
#         return res
