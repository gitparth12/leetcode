class Solution:
    opt = {}  # (r, c) : opt(r, c)
    def uniquePaths(self, a: int, b: int) -> int:

        def dp(m: int, n: int) -> int:
            if (m, n) in self.opt:
                return self.opt[(m, n)]
            # base case
            if m == 0 or n == 0:
                return 1
            left = dp(m, n-1)
            right = dp(m-1, n)

            self.opt[(m, n)] = left + right
            print(m, n, self.opt[(m, n)])
            return self.opt[(m, n)]

        return dp(a-1, b-1)


# only r+1 or c+1 as movement
# opt(r, c) = opt(r-1, c) + opt(r, c-1)
# base case: when r == 0 or c == 0 -> default to 0 for that term