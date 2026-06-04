# week15-3.py
# LeetCode 714. Best Time to Buy and Sell Stock with Transaction Fee
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def helper(i, hasStack):
            if i==len(prices): return 0
            if hasStack: ans = prices[i] + helper(i+1, False) - fee
            else: ans = -prices[i] + helper(i+1, True)
            return max(ans, helper(i+1, hasStack))
        return helper(0, False)
