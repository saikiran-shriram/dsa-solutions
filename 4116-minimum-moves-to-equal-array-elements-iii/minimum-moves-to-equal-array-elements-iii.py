class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        for i in range(len(nums)-1):
            while nums[i] != nums[-1] :
                count += 1
                nums[i] += 1
        return count