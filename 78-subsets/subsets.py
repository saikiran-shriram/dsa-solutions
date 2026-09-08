class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        def fun(start, current) :
            c = current[:]
            result.append(c)
            for i in range(start,len(nums)) :
                current.append(nums[i])
                fun(i+1,current)
                current.pop()
            return result
        return fun(0,current)

        