class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil
        left = 1
        right = max(piles)  
        while left < right :
            hours_needed = 0
            mid = (left + right) // 2
            k = mid
            for i in range(len(piles)) :
                hours_needed += ceil(piles[i]/k)
            if hours_needed <= h :
                right = mid
            else :
                left = mid + 1
        return left

        