class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increase = 1
        decrease = 1
        longest = 1
        for i in range(1,len(nums)) :
            if nums[i] < nums[i-1] :
                decrease += 1
                increase = 1
                longest = max(longest,decrease)
            elif nums[i] > nums[i-1] :
                increase += 1
                decrease = 1
                longest = max(longest,increase)
            else :
                increase = 1
                decrease = 1
        return longest



            

