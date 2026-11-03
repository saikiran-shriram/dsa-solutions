class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count = 0
        maximum = max(nums)
        for i in range(len(nums)):
            count += maximum - nums[i]
        return count