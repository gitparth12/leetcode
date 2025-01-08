class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ## map numbers to indices
        idx_map = {}
        for i, num in enumerate(nums):
            if idx_map.get(num) is None:
                idx_map[num] = i
            elif abs(i - idx_map[num]) <= k:
                return True
            idx_map[num] = i
        return False