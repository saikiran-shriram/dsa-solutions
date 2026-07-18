# Two Sum 
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)) :
            for j in range(i+1,len(nums)):
                if (nums[i] + nums[j]) == target:
                    return (i,j)


# Best Time to Buy Stock 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit


# Contains Duplicate 
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set1 = set()
        for i in range(len(nums)) :
            if nums[i] in set1 :
                return True
            set1.add(nums[i])
        return False


# Maximum Subarray - Beat 100%
class Solution :
    def maxSubArray(self, nums):
        current_sum = 0
        max_sum = nums[0]
    
        for num in nums:
            if current_sum < 0:
                current_sum = num
            else:
                current_sum  = current_sum + num
        
            if current_sum > max_sum:
                max_sum = current_sum
    
        return max_sum
 
# Divisor Game - Beat 100%
class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n%2 == 0
