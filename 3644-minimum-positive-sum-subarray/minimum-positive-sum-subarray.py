class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        answer = float('inf')
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                length = j-i+1
                if l <= length <= r and total > 0 :
                    answer = min(answer,total)
        return answer if answer != float('inf') else -1