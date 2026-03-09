class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        current_end = 0
        jumps = 0

        for i, num in enumerate(nums[:-1]):
            farthest = max(farthest, i + num)
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps


# keep track of:
#   farthest (spot we can reach currently)
#   current_end (farthest spot using the last jump we took which could be from a range of spots)
#   jumps (number of jumps so far)