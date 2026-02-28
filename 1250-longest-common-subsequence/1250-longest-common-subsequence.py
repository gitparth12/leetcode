class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = {}
        
        def subsequence(i: int, j: int) -> int:
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            if text1[i] == text2[j]:
                dp[(i, j)] = 1 + subsequence(i+1, j+1)
                return dp[(i, j)]
            else:
                dp[(i, j)] = max(subsequence(i+1, j), subsequence(i, j+1))
                return dp[(i, j)]
        
        return subsequence(0, 0)

# subproblem at opt(i, j) -> for indices i, j in text1, text2:     (value here being lcs at this cell)
# if text1[i] == text2[j] we move one forward in both directions, return 1 + result of i+1, j+1
# else we return 0 + max of results from down and right directions