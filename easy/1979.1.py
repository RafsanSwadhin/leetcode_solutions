from math import gcd

def findGCD(nums):
    # Step 1: Find the smallest number in the array
    min_num = min(nums)

    # Step 2: Find the largest number in the array
    max_num = max(nums)

    # Step 3: Calculate the GCD of the smallest and largest numbers
    result_gcd = gcd(min_num, max_num)

    return result_gcd

# Test with the given input
nums = [2, 5, 6, 9, 10]
print(findGCD(nums))  # Output will be 2 (GCD of 2 and 10)
'''

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        from math import gcd
        return gcd(min(nums),max(nums))
'''