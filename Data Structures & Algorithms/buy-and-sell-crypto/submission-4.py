class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            current_price = prices[i]
            # baically i found the smallest price i could buy something at...
            # i can only sell it at some future date.
            # i should just find the biggest difference from when i bought something
            # this finds the smallest SO FAR
            if  current_price < buy_price:
                buy_price = current_price

            # this calculates the profit from what the smallest is so far to the biggest so far            
            profit = max(profit, current_price - buy_price)

        return profit