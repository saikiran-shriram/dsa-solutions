class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low<high :
            total_hours = 0
            mid = (low+high)//2
            k = mid
            for i in range(len(piles)):
                total_hours += (piles[i] + k - 1) // k
            if total_hours <= h:
                high = mid
            else :
                low = mid +1
        return low