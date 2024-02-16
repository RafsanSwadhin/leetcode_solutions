class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #if n < 0:
            #return False
        p = 0
        v = 1
        while v <= n :
            #if n < 0:
            if n < 0 and v > n:
                return False
            #if v == n:
            elif v == n:
                return True
           # else :
            p +=1
            v = 2**p
        #return False
        