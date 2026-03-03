class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0: return 1
        dp = [[0] * (amount+1) for c in range(len(coins))]
        for i in range(len(coins)): dp[i][0] = 1
        
        for i, c in enumerate(coins):
            for a in range(1, amount+1):
                rem = a - c
                if rem >= 0:
                    dp[i][a] += dp[i][rem]
                if i > 0:
                    dp[i][a] += dp[i-1][a]
        return dp[-1][-1]