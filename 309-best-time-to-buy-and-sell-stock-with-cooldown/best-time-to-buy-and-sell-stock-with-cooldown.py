class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        hold = -prices[0]
        sold = 0
        rest = 0
        for i in range(1, len(prices)):
            price = prices[i]
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest
            hold = max(hold,rest - price)
            sold = hold + price
            rest = max(prev_rest,prev_sold)
        return max(sold, rest)
