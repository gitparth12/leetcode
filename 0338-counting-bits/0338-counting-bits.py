class Solution:

    def countBits(self, n: int) -> List[int]:
        # 1 2 4 8 16 32 64 128
        # 1 2 3 4 5  6  7  8
        # 6 100 - 64
        # store = [0] * (n + 1)
        # sub = 1

        # for i in range(1, n + 1):
        #     if sub * 2 == i:
        #         sub = i
        #     store[i] = store[i - sub] + 1

        # return store
        res = [0] * (n+1)
        for i in range(1, n+1):
            res[i] = (i & 1) + res[i >> 1]
        return res