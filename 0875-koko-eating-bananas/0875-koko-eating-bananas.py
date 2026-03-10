class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)  # max value of h is the maximum value in piles
        while l <= r:
            mid = (l + r) // 2

            total_time = 0
            if sum((pile + mid - 1) // mid for pile in piles) <= h:
                r = mid - 1
            else:
                l = mid + 1
        return l
        
