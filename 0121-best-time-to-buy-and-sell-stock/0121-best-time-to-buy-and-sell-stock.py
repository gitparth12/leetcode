class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, high = 0, 1
        sums = [0] * (len(prices)+1)
        for i, price in enumerate(prices[1:]):
            if prices[high] > prices[low]:
                sums[i] = max(prices[high]-prices[low], sums[i-1])
                high += 1
            else:
                sums[i] = sums[i-1]
                low = high
                high += 1
                
        return max(sums)