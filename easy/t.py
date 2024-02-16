'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=("".join(i for i in s if i.isalnum())).lower()
        return new==new[::-1]
'''

from collections import defaultdict


d = defaultdict(list)
s = ["eat", "tea", "tan", "ate", "nat", "bat"]
arr = [0] * 26  # Initialize an array with 26 zeros to represent each letter of the alphabet
#print(arr)
arr[0] =1
#print(arr)
for i in s:
    for char in i:
        arr[ord(char) - ord('a')] += 1

print(arr)
n = tuple(arr)
print(n)
d[tuple(arr)].append(s)
        