'''
from collections import Counter

k = 2
nums = [1, 1, 1, 2, 2, 3]
count = Counter(nums)

# Extract the counts and convert them into a list
count_list = list(count.values())

# Sort the count_list in descending order
count_list.sort(reverse=True)

# Print the top k most frequent numbers as a list
print(count_list[:k])
'''


from collections import Counter
k = 3
nums = [1, 1, 1, 2, 2,3,4,4,4,4,4]
count = Counter(nums)
print(count)
#ko = count.most_common(k)
#print(ko) -- The expression "[(4, 5), (1, 3), (2, 2)]" is a list of tuples in Python
# Use Counter's most_common method to get the top k most frequent numbers
top_k = [x for x, _ in count.most_common(k)]
#top_k.sort() #---- if we want the list as ascending order

print(top_k)

'''

In the line top_k = [x for x, _ in count.most_common(k)], the underscore _ is used as a placeholder for the second, third, fourth, and so on elements in the tuples returned by count.most_common(k).

In this specific context, you are only interested in the first element of each tuple (the number itself), so _ is used to ignore and discard the second element (the count) of each tuple. It's a common convention in Python to use _ as a variable name when you want to indicate that you're intentionally ignoring a value.

So, the line effectively extracts and collects the first elements (numbers) from the tuples returned by count.most_common(k), resulting in a list of the most frequent numbers.
'''