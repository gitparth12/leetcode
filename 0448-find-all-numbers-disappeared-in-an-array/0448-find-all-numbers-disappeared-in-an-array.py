class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hs = set()
        missing = []
        
        for num in nums:
            hs.add(num)
        
        for i in range(1, len(nums)+1):
            if i not in hs:
                missing.append(i)
        return missing