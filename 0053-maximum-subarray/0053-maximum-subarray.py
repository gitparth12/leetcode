class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.greedy(nums)
    
    def greedy(self, nums: List[int]) -> int:
        current, max_sum = 0, nums[0]
        for num in nums:
            if current < 0:
                current = 0
            current += num
            max_sum = max(max_sum, current)
        return max_sum

    def dp(self, nums: List[int]) -> int:
        store = nums.copy()
        for i in range(1, len(nums)):
            store[i] = max(nums[i], store[i-1] + nums[i])
        return max(store)