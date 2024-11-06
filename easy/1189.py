from collections import Counter

text = "nlaebolko"
countText = Counter(text)  # Counts each character's frequency in `text`
ballon = Counter("balloon")  # Counts each character's frequency in the target word "balloon"

print(countText)  # This will print the frequency of characters in `text`

res = len(text)  # Initialize `res` to the length of `text`
for c in ballon:
    res = min(res, countText[c] // ballon[c])  # Update `res` with the minimum count of each character required

print(res)  # This will print the number of times "balloon" can be formed from `text`


# Here's a step-by-step explanation of each line in this code:

# ### Code Overview

# This code counts how many times you can form the word "balloon" using the letters in the `text` string. 

# ### Step-by-Step Breakdown

# ```python
# from collections import Counter
# ```
# - **Explanation**: This line imports `Counter` from Python's `collections` module. `Counter` is a specialized dictionary-like structure that helps in counting the frequency of elements in a sequence (like a string).

# ```python
# text = "nlaebolko"
# ```
# - **Explanation**: This line initializes a variable `text` with the string `"nlaebolko"`. This string contains letters that may or may not be enough to form the word "balloon."

# ```python
# countText = Counter(text)
# ```
# - **Explanation**: `Counter(text)` creates a `Counter` object, `countText`, which counts the occurrences of each character in `text`.
  
#   For `text = "nlaebolko"`, `countText` would be:
#   ```python
#   Counter({'o': 2, 'l': 2, 'n': 1, 'a': 1, 'e': 1, 'b': 1, 'k': 1})
#   ```

# ```python
# ballon = Counter("balloon")
# ```
# - **Explanation**: This line creates another `Counter` object, `ballon`, based on the string `"balloon"`. This helps to know how many of each letter are needed to form the word "balloon."

#   For `"balloon"`, `ballon` would be:
#   ```python
#   Counter({'o': 2, 'l': 2, 'b': 1, 'a': 1, 'n': 1})
#   ```

# ```python
# res = len(text)
# ```
# - **Explanation**: The variable `res` is initialized to `len(text)`, which is the length of `text`. In this case, `len("nlaebolko")` is `9`.
# - **Purpose**: `res` will be used to store the minimum number of times "balloon" can be formed with the characters in `text`. Setting `res` to `len(text)` ensures we start with a high value to find the minimum value.

# ```python
# for c in ballon:
# ```
# - **Explanation**: This starts a loop over each unique character `c` in `ballon` (the required letters for "balloon": 'b', 'a', 'l', 'o', 'n').

# ```python
#     res = min(res, countText[c] // ballon[c])
# ```
# - **Explanation**: For each character `c` in `ballon`:
#   - `countText[c]` gives the count of character `c` in `text`.
#   - `ballon[c]` gives the count of character `c` required to form one "balloon."
#   - `countText[c] // ballon[c]` calculates how many times `text` provides enough of that specific character to form "balloon."

#   Using `min(res, countText[c] // ballon[c])` ensures that `res` takes the minimum value across all letters in "balloon," as forming the word "balloon" requires each letter in the exact quantities in `ballon`.

# - **Example**: For `text = "nlaebolko"`, here's how `res` is updated for each character:
#   - For `'b'`: `res = min(9, 1 // 1) => res = 1`
#   - For `'a'`: `res = min(1, 1 // 1) => res = 1`
#   - For `'l'`: `res = min(1, 2 // 2) => res = 1`
#   - For `'o'`: `res = min(1, 2 // 2) => res = 1`
#   - For `'n'`: `res = min(1, 1 // 1) => res = 1`

# After the loop, `res` holds the value `1`, indicating that "balloon" can be formed once.

# ```python
# print(res)
# ```
# - **Explanation**: This prints the result, which is the maximum number of times "balloon" can be constructed from the characters in `text`. In this case, the output is `1`.

# ### Summary of Output

# For `text = "nlaebolko"`, the output is:
# ```python
# 1
# ```

# This means that "balloon" can be formed exactly once using the characters in `text`.