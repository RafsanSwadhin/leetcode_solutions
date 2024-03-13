nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
res = []
for i in range(m):
    for  j in range(n):
        if nums1[i] > nums2[i]:
            res.append(nums2[i])
        else:
            res.append(nums1[i])

  
print(res)