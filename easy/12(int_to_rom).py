
s = "1"

roman={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
result = 0
print(type(roman[1]))
print(roman[1])

print(list(roman.keys())[0])  # This will print 1
print(list(roman.keys())[1])  # This will print 5

'''
for i in range(len(s)):
    #print(roman[s[i]]) -- 1
    if i +1 < len(s) and roman[s[i]] < roman[s[i+1]]:
        result -= roman[s[i]]
    else:
        result += roman[s[i]]

print(result)


'''