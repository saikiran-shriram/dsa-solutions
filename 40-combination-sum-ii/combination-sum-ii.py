class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        path = []

        def fun(start , current_sum) :
            if current_sum == target:
                result.append(path.copy())
                return
            if current_sum > target:
                return    
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target - current_sum:
                    break
                path.append(candidates[i])
                fun(i+1, current_sum + candidates[i])
                path.pop()

        fun(0, 0)
        return result
        
