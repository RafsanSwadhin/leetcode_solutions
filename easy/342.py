class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        p = 0
        v = 1
        while v <= n :
            if v < 0 and v>n:
                return False
            elif v  == n :
                return True
            p += 1
            v = 4**p