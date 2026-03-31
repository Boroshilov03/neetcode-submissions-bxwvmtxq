class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest = prices[0]
        for price in prices:
            if lowest > price:
                lowest = price
            profit = price - lowest
            res = max(profit, res)
        return res

