class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l, r = 0, 1  # Left to buy, right to sell

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                res = max(res, profit)
            else:
                l = r  # Move the left pointer to the right
            r += 1  # Always move the right pointer to the right

        return res
