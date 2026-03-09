class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i, num in enumerate(nums):
            if i > farthest:
                return False
            farthest = max(farthest, i + num)
        return True

# At each point we keep track of the farthest we can currently reach from previouse numbers
# If the jumps run out, this number wouldn't update and we would become out of reach (return false)