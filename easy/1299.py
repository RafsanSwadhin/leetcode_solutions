'''

arr = [17, 18, 5, 4, 6, 1]
res = []

for i in range(1,len(arr)):
    max_val = max(arr[i:])  # Find the maximum of the remaining sublist
    res.append(max_val)

print(res+[-1])

'''


'''

arr = [17, 18, 5, 4, 6, 1]

res = []
max_val = -1  # Start with -1 as the last element should be -1

# Traverse the array from right to left
for i in range(len(arr)-1, -1, -1):
    res.append(max_val)
    max_val = max(max_val, arr[i])  # Update the maximum value

# Since we traversed from right to left, reverse the result
res.reverse()

print(res)

'''

arr = [17, 18, 5, 4, 6, 1]
rightmax = -1
for i in range(len(arr)-1, -1, -1):
    newmax = max(rightmax,arr[i])
    arr[i] = rightmax
    rightmax = newmax

print(arr)

#explanation
'''

Let's break down the code step by step:

### Initial Setup:
```python
arr = [17, 18, 5, 4, 6, 1]  # The original array
rightmax = -1                # Initialize the maximum value to the right to -1
```

- `arr` is the list of integers we are modifying. The goal is to replace each element with the greatest value that exists to its right.
- `rightmax` is initialized to `-1` because the rightmost value should be replaced by `-1` (as there are no elements to its right).

### Loop Setup:
```python
for i in range(len(arr)-1, -1, -1):
```

- This loop iterates through the array from **right to left**. The `range(len(arr)-1, -1, -1)` means:
  - Start at index `len(arr)-1` (which is the last index, `5` in this case).
  - Continue until you reach index `0`.
  - Move backward by decrementing the index by `1` in each iteration.
  
For the array `[17, 18, 5, 4, 6, 1]`, this loop will iterate over the indices `5, 4, 3, 2, 1, 0`.

### Inside the Loop:
```python
    newmax = max(rightmax, arr[i])
    arr[i] = rightmax
    rightmax = newmax
```

- **`newmax = max(rightmax, arr[i])`**: 
  - Here, `newmax` is set to the maximum of `rightmax` and `arr[i]`.
  - `rightmax` holds the maximum value to the right of the current element `arr[i]`.
  - `arr[i]` is the current element of the array.
  
- **`arr[i] = rightmax`**:
  - Replace the current element `arr[i]` with `rightmax`, which is the maximum value of all the elements to the right of it.
  
- **`rightmax = newmax`**:
  - Update `rightmax` to `newmax` so that on the next iteration, `rightmax` contains the largest value encountered so far from the right side of the array.

### Step-by-Step Execution:

1. **Initial state**:
   - `arr = [17, 18, 5, 4, 6, 1]`
   - `rightmax = -1`
   
2. **Iteration 1 (`i = 5`)**:
   - `arr[5] = 1`
   - `newmax = max(-1, 1) = 1`
   - Replace `arr[5]` with `rightmax = -1`, so `arr[5] = -1`.
   - Update `rightmax = 1`.

   Resulting `arr`: `[17, 18, 5, 4, 6, -1]`
   
3. **Iteration 2 (`i = 4`)**:
   - `arr[4] = 6`
   - `newmax = max(1, 6) = 6`
   - Replace `arr[4]` with `rightmax = 1`, so `arr[4] = 1`.
   - Update `rightmax = 6`.

   Resulting `arr`: `[17, 18, 5, 4, 1, -1]`
   
4. **Iteration 3 (`i = 3`)**:
   - `arr[3] = 4`
   - `newmax = max(6, 4) = 6`
   - Replace `arr[3]` with `rightmax = 6`, so `arr[3] = 6`.
   - `rightmax` remains `6`.

   Resulting `arr`: `[17, 18, 5, 6, 1, -1]`
   
5. **Iteration 4 (`i = 2`)**:
   - `arr[2] = 5`
   - `newmax = max(6, 5) = 6`
   - Replace `arr[2]` with `rightmax = 6`, so `arr[2] = 6`.
   - `rightmax` remains `6`.

   Resulting `arr`: `[17, 18, 6, 6, 1, -1]`
   
6. **Iteration 5 (`i = 1`)**:
   - `arr[1] = 18`
   - `newmax = max(6, 18) = 18`
   - Replace `arr[1]` with `rightmax = 6`, so `arr[1] = 6`.
   - Update `rightmax = 18`.

   Resulting `arr`: `[17, 6, 6, 6, 1, -1]`
   
7. **Iteration 6 (`i = 0`)**:
   - `arr[0] = 17`
   - `newmax = max(18, 17) = 18`
   - Replace `arr[0]` with `rightmax = 18`, so `arr[0] = 18`.
   - `rightmax` remains `18`.

   Final `arr`: `[18, 6, 6, 6, 1, -1]`

### Final Output:
```python
[18, 6, 6, 6, 1, -1]
```

### Summary:
- We iterate over the array from the rightmost element to the leftmost.
- For each element, we replace it with the greatest element to its right, updating the `rightmax` as we go.
- This approach ensures that we only pass through the list once, achieving an efficient time complexity of `O(n)`.

'''