class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        import heapq
        total = sum(stones)
        target = total // 2 
        dp = [False] * (target + 1)
        dp[0] = True
        best_sum = 0
        for stone in stones:
            for s in range(target, stone - 1, -1):
                if dp[s - stone]:
                    dp[s] = True
        for s in range(target, -1, -1):
            if dp[s]:
                best_sum = s
                break
        return total - 2 * best_sum