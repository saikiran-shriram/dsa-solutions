class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        turtle = 0
        hare = 0
        turtle = nums[turtle]
        new_index = nums[hare]
        hare = nums[new_index]
        while turtle != hare:
            turtle = nums[turtle]
            new_index = nums[hare]
            hare = nums[new_index]
        turtle = 0
        while turtle != hare:
            turtle = nums[turtle]
            hare = nums[hare]
        return turtle