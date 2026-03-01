class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}  # (i, buying)

        def dfs(i: int, buying: bool) -> int:
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            cooldown = dfs(i+1, buying)
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
        return dfs(0, True)


# Solution is to basically try all paths but cache all nodes
# We end up at O(num_nodes) which is O(2n) because 2 states per price