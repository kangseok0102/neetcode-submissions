class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        price = 1
        profit = 0
        max_profit = 0

        for price in range(len(prices)):
            if prices[price] > min_price:
                profit = prices[price] - min_price
                max_profit = max(max_profit, profit)
            else:
                min_price = prices[price] 
        return max_profit
