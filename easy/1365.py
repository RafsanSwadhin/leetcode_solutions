nums = [8,1,2,2,3]
my_dict = {}
sort_ = sorted(nums)
#print(sort_)
#print

res = []
for i in range(len(nums)):
    if sort_[i] not in my_dict:
        my_dict[sort_[i]] = i

#for j in range(len(nums)):
#print(my_dict)
for j in range(len(nums)):
    res.append(my_dict[nums[j]])
print(res)