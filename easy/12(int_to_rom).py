
num = 1
all = [["I",1],["IV",4],["V",5],["IX",9],["X",10],["XL",40],["L",50],["XC",90],
       ["C",100],["CD",400],["D",500],["CM",900],["M",1000],
       ]
result =   ""
for sym,val in reversed(all):
    #print(sym,val)
    #print(type(sym),type(val))
    if num // val:
        count = num//val
        result += (sym*count)
        num = num % val
print(result)




#print(s[0]) ---s[0]=1 
#print(type(roman[1]))--- class 'str'
#print(roman[1]) ---I
#print(type(roman[1])) --- class 'str'
#print(list(roman.keys())[0])  # This will print 1
#print(list(roman.keys())[1])  # This will print 5
'''
for i in range(len(s)):
    #print(roman[s[i]]) -- 1
    if i +1 < len(s) and roman[s[i]] < roman[s[i+1]]:
        result -= roman[s[i]]
    else:
        result += roman[s[i]]

print(result)


'''

