class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(speed):
            return sum((pile + speed - 1) // speed for pile in piles) <= h

        l, r = 1, max(piles)  # max value of h is the maximum value in piles
        while l <= r:
            mid = (l + r) // 2

            total_time = 0
            if feasible(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l