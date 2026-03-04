class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}  # (i, target) = num_ways 

        def dfs(i, target):
            if i >= len(nums):
                return 0
            if i == len(nums) - 1:
                count = 0
                if nums[i] == target:
                    count += 1
                if -nums[i] == target:
                    count += 1
                return count
            if (i, target) in dp:
                return dp[(i, target)]
            
            print(f'i: {i}, target: {target}')
            add = dfs(i+1, target + nums[i])
            sub = dfs(i+1, target - nums[i])
            dp[(i, target)] = add + sub
            return dp[(i, target)]
        return dfs(0, target)
            

# since we can only add or subtract, not skip the number entirely,
# at each number we have two choices =>
# 1. add the number and 2. subtract the number
# To know what to do, we need information computed already (maybe bottom up):
#   For the last number see if we can sum to target - current or target + current
#   This will let us either sum up to or subtract
#   In a top-down way we can recurse and keep setting a new target depending on the current number
