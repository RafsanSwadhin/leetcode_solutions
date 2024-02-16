prices=[7,1,5,3,6,4]

first_value,second_value = 0,1
max_profit = 0
while second_value < len(prices):
    if prices[second_value] > prices[first_value]:
        profit = prices[second_value]-prices[first_value]
        max_profit = max(profit,max_profit)

    else:
        first_value = second_value
    second_value+=1

print(max_profit) 