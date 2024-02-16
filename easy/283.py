
n = [1,2,3,4]
l = 0
k = []

for i in range(len(n)-1):
    if n[l] in n:
        n.remove(n[l])
        print(n)
        s = 1  
        for j in n:
            s = s*j
        k.append(s)

        n.insert(l,n[l])
        l= 1+l
print(k)

'''
n = [2,3,4,5]
m = n[:1] + n[1+1:]
print(m)

n = [1, 2, 3, 4]
k = []

for i in range(len(n)):
    # Create a copy of the list n with the current element removed
    temp_list = n[:i] + n[i+1:]
    
    # Calculate the product of all elements in temp_list
    s = 1
    for j in temp_list:
        s *= j
    
    k.append(s)

#print(k)
n = [-1, 1, 0, -3, 3]

try:
    index_of_zero = n.index(0)
    print(index_of_zero)

except ValueError:
    print("0 not found in the list")

'''


