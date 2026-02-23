class Solution:
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        tab = {0: nums[0], 1: max(nums[0], nums[1])}
        res = max(nums[0], nums[1])
        for i, num in enumerate(nums):
            if i < 2: continue
            res = max(tab[i-1], tab[i-2]+nums[i])
            tab[i] = res
        return res

# n = max(res[n-1], res[n-2] + n)