from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            lst = [0] * 26
            for c in i:
                lst[ord(c) - ord("a")] += 1
            res[tuple(lst)].append(i)
        return list(res.values())


'''
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # Create a defaultdict to store grouped anagrams
        
        for i in strs:  # Iterate through the list of input strings
            lst = [0] * 26  # Initialize a list for counting character occurrences for each string
            
            for c in i:  # Iterate through each character in the current string
                lst[ord(c) - ord("a")] += 1  # Increment the count of the character in lst
                
            # Convert the count list to a tuple and use it as a key in res dictionary
            # Append the current string to the list associated with this key
            res[tuple(lst)].append(i)
        
        return res.values  # Return the values (groups of anagrams) from the defaultdict


'''




'''
Now, let's go through the code execution:

You import defaultdict from the collections module, which will be used to create a dictionary with default list values.

You define a class called Solution with a method groupAnagrams that takes a list of strings strs as input.

You initialize a defaultdict named res to store grouped anagrams. This dictionary will have lists as default values.

You iterate through each string i in the strs list:

a. You initialize a list lst of 26 zeros, where each element represents the count of a letter from 'a' to 'z'.

b. You iterate through each character c in the current string i.

c. You increment the count for the character c in the lst list based on its position in the alphabet.

d. You convert the lst list into a tuple and use it as the key in the res dictionary. You then append the current string i to the list associated with this key.

Finally, you return the values (groups of anagrams) from the res dictionary.

The code should work correctly to group anagrams, but there is a small issue with return res.values. It should be return list(res.values()) to convert the values of the dictionary to a list of lists. Here's the corrected code:
'''

'''
A defaultdict is a subclass of the built-in Python dict class. It's a container that's similar to a regular dictionary, but it allows you to specify a default value for any new keys that are accessed. This can be quite useful in various scenarios, especially when you're dealing with dictionaries of lists, sets, or other data structures. Let's explore defaultdict with multiple examples.

Example 1: defaultdict with Lists

Suppose you want to create a dictionary where each key is associated with a list of values. A defaultdict makes it easy to add elements to the lists without checking if the key exists or not.

from collections import defaultdict

# Create a defaultdict where the default value for each key is an empty list
my_dict = defaultdict(list)

my_dict['fruits'].append('apple')
my_dict['fruits'].append('banana')
my_dict['vegetables'].append('carrot')

print(my_dict)

In this example, you don't need to check if the key exists in the dictionary before appending to the list associated with that key. The defaultdict automatically initializes an empty list for any new key.

Example 2: defaultdict with Integers

You can also use defaultdict with integers to create a counter-like structure.

from collections import defaultdict

# Create a defaultdict where the default value for each key is 0 (an integer)
count_dict = defaultdict(int)

words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']

for word in words:
    count_dict[word] += 1

print(count_dict)

Output:

defaultdict(<class 'int'>, {'apple': 3, 'banana': 2, 'cherry': 1})

In this example, you're counting the occurrences of each word in a list. The defaultdict with integer default values makes it easy to increment the count for each word without explicitly initializing them.

Example 3: defaultdict with Sets

You can use defaultdict with sets to create a dictionary of sets. This is useful for grouping elements.

from collections import defaultdict

# Create a defaultdict where the default value for each key is an empty set
group_dict = defaultdict(set)

group_dict['fruits'].add('apple')
group_dict['fruits'].add('banana')
group_dict['vegetables'].add('carrot')

print(group_dict)
output :

defaultdict(<class 'set'>, {'fruits': {'apple', 'banana'}, 'vegetables': {'carrot'}})
In this example, you're creating groups of items using sets for different categories.

These are just a few examples of how you can use defaultdict in Python. It simplifies the process of working with dictionaries and is especially helpful when dealing with collections of data that need to be organized efficiently.


If you use res[list(lst)].append(i) instead of res[tuple(lst)].append(i), you will encounter a TypeError. Here's why:

res is a defaultdict with lists as its default values.

In the original code, you use tuple(lst) as the key for the res dictionary. This works because a tuple is hashable, meaning it can be used as a dictionary key.

If you change it to list(lst), you are using a list as the key. Lists are not hashable in Python, which means they cannot be used as dictionary keys. Attempting to do so will result in a TypeError.

So, using res[list(lst)].append(i) is not a valid way to modify the code because it will lead to an error. You should keep res[tuple(lst)].append(i) as it is, as this correctly utilizes a tuple as the dictionary key.

'''