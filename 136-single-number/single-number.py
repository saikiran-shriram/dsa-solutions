class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        dict = {}
        for i in range(len(nums)) :
            if nums[i] in dict :
                dict[nums[i]] += 1
            else :
                dict[nums[i]] = 0
        for key,value in dict.items() :
            if value == 0 :
                return key