class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i, num in enumerate(nums):
            if num > 0:
                break  # not possible to sum to 0
            if i > 0 and num == nums[i-1]:
                continue  # since we would've considered this number last time
            ## for nums[i], check all numbers between nums[i+1] and nums[-1] to see if we can form a triplet
            l, r = i+1, len(nums) - 1
            while l < r:
                sum_val = nums[i] + nums[l] + nums[r]
                if sum_val == 0:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif sum_val < 0:
                    l += 1
                elif sum_val > 0:
                    r -= 1
        return output