class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}

        def dfs(i: int) -> int:
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0
            
            res = dfs(i + 1)
            if i < len(s) - 1:
                if (s[i] == '1' or
                (s[i] == '2' and s[i+1] < '7')):
                    res += dfs(i + 2)
            dp[i] = res
            return res
        return dfs(0)
            

            

# At each point, our choices are to decode singular number or a pair (skipping the next number)
# This makes opt(i) = opt(i+1) + opt(i+2) for top-down dp
#       but we have to account for startin with 0, and checking for 6 and less when starting with 2