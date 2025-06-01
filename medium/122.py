from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pro = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                max_pro = max_pro + (prices[i]-prices[i-1])
        return max_pro
        



## dynamic approach

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        hold = -prices[0]   # Max profit if holding a stock on day 0
        not_hold = 0        # Max profit if not holding a stock on day 0

        for price in prices[1:]:
            new_hold = max(hold, not_hold - price)   # Either keep holding, or buy today
            new_not_hold = max(not_hold, hold + price)  # Either keep not holding, or sell today

            hold = new_hold
            not_hold = new_not_hold

        return not_hold  # We want max profit without holding any stock at the end



"""