class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list = []
        for i in range(len(nums)+1) :
            list.append(i)
        return sum(list) - sum(nums)
        