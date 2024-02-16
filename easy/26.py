from collections import Counter
from typing import List
a = [1, 1, 1, 2, 2, 3, 4, 5]
b = [a[0]]
for i in range(1, len(a)):
    if a[i] != a[i - 1]:
        b.append(a[i])

print(b)



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l =1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[l] = nums[i]
                l =l+1
        return l

