nums = [1,2,3,4,5,6,7]
# k = 3
# left_k = 0
# right_k = (-1)*k
# # print(nums[-3]) 5
# while left_k < k:
#     nums[left_k],nums[right_k] = nums[right_k],nums[left_k]
#     left_k +=1
#     right_k +=1

# print(nums)

nums = [1,2,3,4,5,6,7]
k = 3
k = k%len(nums)
l,r = 0, len(nums)-1

while l < r:
    nums[l],nums[r] = nums[r],nums[l]
    l +=1
    r -=1

print(nums)

l,r = 0, k-1

while l < r:
    nums[l],nums[r] = nums[r],nums[l]
    l +=1
    r -=1
print(nums)

l,r = k, len(nums)-1

while l < r:
    nums[l],nums[r] = nums[r],nums[l]
    l +=1
    r -=1
print(nums)



# Let's analyze the time complexity and space complexity of the provided solution for rotating an array.

# ### Code Breakdown:
# 1. **Step 1: Calculate `k = k % len(nums)`**: 
#    - This ensures `k` is within the bounds of the array's length, avoiding unnecessary rotations. 
#    - This takes **O(1)** time.

# 2. **Step 2: Reverse the entire array:**
#    - The first `while` loop reverses the entire array. 
#    - The two-pointer approach swaps elements from the start and end, moving toward the center.
#    - This takes **O(n)** time, where `n` is the length of the array (`len(nums)`).

# 3. **Step 3: Reverse the first `k` elements:**
#    - The second `while` loop reverses the first `k` elements.
#    - This operation takes **O(k)** time.

# 4. **Step 4: Reverse the remaining `n - k` elements:**
#    - This operation isn't shown directly in the code provided but would involve another loop similar to Step 3 to reverse the elements from `k` to the end.
#    - This would take **O(n - k)** time.

# ### Time Complexity:
# - The first reversal (entire array) takes **O(n)**.
# - The second reversal (first `k` elements) takes **O(k)**.
# - The third reversal (remaining `n - k` elements) takes **O(n - k)**.
  
# So the overall time complexity is **O(n)**, as all the operations together are linear in relation to the size of the array.

# ### Space Complexity:
# - The solution only uses a constant amount of extra space for the pointers (`l`, `r`) and some temporary variables for swapping.
# - Since no additional arrays or data structures are used, the space complexity is **O(1)**.

# ### Conclusion:
# - **Time complexity**: **O(n)**
# - **Space complexity**: **O(1)**

# This is an efficient in-place solution for rotating the array.