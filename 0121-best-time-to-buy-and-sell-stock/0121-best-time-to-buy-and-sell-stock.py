class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        profit = 0
        for i in range(len(prices)):
            if prices[buy] > prices[i]:
                buy = i
            else:
                profit = max(profit, prices[i] - prices[buy])
        return profit