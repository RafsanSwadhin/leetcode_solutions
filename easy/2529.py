# 2529. Maximum Count of Positive Integer and Negative Integer
from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        p = 0
        n = 0
        for i in nums:
            if i > 0:
                p += 1
            elif i < 0:
                n += 1
        return max(p, n)
