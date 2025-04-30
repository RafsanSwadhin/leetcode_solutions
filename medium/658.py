def findClosestElements(arr, k, x):
    left = 0
    right = len(arr) - k  # possible starting positions

    while left < right:
        mid = (left + right) // 2
        
        # Compare distances:
        if x - arr[mid] > arr[mid + k] - x:
            # x is closer to arr[mid + k], move window right
            left = mid + 1
        else:
            # x is closer to arr[mid], move window left
            right = mid

    # After binary search, left is the best starting index
    return arr[left:left + k]





## ✅ Idea (Using Binary Search):
# Since `arr` is **already sorted**, we can use **binary search** to find the **best window** of size `k`.

# - **Window** means continuous subarray of size `k`.
# - We search for the **left boundary** of the window.

# ---

# ## ✅ Full Python Code (Binary Search Approach):

# ```python
# def findClosestElements(arr, k, x):
#     left = 0
#     right = len(arr) - k  # possible starting positions

#     while left < right:
#         mid = (left + right) // 2
        
#         # Compare distances:
#         if x - arr[mid] > arr[mid + k] - x:
#             # x is closer to arr[mid + k], move window right
#             left = mid + 1
#         else:
#             # x is closer to arr[mid], move window left
#             right = mid

#     # After binary search, left is the best starting index
#     return arr[left:left + k]
# ```

# ---

# ## ✅ Step-by-step Explanation:

# 1. `left = 0`, `right = len(arr) - k`
# 2. While `left < right`:
#    - Find mid index.
#    - Compare distance between `x` and:
#      - `arr[mid]`
#      - `arr[mid + k]`
# 3. Shift window **left** or **right** based on distance.
# 4. Finally, return `arr[left:left+k]` — the k closest numbers.

# ---

# ## ✅ Example Walkthrough:

# Input:
# ```python
# arr = [1,2,3,4,5]
# k = 4
# x = 3
# ```

# - left = 0, right = 1
# - mid = 0
# - Compare:
#   - Distance to arr[mid]=1: |1-3| = 2
#   - Distance to arr[mid+k]=5: |5-3| = 2
# - Since 2 <= 2, move `right = mid = 0`
# - Now left == right

# Pick elements: `arr[0:4] = [1,2,3,4]` ✅

# ---

# # 🎯 Final Summary:
# | Method | Time Complexity | When to use |
# |:---|:---|:---|
# | Simple Sort | O(N log N) | Small input |
# | Binary Search | O(log(N-k) + k) | Large input, faster |

