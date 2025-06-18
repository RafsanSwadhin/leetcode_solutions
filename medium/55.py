class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if 0 in nums or nums[0]:
            return False
        else:
            return True