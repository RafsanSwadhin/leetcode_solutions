nums = [1,2,3,1,1,3]
ans = 0
for i in range(len(nums)):
    count = 0
    for j in range(i+1,len(nums)):
        if nums[i] == nums[j]:
            count += 1

    ans +=count
print(ans)



    