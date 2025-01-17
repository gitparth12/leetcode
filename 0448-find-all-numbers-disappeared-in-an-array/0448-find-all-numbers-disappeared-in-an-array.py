class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hs = set(nums)
        missing = []
        
        for i in range(1, len(nums)+1):
            if i not in hs:
                missing.append(i)
        return missing