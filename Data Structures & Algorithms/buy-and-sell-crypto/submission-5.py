class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0
        # profit is always new price - old price
        min_price = prices[0]
        for r in range(len(prices)):
            # find the smallest old price
            min_price = min(prices[r], min_price)

            profit = max(profit, prices[r] - min_price)
        
        return profit