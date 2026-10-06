class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]
        dp = [[0] * len(nums) for _ in range(len(nums))]
        for length in range(2, len(nums)):
            for L in range(len(nums) - length):
                R = L + length
                for K in range(L + 1, R) :
                    coins = dp[L][K] + dp[K][R] + nums[L] * nums[K] * nums[R]
                    dp[L][R] = max(dp[L][R], coins)
        return dp[0][len(nums) - 1]
                    

