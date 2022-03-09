class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        for i in range(0, len(prices) - 1):
            if prices[i+1] - prices[i] > 0 :
                max_profit += prices[i+1] - prices[i]
        return max_profit

# 只要后一天的价格比前一天的价格高，就可以盈利