# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.
 

# Example 1:

# Input: s = "abcde", goal = "cdeab"
# Output: true
# Example 2:

# Input: s = "abcde", goal = "abced"
# Output: false
 

# class Solution:
#     def rotateString(self, s: str, goal: str) -> bool:
#         if goal == s[::-1] or len(s) != len(goal):
#             return False
#         return goal in s + s
