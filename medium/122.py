class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pro = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                max_pro = max_pro + (prices[i]-prices[i-1])
        return max_pro