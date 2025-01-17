class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # binary search -> check size of left and right halves at each point to decide direction
        # need to sort first
        # nums.sort()
        # mini, maxi = 0, len(nums) - 1
        # while mini <= maxi:
        #     idx = mini + ((maxi - mini) // 2)
        #     print(idx, nums[idx])
        #     if idx >= len(nums)-1:
        #         return idx
        #     elif nums[idx] == idx:  # number in right half
        #         mini = idx+1
        #     elif nums[idx] > idx:  # number in left half
        #         maxi = idx
        # return idx
        hs = set()
        for num in nums:
            hs.add(num)
        
        for i in range(len(nums)):
            if i not in hs:
                return i

        return len(nums)