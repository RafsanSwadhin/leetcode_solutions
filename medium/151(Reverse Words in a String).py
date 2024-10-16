# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


#solution

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         new_s = s.split()
#         left = 0
#         right = len(new_s)-1
#         while left < right:
#             new_s[left], new_s[right] = new_s[right], new_s[left]
#             left += 1
#             right -= 1
#         return " ".join(new_s)

#explanation





### Intuition of the Code:

# The goal of the code is to **reverse the order of words** in a given string. Here's a breakdown of the intuition behind each step:

# 1. **Splitting the String into Words (`s.split()`)**:
#    - The input string `s` is a sequence of characters with words separated by spaces.
#    - The method `split()` is used to break the string into individual words and return them as a list. Each word is treated as a distinct unit.
#    - Example:
#      - Input: `"the sky is blue"`
#      - After `split()`: `['the', 'sky', 'is', 'blue']`
#    - **Intuition**: We convert the sentence into a list of words because lists are mutable, allowing us to rearrange the words easily.

# 2. **Reversing the List of Words (while loop)**:
#    - Once the string is split into words, the code uses a two-pointer approach (`left` and `right`) to reverse the list of words in place.
#    - **Two-Pointer Technique**:
#      - `left` starts at the beginning of the list, and `right` starts at the end.
#      - The words at `left` and `right` are swapped, then both pointers move inward (increment `left` and decrement `right`).
#      - This process continues until `left` is no longer less than `right`, meaning all words have been reversed.
#    - **Intuition**: Swapping the words from the start and the end mirrors the entire list, effectively reversing the word order.
#      - Example:
#        - Initial: `['the', 'sky', 'is', 'blue']`
#        - After swap: `['blue', 'sky', 'is', 'the']`
#        - Final after all swaps: `['blue', 'is', 'sky', 'the']`

# 3. **Joining the Reversed List Back into a String (`" ".join(new_s)`)**:
#    - After reversing the list of words, the function uses the `join()` method to concatenate the words back into a single string, with spaces in between.
#    - **Intuition**: We have the list of words in the correct order, but we need to form a proper sentence (i.e., a single string with spaces between words), which is why we use `join()`.
#      - Example:
#        - List: `['blue', 'is', 'sky', 'the']`
#        - After `join()`: `"blue is sky the"`

# ### Overall Intuition:

# 1. **Break the Sentence into Manageable Parts (Words)**:
#    - The problem is easier to solve if we treat each word as an individual unit. By splitting the string into words, we isolate each unit and remove concerns about spaces.

# 2. **Reverse the Order of the Units (Words)**:
#    - Reversing the word order can be efficiently done using the two-pointer technique. This avoids the need to create additional data structures and allows us to reverse the list of words in place.

# 3. **Reconstruct the Sentence**:
#    - Once the list of words is in the correct order, we use `join()` to turn it back into a proper sentence format.

# ### Example Walkthrough:

# For the input `"the sky is blue"`:

# 1. **Split into Words**:
#    - `s.split()` → `['the', 'sky', 'is', 'blue']`
   
# 2. **Reverse the List**:
#    - Initial: `['the', 'sky', 'is', 'blue']`
#    - First swap: `['blue', 'sky', 'is', 'the']`
#    - Second swap (in-place): `['blue', 'is', 'sky', 'the']`

# 3. **Join into a Sentence**:
#    - `" ".join(new_s)` → `"blue is sky the"`

# Thus, the final result is `"blue is sky the"`.

# ### Key Takeaways:
# - **Decomposition**: Break down a complex problem (reversing a sentence) into simpler subproblems (managing words in a list).
# - **Two-pointer technique**: A common and efficient way to reverse elements in a list.
# - **Immutability of strings**: The string is split into a list because strings in Python are immutable, and modifying individual characters or words directly isn't feasible. The list provides a mutable structure that makes manipulation easier.