'''
strs = ["flower", "flow", "flight"]
res = ""
for i in range(len(strs[0])):
    for s in strs:
        if i == len(s) or s[i] != strs[0][i]: 
            print(res)
            

    res += strs[0][i]

print(res)

'''

def longestCommonPrefix(strs):
    if not strs:
        return ""

    res = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i >= len(s) or s[i] != strs[0][i]:
                return res

        res += strs[0][i]

    return res

# Test the function
strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))




