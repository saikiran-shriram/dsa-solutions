class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            while nums[i] != max(nums) :
                count += 1
                nums[i] +=1
        return count