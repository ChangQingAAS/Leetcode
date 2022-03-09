class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            # 记录最小价格
            if price < min_price:
                min_price = price
            # 记录最大利润
            if price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit