# Climbing Stairs - Beat 100%
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = 2
        count = 0
        if n == 1 :
            return 1
        if n == 2:
            return 2
        i = 1
        while i< n-1:
            count = a + b
            a = b
            b = count
            i = i+1
        return count

# House Robber - Beat 100%
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 :
            return nums[0]
        if len(nums) == 2 :
            return max(nums)
        max_money = [0] * len(nums)
        max_money[0] = nums[0]
        max_money[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)) :
            max_money[i] = max(nums[i] + max_money[i-2], max_money[i-1])
        return max_money[-1]

# House Robber 2 - Beat 100%
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums :
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        def rob(nums) :
            max_money = []
            max_money = [0] * len(nums)
            max_money[0] = nums[0]
            max_money[1] = max(nums[0],nums[1])
            for i in range(2,len(nums)):
                max_money[i] = max(nums[i]+max_money[i-2],max_money[i-1])
            return max_money[-1]
        return max(rob(nums[:-1]),rob(nums[1:]))

# Coin Change
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for coin in coins:
                if coin <= a:
                    dp[a] = min(dp[a], dp[a - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
        
# Unique Paths 
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1] * n for _ in range(m)]

        for i in range(1,m) :
            for j in range(1,n) :
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]


# Decode Ways
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * (len(s)+1)
        dp[0] = 1
        if s and s[0] != '0' :
            dp[1] = 1
        for i in range(2,len(s)+1) :
            one = s[i-1]
            two = s[i-2:i]
            if one != '0' :
                dp[i] += dp[i-1] 
            if '10' <= two <= '26' :
                dp[i] += dp[i-2]
        return dp[len(s)]
            
 
# Partition Equal Subset Sum
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total_sum = sum(nums)
        if total_sum % 2 != 0 :
            return False
        target = total_sum // 2
        dp = [False] * (target +1)
        dp[0] = True
        for num in nums :
            for j in range(target , num -1 ,-1) :
                dp[j] = dp[j] or dp[j-num]
        return dp[target]

        
# Climbing Stairs - Beats 100%
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b= 2
        count =0
        if n== 1:
	        return 1
        if n== 2:
	        return 2
        i = 3
        while i <= n :
	        count = a +b
	        a= b
	        b =count
	        i += 1
        return count
        
# Min Cost Climbing Stairs - Beats 100%
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0] * (len(cost)+1)
        dp [0] = 0
        dp [1] = 0
        for i in range(2,len(cost)+1):
            dp[i] = min(dp[i-1] + cost[i-1] , dp[i-2] + cost[i-2])
        return dp[len(cost)]
