class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_value = 0
        maximum = 0
        minimum = 0
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)) :
            old_max = maximum
            old_min = minimum
            maximum = max(nums[i],max(old_min * nums[i],nums[i] * old_max))
            minimum = min(nums[i],min(old_max * nums[i],nums[i] *old_min))
            max_value = max(max_value, maximum)
        return max_value