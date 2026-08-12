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

# Palindrome Number 
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x ):
            return False
        rev = 0
        while x> rev :
            rev = rev * 10 + x%10
            x = x//10
        return rev == x or rev // 10 == x
       
# Jump Game 
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
        return True

        
# Jump Game II
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_end = 0
        jumps = 0
        farthest = 0
        for i in range(len(nums)-1) :
            farthest = max(farthest, i + nums[i])
            if i == current_end:  
                jumps += 1
                current_end = farthest
        return jumps  

# Maximum Product Subarray
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        max_product = nums[0]
        min_product = nums[0]

        for num in nums[1:] :
            if num < 0:
                max_product , min_product = min_product, max_product
            max_product = max(num , num* max_product)
            min_product = min(num , num* min_product)
            result = max(result, max_product)
            
        return result

