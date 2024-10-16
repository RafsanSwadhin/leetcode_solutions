# n = [1,2,3,4,5,6,7]
# n.remove(1)
# print(n)
# n.insert(0,1)
# print(n)

# n = "the sky is blue"
# print(n)
# words = n.split() 
# print(words) #['the', 'sky', 'is', 'blue']

# for w in words:
#     print(w)

n = "the sky is blue"
new_n = n.split()  # ['the', 'sky', 'is', 'blue']
left = 0
right = len(new_n) - 1
while left < right:
    # Swap the elements at 'left' and 'right' indices
    new_n[left], new_n[right] = new_n[right], new_n[left]
    left += 1
    right -= 1
res = " ".join(new_n)
print(new_n)
print(res)

