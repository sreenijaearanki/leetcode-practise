class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        # sell =prices[i]-buy
        profit=0
        for i in range(len(prices)):
            if prices[i]<buy:
                buy=prices[i]
            profit=max(profit, prices[i]-buy)
        return profit
