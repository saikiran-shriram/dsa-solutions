class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_length = float('inf')
        sum = 0
        for right in range(len(nums)) :
            sum = sum + nums[right]
            while sum >= target:
                min_length = min(min_length,right-left+1)
                sum -= nums[left]
                left += 1
        if min_length == float('inf') :
            min_length = 0
        return min_length 
