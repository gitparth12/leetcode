class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return bottom_up(triangle)

def bottom_up(triangle: List[List[int]]) -> int:
    # dp = triangle[-1]  # Can do inplace by treating current row in triangle as dp
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] = triangle[i][j] + min(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]

def top_down(triangle: List[List[int]]) -> int:
    dp = {}  # (i, j) = min sum path from triangle[i][j] to bottom
    def dfs(i, j):
        if i == len(triangle)-1:
            return triangle[i][j]
        if (i, j) in dp:
            return dp[(i, j)]
        
        dp[(i, j)] = triangle[i][j] + min(dfs(i+1, j), dfs(i+1, j+1))
        return dp[(i, j)]
    return dfs(0, 0)

# dp solution: at the top, we need to know which path leads to the minimum sum
# for a top-down solution, dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
# bottom-up optimisation: keep track of only two rows because we never go past 1 row access