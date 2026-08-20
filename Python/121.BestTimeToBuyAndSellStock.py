class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            max_profit = price - min_price if price - min_price > max_profit else max_profit
        return max_profit