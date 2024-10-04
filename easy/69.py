# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x == 0:
#             return 0
#         l = 1
#         r = x
        
#         while l <= r:
#             m = (l + r) // 2
#             if m**2 == x:  # Perfect square
#                 return m

#             elif m**2 < x:  # Too small, move the left boundary
#                 l = m + 1
#             else:  # Too large, move the right boundary
#                 r = m - 1
                
#         return r  # r will be the floor of the square root of x


#---------- explanation

# The line `return r` in your code handles cases where the number `x` is **not a perfect square**. When the loop ends (i.e., when `l` exceeds `r`), `r` will hold the largest integer whose square is less than or equal to `x`. 

# Here's an example to show how `return r` works:

# ### Example: 
# **Input**: `x = 8`

# #### Steps:

# 1. **Initial values**:
#    - `l = 1`
#    - `r = 8`

# 2. **First iteration**:
#    - `m = (l + r) // 2 = (1 + 8) // 2 = 4`
#    - `m**2 = 4**2 = 16`
#    - Since `m**2 > x`, set `r = m - 1 = 3`.

# 3. **Second iteration**:
#    - `l = 1`
#    - `r = 3`
#    - `m = (l + r) // 2 = (1 + 3) // 2 = 2`
#    - `m**2 = 2**2 = 4`
#    - Since `m**2 < x`, set `l = m + 1 = 3`.

# 4. **Third iteration**:
#    - `l = 3`
#    - `r = 3`
#    - `m = (l + r) // 2 = (3 + 3) // 2 = 3`
#    - `m**2 = 3**2 = 9`
#    - Since `m**2 > x`, set `r = m - 1 = 2`.

# 5. **End of the loop**:
#    - Now, `l = 3` and `r = 2`. Since `l > r`, the loop terminates, and the function returns `r = 2`.

# #### Explanation:
# The square root of `8` is approximately `2.828`, but since we are returning the **floor** of the square root, the function correctly returns `2`. The `return r` works here because `r = 2` is the largest integer whose square (`2**2 = 4`) is less than or equal to `8`.