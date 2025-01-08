class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end_1 = m-1
        end_2 = n-1
        idx = m+n-1
        while end_2 >= 0:
            if end_1 < 0 or nums2[end_2] >= nums1[end_1]:
                nums1[idx] = nums2[end_2]
                end_2 -= 1
            elif end_2 < 0 or nums1[end_1] > nums2[end_2]:
                nums1[idx] = nums1[end_1]
                end_1 -= 1
            idx -= 1