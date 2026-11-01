class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        result = []
        for i in range(0, len(nums), 2) :
            result.append(int(str(nums[i])+str(nums[i+1])))
        return min(result)
            