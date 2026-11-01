class Solution:
    def minOperations(self, nums: list[int], locked: list[int], k: int) -> int:
        n = len(nums)
        swaps = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    swaps += 1
        needed = [False] * n
        for i in range(n - 1):
            if max(nums[:i+1]) > min(nums[i+1:]):
                needed[i] = True
                needed[i+1] = True
        unlocks = sum(1 for i in range(n) if needed[i] and locked[i] == 1)
        if unlocks > k:
            return -1
        return swaps + unlocks