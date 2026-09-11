class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        def fun(current) :
            for i in range(len(nums)) :
                if nums[i] not in current :
                    current.append(nums[i])
                    if len(current) == len(nums) :
                        copy = list(current)
                        result.append(copy)
                    else :
                        fun(current)
                    current.pop()
            return result
        return fun(current)
