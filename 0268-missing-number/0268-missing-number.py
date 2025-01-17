class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hs = set(nums)
        
        for i in range(len(nums)):
            if i not in hs:
                return i

        return len(nums)