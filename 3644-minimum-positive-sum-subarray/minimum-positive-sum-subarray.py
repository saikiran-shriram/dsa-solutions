class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        answer = float('inf')
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                length = j-i+1
                if l <= length <= r:
                    total = sum(nums[i:j+1])
                    if total > 0 :
                        answer = min(answer,total)
        return answer if answer != float('inf') else -1