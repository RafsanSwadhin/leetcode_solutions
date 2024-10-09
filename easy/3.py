class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset = set()
        l =  0
        res = 0
        for i in range(len(s)):
            while s[i] in myset:
                myset.remove(s[l])
                l += 1
            myset.add(s[i])
            res = max(res,i-l+1)
        return res