'''
list_ = [88,2,3,5,7,7,"i"]
set_ = {2,3,3,3,3,3,3,3,"i"}
print(set_) #{'i',2,3}
tuple_ = tuple(list_) 
print(tuple_) #(2, 3, 5, 7, 7, 'i')

'''

nums = [-1,0,1,2,-1,-4]
n = len(nums)
nums.sort()
#print(nums) #[-4, -1, -1, 0, 1, 2]
ans = []
mySet = set()
for i in range(n):
    j = i + 1
    k = n - 1

    while j < k:
        total = nums[i] + nums[j] + nums[k]

        if total == 0:
            temp = [nums[i], nums[j], nums[k]]
            mySet.add(tuple(temp))
            j += 1
            k -= 1
        elif total < 0:
            j += 1
        elif total > 0:
            k -= 1
#print(mySet)
for x in mySet:
    ans.append(list(x))
    #print(list(x))
print(ans)
