class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        if len(nums) == 1 :
            result.append(nums)
            return result
        def fun(current) :
            for i in range(len(nums)) :
                if nums[i] not in current :
                    current.append(nums[i])
                    if len(current) == len(nums) :
                        c = list(current)
                        result.append(c)
                    else :
                        fun(current)
                    current.remove(nums[i])
            return result
        return fun(current)
