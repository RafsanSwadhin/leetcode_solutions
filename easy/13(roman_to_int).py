# roman to integer
s = "IV"
#print(s[0])  -- 1
roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
result = 0
for i in range(len(s)):
    #print(roman[s[i]]) -- 1
    if i +1 < len(s) and roman[s[i]] < roman[s[i+1]]:
        result -= roman[s[i]]
    else:
        result += roman[s[i]]

print(result)

