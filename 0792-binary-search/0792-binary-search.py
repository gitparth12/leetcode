class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        one = self.search(nums[0: len(nums) // 2], target)
        two = self.search(nums[len(nums) // 2: len(nums)], target)

        if one >= 0:
            return one
        elif two >= 0:
            return len(nums[0: len(nums) // 2]) + two
        else:
            return -1