# At last stage, for final result:
# 1. number of ways at n-1
# 2. number of ways at n-2
# ways(x) = ways(x-2) + ways(x-1) -> no +2 because ways(x-2) can only reach ways(x) by ways(x-2) + 2
# base case: ways(1) = 1, ways(2) = 2
# eg. ways(3) = ways(1) + ways(2) = 3

class Solution:
    table = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        # base case(s) handled through hashmap
        if n <= 2:
            return Solution.table[n]

        # recursive case
        minustwo, minusone = 0, 0
        try:
            minustwo = Solution.table[n-2]
        except KeyError:
            minustwo = self.climbStairs(n-2)
            Solution.table[n-2] = minustwo
        try:
            minusone = Solution.table[n-1]
        except KeyError:
            minusone = self.climbStairs(n-1)
            Solution.table[n-1] = minusone

        return minustwo + minusone