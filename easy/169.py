#nums = [3,2,3]
def majorityElement(nums):
    res = 0
    count = 0
    for i in nums:
        if count == 0:
            res = i
        if i == res:
            count += 1
        else:
            count -=1
    return res

print(majorityElement([6,5,5]))
"""

Let's break down the function `majorityElement(nums)` step by step to understand how it works.

### Problem:
The function is supposed to find the **majority element** in a list of integers, which is defined as an element that appears more than `n / 2` times (where `n` is the number of elements in the list). The algorithm used here is the **Boyer-Moore Voting Algorithm**.

### Function Explanation:
```python
def majorityElement(nums):
    res = 0
    count = 0
```
- `res` will store the current candidate for the majority element.
- `count` will keep track of how many times the current candidate appears relative to other numbers.

### Loop:
```python
    for i in nums:
```
- We iterate through each element `i` in the `nums` list.

### Step 1: Reset Candidate
```python
        if count == 0:
            res = i
```
- When `count` is 0, we choose the current element `i` as the new candidate (`res`).
- This is the reset point: If the count drops to 0, we discard the previous candidate and select a new one.

### Step 2: Increment or Decrement Count
```python
        if i == res:
            count += 1
        else:
            count -= 1
```
- If the current element `i` is equal to `res` (the current candidate), we increment the `count`, indicating that this candidate has gained support.
- If `i` is different from `res`, we decrement the `count`, meaning this candidate has lost some support.
- The idea is that the majority element will gain more support than it loses as we move through the list.

### Final Step:
```python
    return res
```
- After looping through the list, `res` will be the majority element.

### Example: `majorityElement([6, 5, 5])`

1. **Initial state**:
   - `res = 0`, `count = 0`.

2. **First iteration** (`i = 6`):
   - `count == 0`, so we set `res = 6`.
   - `i == res` (both are 6), so `count += 1`. Now, `count = 1`.

3. **Second iteration** (`i = 5`):
   - `i != res` (5 is not equal to 6), so `count -= 1`. Now, `count = 0`.

4. **Third iteration** (`i = 5`):
   - `count == 0`, so we set `res = 5`.
   - `i == res` (both are 5), so `count += 1`. Now, `count = 1`.

5. **End of loop**:
   - The final value of `res` is `5`.

### Result:
- The function returns `5`, which is the majority element in the list `[6, 5, 5]`.


"""