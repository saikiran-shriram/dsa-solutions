class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        current = []
        total = 0
        def fun(start,current,total):
            if total == target :
                result.append(list(current))
                return
            if total > target :
                return
            for i in range(start,len(candidates)):
                current.append(candidates[i])
                fun(i,current,total + candidates[i])
                if current :
                    current.pop()
            return result
        return fun(0,current,total)

