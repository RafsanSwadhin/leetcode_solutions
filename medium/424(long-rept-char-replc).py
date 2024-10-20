class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        counts = [0]*26
        for r in range(len(s)):
            counts[ord(s[r])-65] +=1
            while (r-l+1) - max(counts) >k:
                counts[ord(s[l])-65] -=1
                l +=1
            longest = max(longest, (r-l+1))
        return longest


# Let's walk through your code step-by-step for the input `s = "AABABBA"` and `k = 1` to explain how each line works and produces the output `4`.

# ### Your Code:
# ```python
# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         longest = 0
#         l = 0
#         counts = [0] * 26
#         for r in range(len(s)):
#             counts[ord(s[r]) - 65] += 1
#             while (r - l + 1) - max(counts) > k:
#                 counts[ord(s[l]) - 65] -= 1
#                 l += 1
#             longest = max(longest, r - l + 1)
#         return longest
# ```

# ### Explanation of Each Line:
# 1. **`class Solution:`**
#    - Defines a class `Solution` in which the method `characterReplacement` is implemented.

# 2. **`def characterReplacement(self, s: str, k: int) -> int:`**
#    - This method takes two arguments: the string `s` and the integer `k`, representing the maximum number of changes allowed.
#    - The method will return an integer, the length of the longest substring containing the same letter after making at most `k` changes.

# 3. **`longest = 0`**
#    - Initializes a variable `longest` to store the length of the longest valid substring found so far.

# 4. **`l = 0`**
#    - Initializes the left pointer `l` of the sliding window. This pointer helps in keeping track of the start of the current window.

# 5. **`counts = [0] * 26`**
#    - This initializes a list `counts` of size 26, where each index corresponds to a letter of the alphabet ('A' to 'Z'). The list is used to count the occurrences of each letter in the current window.
#    - Example: If `counts[0] = 3`, it means there are 3 occurrences of the letter 'A' in the current window.

# 6. **`for r in range(len(s)):`**
#    - A `for` loop iterating over each character in the string `s`. `r` is the right pointer of the sliding window, starting from 0 and moving right through the string.
   
# ### Processing Each Character (with Input: `"AABABBA"`)

# 7. **`counts[ord(s[r]) - 65] += 1`**
#    - This line updates the `counts` array by incrementing the count of the current character `s[r]`.
#    - `ord(s[r]) - 65` gives the index in the `counts` array that corresponds to the character `s[r]` ('A' = 0, 'B' = 1, etc.).
#    - Example: For `r = 0`, `s[r] = "A"`, and `counts[ord("A") - 65] += 1` increments `counts[0]` by 1.

# 8. **`while (r - l + 1) - max(counts) > k:`**
#    - This `while` loop ensures that the window `[l, r]` contains at most `k` characters that need to be changed.
#    - `(r - l + 1)` is the current window size, and `max(counts)` is the count of the most frequent character in the window.
#    - The difference `(r - l + 1) - max(counts)` gives the number of characters that need to be changed in the window.
#    - If this difference is greater than `k`, it means more than `k` characters need to be changed, so the window must be shrunk by moving the left pointer `l` to the right.

# ### Shrinking the Window (if needed)

# 9. **`counts[ord(s[l]) - 65] -= 1`**
#    - If the `while` loop condition is met, this line decreases the count of the character at the left of the window (`s[l]`), because the left pointer `l` will be moved to the right.

# 10. **`l += 1`**
#     - Moves the left pointer `l` one step to the right, effectively shrinking the window.

# ### Updating the Longest Valid Substring

# 11. **`longest = max(longest, r - l + 1)`**
#     - After adjusting the window (if necessary), this line updates the `longest` variable to the maximum of its current value and the size of the current valid window (`r - l + 1`).

# ### Final Return

# 12. **`return longest`**
#     - After iterating over all characters in the string, the method returns `longest`, which is the length of the longest substring containing the same letter after at most `k` changes.

# ---

# ### Example Walkthrough: Input `s = "AABABBA"`, `k = 1`

# 1. Initial State: `longest = 0`, `l = 0`, `counts = [0]*26`.
   
# 2. **Step 1 (`r = 0`)**: `s[0] = "A"`.
#    - Update `counts`: `counts[0] = 1`.
#    - Window size: `(r - l + 1) = 1`, `max(counts) = 1`.
#    - No need to shrink the window.
#    - Update `longest = max(0, 1) = 1`.

# 3. **Step 2 (`r = 1`)**: `s[1] = "A"`.
#    - Update `counts`: `counts[0] = 2`.
#    - Window size: `(r - l + 1) = 2`, `max(counts) = 2`.
#    - No need to shrink the window.
#    - Update `longest = max(1, 2) = 2`.

# 4. **Step 3 (`r = 2`)**: `s[2] = "B"`.
#    - Update `counts`: `counts[1] = 1`.
#    - Window size: `(r - l + 1) = 3`, `max(counts) = 2`.
#    - No need to shrink the window (`3 - 2 <= 1`).
#    - Update `longest = max(2, 3) = 3`.

# 5. **Step 4 (`r = 3`)**: `s[3] = "A"`.
#    - Update `counts`: `counts[0] = 3`.
#    - Window size: `(r - l + 1) = 4`, `max(counts) = 3`.
#    - No need to shrink the window (`4 - 3 <= 1`).
#    - Update `longest = max(3, 4) = 4`.

# 6. **Step 5 (`r = 4`)**: `s[4] = "B"`.
#    - Update `counts`: `counts[1] = 2`.
#    - Window size: `(r - l + 1) = 5`, `max(counts) = 3`.
#    - Need to shrink the window (`5 - 3 > 1`).
#    - Shrink by moving `l = 1`, then `l = 2`.
#    - Update `longest = 4` (window size still 4).

# 7. **Step 6 (`r = 5`)**: `s[5] = "B"`.
#    - Update `counts`: `counts[1] = 3`.
#    - No need to shrink the window.
#    - `longest` remains 4.

# 8. **Step 7 (`r = 6`)**: `s[6] = "A"`.
#    - Update `counts`: `counts[0] = 3`.
#    - Shrink window again, but `longest` stays 4.

# **Final Result: 4**

# ---

# ### Summary:

# - The code uses a sliding window approach to find the longest substring that can be transformed into a sequence of the same letter with at most `k` replacements.
# - The output `4` corresponds to the substring `"AABB"` after replacing one 'A' with 'B'.


# Let’s break it down in a more straightforward way with a simple analogy:

# ### Key Idea:
# The main goal of the algorithm is to find the longest substring where you can have as many repeating characters as possible by changing at most `k` characters.

# #### 1. **Understanding `(r - l + 1)`**
# This expression gives the length of the current window (substring) from the left pointer `l` to the right pointer `r`. For example, if `l = 1` and `r = 4`, the length of the window (substring) is `4 - 1 + 1 = 4`.

# #### 2. **Understanding `max(counts)`**
# - `counts` is a list that keeps track of how many times each character appears in the current window (substring).
# - `max(counts)` gives us the count of the **most frequent character** in the current window.

# So, in a substring like `"AABBA"`, the most frequent character is `'A'` and its count is `3` (since there are three A’s).

# #### 3. **Why the difference `(r - l + 1) - max(counts)`?**
# This difference represents **the number of characters in the window that are NOT the most frequent character**.

# - `(r - l + 1)` is the total number of characters in the window.
# - `max(counts)` is the number of characters in the window that are already the most frequent.

# The difference, `(r - l + 1) - max(counts)`, tells us how many characters **need to be changed** to make the entire window consist of only the most frequent character.

# ##### Example:
# - Suppose the window is `"AABBA"`.
#   - `(r - l + 1)` = 5 (the window length is 5).
#   - `max(counts)` = 3 (the most frequent character, 'A', appears 3 times).

# The difference is `5 - 3 = 2`. This means that to make the entire window `"AAAAA"`, we need to change 2 characters (the 2 'B's).

# #### 4. **Why compare the difference with `k`?**
# - `k` is the number of changes you are allowed to make.
# - If the difference `(r - l + 1) - max(counts)` is **less than or equal to `k`**, it means that we can change the necessary characters (because it’s within the allowed `k` changes).
# - **But**, if the difference is **greater than `k`**, it means we need to make more changes than `k`, which is not allowed.

# #### 5. **Why shrink the window when the difference is greater than `k`?**
# If the number of changes needed is greater than `k`, we cannot maintain that large window. So, we shrink the window by moving the left pointer `l` to the right. This reduces the window size until the number of changes required is within the allowed `k`.

# ### Example:
# - String: `"AABBA"`
# - Allowed changes (`k`): 1

# 1. **Initial Window: `"AAB"` (l = 0, r = 2)**
#    - Window size: 3
#    - Most frequent character: 'A' (2 occurrences)
#    - Characters to change: `3 - 2 = 1`
#    - Since `1 <= k`, this window is valid.

# 2. **Next Window: `"AABB"` (l = 0, r = 3)**
#    - Window size: 4
#    - Most frequent character: 'A' (2 occurrences)
#    - Characters to change: `4 - 2 = 2`
#    - Since `2 > k`, this window is not valid. We need to shrink it by moving `l` to the right.

# 3. **Shrinking to: `"ABB"` (l = 1, r = 3)**
#    - Window size: 3
#    - Most frequent character: 'B' (2 occurrences)
#    - Characters to change: `3 - 2 = 1`
#    - Since `1 <= k`, this window is valid.

# By adjusting the window size using this logic, the algorithm finds the longest possible valid substring.