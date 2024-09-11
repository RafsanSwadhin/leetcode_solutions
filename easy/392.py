s = "bwc"
t = "ahbgdc"

l,r = 0,0

while l < len(s) and r < len(t):
    if s[l] == t[r]:
        l += 1
    r += 1

if l == len(s):
    print(True)
else:
    print(False)

