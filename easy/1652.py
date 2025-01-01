# class Solution:
#     def decrypt(self, code: List[int], k: int) -> List[int]:
#         n = len(code)
#         res = [0]*n
#         l = 0
#         curr_sum = 0
#         for r in range(n + abs(k)):
#             curr_sum += code[r % n]
#             if r-l+1 > abs(k):
#                 curr_sum -= code[l%n]
#                 l = (l+1)%n
#             if r-l+1 == abs(k):
#                 if k > 0:
#                     res[(l-1)%n] = curr_sum
#                 elif k < 0 :
#                     res[(r+1)%n] = curr_sum
#         return res


# ### Input:
# ```python
# code = [5, 7, 1, 4]
# k = 3


# ### Explanation by Iteration:

# #### Initialization:
# - `n = 4`, `res = [0, 0, 0, 0]`, `l = 0`, `curr_sum = 0`
# - `r` will loop from `0` to `6` (because `n + abs(k) = 4 + 3 = 7`).

# ---

# #### Iteration 1 (`r = 0`):
# 1. `curr_sum += code[0 % 4] = curr_sum + code[0] = 0 + 5 = 5`
# 2. Window size = `r - l + 1 = 0 - 0 + 1 = 1` → Not equal to `abs(k) = 3`. Do nothing.
# 3. **State**:
#    - `curr_sum = 5`, `res = [0, 0, 0, 0]`, `l = 0`

# ---

# #### Iteration 2 (`r = 1`):
# 1. `curr_sum += code[1 % 4] = curr_sum + code[1] = 5 + 7 = 12`
# 2. Window size = `r - l + 1 = 1 - 0 + 1 = 2` → Not equal to `abs(k) = 3`. Do nothing.
# 3. **State**:
#    - `curr_sum = 12`, `res = [0, 0, 0, 0]`, `l = 0`

# ---

# #### Iteration 3 (`r = 2`):
# 1. `curr_sum += code[2 % 4] = curr_sum + code[2] = 12 + 1 = 13`
# 2. Window size = `r - l + 1 = 2 - 0 + 1 = 3` → Equal to `abs(k) = 3`. Perform update:
#    - Since `k > 0`, update `res[(l - 1) % n] = res[-1 % 4] = res[3] = 13`.
# 3. **State**:
#    - `curr_sum = 13`, `res = [0, 0, 0, 13]`, `l = 0`

# ---

# #### Iteration 4 (`r = 3`):
# 1. `curr_sum += code[3 % 4] = curr_sum + code[3] = 13 + 4 = 17`
# 2. Window size = `r - l + 1 = 3 - 0 + 1 = 4` → Greater than `abs(k) = 3`. Shrink the window:
#    - `curr_sum -= code[0 % 4] = curr_sum - code[0] = 17 - 5 = 12`
#    - `l = (l + 1) % 4 = 1`
# 3. Window size after shrinking = `r - l + 1 = 3 - 1 + 1 = 3`. Perform update:
#    - Since `k > 0`, update `res[(l - 1) % n] = res[0] = 12`.
# 4. **State**:
#    - `curr_sum = 12`, `res = [12, 0, 0, 13]`, `l = 1`

# ---

# #### Iteration 5 (`r = 4`):
# 1. `curr_sum += code[4 % 4] = curr_sum + code[0] = 12 + 5 = 17`
# 2. Window size = `r - l + 1 = 4 - 1 + 1 = 4` → Greater than `abs(k) = 3`. Shrink the window:
#    - `curr_sum -= code[1 % 4] = curr_sum - code[1] = 17 - 7 = 10`
#    - `l = (l + 1) % 4 = 2`
# 3. Window size after shrinking = `r - l + 1 = 4 - 2 + 1 = 3`. Perform update:
#    - Since `k > 0`, update `res[(l - 1) % n] = res[1] = 10`.
# 4. **State**:
#    - `curr_sum = 10`, `res = [12, 10, 0, 13]`, `l = 2`

# ---

# #### Iteration 6 (`r = 5`):
# 1. `curr_sum += code[5 % 4] = curr_sum + code[1] = 10 + 7 = 17`
# 2. Window size = `r - l + 1 = 5 - 2 + 1 = 4` → Greater than `abs(k) = 3`. Shrink the window:
#    - `curr_sum -= code[2 % 4] = curr_sum - code[2] = 17 - 1 = 16`
#    - `l = (l + 1) % 4 = 3`
# 3. Window size after shrinking = `r - l + 1 = 5 - 3 + 1 = 3`. Perform update:
#    - Since `k > 0`, update `res[(l - 1) % n] = res[2] = 16`.
# 4. **State**:
#    - `curr_sum = 16`, `res = [12, 10, 16, 13]`, `l = 3`

# ---

# ### Final Output:
# ```python
# res = [12, 10, 16, 13]
# ```