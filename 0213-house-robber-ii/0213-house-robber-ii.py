class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        tab = {0: nums[0], 1: max(nums[0], nums[1])}
        res1 = max(nums[0], nums[1])
        for i, num in enumerate(nums[:-1]):
            if i < 2: continue
            res1 = max(tab[i-1], tab[i-2]+nums[i])
            tab[i] = res1

        if len(nums) == 2:
            return max(nums)
        tab = {1: nums[1], 2: max(nums[1], nums[2])}
        res2 = max(nums[1], nums[2])
        for i, num in enumerate(nums):
            if i < 3: continue
            res2 = max(tab[i-1], tab[i-2]+nums[i])
            tab[i] = res2
        return max(res1, res2)

# n = max(res[n-1], res[n-2] + n) but circle so we run twice, once ignoring 0 and once ignoring -1 and then take max

# 1 2 3 4 5 6