class Solution:
    def longestSquareStreak(self, nums: list[int]) -> int:
        nums.sort()
        count = -1
        visited= set()
        for i in range(len(nums)) :
            visited.add(nums[i])
        for i in range(len(nums)):
            val = nums[i]
            length = 0
            while val in visited :
                length +=1 
                val = val*val
            if length >= 2 :
                count = max(length,count)
        return count