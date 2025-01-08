class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        max_diff = prices[1] - prices[0]
        min_num = prices[0]

        for i in range(len(prices)):
            if prices[i] - min_num > max_diff:
                max_diff = prices[i] - min_num
            
            if prices[i] < min_num:
                min_num = prices[i]

        return max_diff